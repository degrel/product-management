/**
 * Design System Extractor — REST API
 * Extracts components, styles, and variables from a Figma file
 * using the Figma REST API with a Personal Access Token.
 *
 * Usage: npx tsx ds-extractor/extract.ts <FILE_KEY> [--token <PAT>]
 *
 * Environment: FIGMA_TOKEN or --token flag
 * Output: knowledge-base/<file-name>-ds.md
 */

const FIGMA_API = "https://api.figma.com/v1";

interface FigmaComponent {
  key: string;
  name: string;
  description: string;
  containing_frame?: { name: string };
}

interface FigmaStyle {
  key: string;
  name: string;
  description: string;
  style_type: string;
}

async function figmaFetch(path: string, token: string): Promise<any> {
  const res = await fetch(`${FIGMA_API}${path}`, {
    headers: { "X-Figma-Token": token },
  });
  if (!res.ok) {
    throw new Error(`Figma API ${res.status}: ${await res.text()}`);
  }
  return res.json();
}

function groupBy<T>(items: T[], keyFn: (item: T) => string): Record<string, T[]> {
  const groups: Record<string, T[]> = {};
  for (const item of items) {
    const key = keyFn(item);
    (groups[key] ||= []).push(item);
  }
  return groups;
}

async function extract(fileKey: string, token: string): Promise<string> {
  console.log(`Extracting design system from file: ${fileKey}`);

  // Parallel fetches
  const [fileData, componentsData, stylesData] = await Promise.all([
    figmaFetch(`/files/${fileKey}?depth=1`, token),
    figmaFetch(`/files/${fileKey}/components`, token),
    figmaFetch(`/files/${fileKey}/styles`, token),
  ]);

  const fileName = fileData.name || fileKey;
  const components: Record<string, FigmaComponent> = componentsData.meta?.components || {};
  const styles: Record<string, FigmaStyle> = stylesData.meta?.styles || {};

  // Try to get variables (may fail if not on a supported plan)
  let variables: any = null;
  try {
    variables = await figmaFetch(`/files/${fileKey}/variables/local`, token);
  } catch {
    console.log("Variables API not available (requires Enterprise plan)");
  }

  // Build markdown
  const lines: string[] = [];
  lines.push(`# Design System: ${fileName}`);
  lines.push("");
  lines.push(`> Extracted on ${new Date().toISOString().split("T")[0]} from Figma file \`${fileKey}\``);
  lines.push("");

  // --- Styles ---
  const styleList = Object.values(styles);
  const stylesByType = groupBy(styleList, (s) => s.style_type);

  if (stylesByType["FILL"]) {
    lines.push("## Color Styles");
    lines.push("");
    lines.push("| Style | Description |");
    lines.push("|-------|-------------|");
    for (const s of stylesByType["FILL"]) {
      lines.push(`| ${s.name} | ${s.description || "-"} |`);
    }
    lines.push("");
  }

  if (stylesByType["TEXT"]) {
    lines.push("## Text Styles");
    lines.push("");
    lines.push("| Style | Description |");
    lines.push("|-------|-------------|");
    for (const s of stylesByType["TEXT"]) {
      lines.push(`| ${s.name} | ${s.description || "-"} |`);
    }
    lines.push("");
  }

  if (stylesByType["EFFECT"]) {
    lines.push("## Effect Styles");
    lines.push("");
    lines.push("| Style | Description |");
    lines.push("|-------|-------------|");
    for (const s of stylesByType["EFFECT"]) {
      lines.push(`| ${s.name} | ${s.description || "-"} |`);
    }
    lines.push("");
  }

  // --- Components ---
  const componentList = Object.values(components);
  if (componentList.length > 0) {
    lines.push("## Components");
    lines.push("");

    const byFrame = groupBy(
      componentList,
      (c) => c.containing_frame?.name || "Uncategorized"
    );

    for (const [frameName, comps] of Object.entries(byFrame)) {
      lines.push(`### ${frameName}`);
      lines.push("");
      lines.push("| Component | Key | Description |");
      lines.push("|-----------|-----|-------------|");
      for (const c of comps) {
        lines.push(`| ${c.name} | \`${c.key}\` | ${c.description || "-"} |`);
      }
      lines.push("");
    }
  }

  // --- Variables ---
  if (variables?.meta?.variables) {
    const vars = Object.values(variables.meta.variables) as any[];
    const collections = Object.values(variables.meta.variableCollections || {}) as any[];

    lines.push("## Variables");
    lines.push("");

    for (const collection of collections) {
      lines.push(`### ${collection.name}`);
      lines.push("");
      const collVars = vars.filter(
        (v: any) => v.variableCollectionId === collection.id
      );
      lines.push("| Variable | Type | Values |");
      lines.push("|----------|------|--------|");
      for (const v of collVars) {
        const values = Object.values(v.valuesByMode || {})
          .map((val: any) => {
            if (typeof val === "object" && "r" in val) {
              return `rgb(${Math.round(val.r * 255)},${Math.round(val.g * 255)},${Math.round(val.b * 255)})`;
            }
            return String(val);
          })
          .join(", ");
        lines.push(`| ${v.name} | ${v.resolvedType} | ${values} |`);
      }
      lines.push("");
    }
  }

  // --- Usage rules (placeholder for PM to fill) ---
  lines.push("## Usage Rules");
  lines.push("");
  lines.push("<!-- PM: Add design system rules, constraints, and anti-patterns here -->");
  lines.push("");
  lines.push("## Anti-patterns");
  lines.push("");
  lines.push("<!-- PM: Add things NOT to do with this design system -->");
  lines.push("");

  return lines.join("\n");
}

// --- CLI ---
async function main() {
  const args = process.argv.slice(2);
  const fileKey = args.find((a) => !a.startsWith("--"));
  const tokenIdx = args.indexOf("--token");
  const token = tokenIdx >= 0 ? args[tokenIdx + 1] : process.env.FIGMA_TOKEN;

  if (!fileKey) {
    console.error("Usage: npx tsx ds-extractor/extract.ts <FILE_KEY> [--token <PAT>]");
    process.exit(1);
  }
  if (!token) {
    console.error("Set FIGMA_TOKEN env var or pass --token <PAT>");
    process.exit(1);
  }

  const markdown = await extract(fileKey, token);

  const { writeFileSync, mkdirSync } = await import("fs");
  const { join } = await import("path");

  const outDir = join(import.meta.dirname || ".", "..", "knowledge-base");
  mkdirSync(outDir, { recursive: true });

  const outFile = join(outDir, `${fileKey}-ds.md`);
  writeFileSync(outFile, markdown, "utf-8");
  console.log(`Written to: ${outFile}`);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
