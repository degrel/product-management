/**
 * Design System Extractor — Plugin-based (deep extraction)
 *
 * This script connects to the Figma Bridge and uses the plugin's
 * extraction actions to get detailed design system data that the
 * REST API can't provide (local variables, unpublished components, etc.)
 *
 * Usage: npx tsx ds-extractor/plugin-extract.ts [--output <filename>]
 *
 * Requires: Figma Bridge plugin running and connected.
 */

import { WebSocket } from "ws";
import { v4 as uuidv4 } from "uuid";
import { writeFileSync, mkdirSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";

const WS_URL = "ws://127.0.0.1:3055";
const TIMEOUT = 20_000;

function sendAction(ws: WebSocket, action: string, args: Record<string, any> = {}): Promise<any> {
  return new Promise((resolve, reject) => {
    const id = uuidv4();
    const timer = setTimeout(() => reject(new Error(`Timeout: ${action}`)), TIMEOUT);

    const handler = (raw: Buffer) => {
      try {
        const msg = JSON.parse(raw.toString());
        if (msg.replyTo === id) {
          ws.off("message", handler);
          clearTimeout(timer);
          if (msg.error) reject(new Error(msg.error));
          else resolve(msg.result);
        }
      } catch { /* ignore non-JSON */ }
    };

    ws.on("message", handler);
    ws.send(JSON.stringify({ id, action, args }));
  });
}

function rgbToHex(r: number, g: number, b: number): string {
  const toHex = (v: number) => Math.round(v * 255).toString(16).padStart(2, "0");
  return `#${toHex(r)}${toHex(g)}${toHex(b)}`;
}

async function main() {
  const args = process.argv.slice(2);
  const outputIdx = args.indexOf("--output");
  const outputName = outputIdx >= 0 ? args[outputIdx + 1] : "plugin-ds";

  console.log("Connecting to Figma Bridge...");

  const ws = new WebSocket(WS_URL);
  await new Promise<void>((resolve, reject) => {
    ws.on("open", resolve);
    ws.on("error", reject);
  });

  console.log("Connected. Extracting...");

  // Run all extractions in parallel
  const [styles, components, variables] = await Promise.all([
    sendAction(ws, "extract_local_styles").catch(() => null),
    sendAction(ws, "extract_components").catch(() => null),
    sendAction(ws, "extract_local_variables").catch(() => null),
  ]);

  const lines: string[] = [];
  lines.push("# Design System (Plugin Extraction)");
  lines.push("");
  lines.push(`> Extracted on ${new Date().toISOString().split("T")[0]} via Figma Bridge plugin`);
  lines.push("");

  // --- Color Styles ---
  if (styles?.paintStyles?.length) {
    lines.push("## Color Styles");
    lines.push("");
    lines.push("| Name | Color | Opacity | Description |");
    lines.push("|------|-------|---------|-------------|");
    for (const s of styles.paintStyles) {
      const paint = s.paints[0];
      const color = paint?.color || "-";
      const opacity = paint?.opacity !== undefined ? paint.opacity : 1;
      lines.push(`| ${s.name} | ${color} | ${opacity} | ${s.description || "-"} |`);
    }
    lines.push("");
  }

  // --- Text Styles ---
  if (styles?.textStyles?.length) {
    lines.push("## Text Styles");
    lines.push("");
    lines.push("| Name | Font | Size | Style | Description |");
    lines.push("|------|------|------|-------|-------------|");
    for (const s of styles.textStyles) {
      lines.push(`| ${s.name} | ${s.fontFamily} | ${s.fontSize} | ${s.fontStyle} | ${s.description || "-"} |`);
    }
    lines.push("");
  }

  // --- Effect Styles ---
  if (styles?.effectStyles?.length) {
    lines.push("## Effect Styles");
    lines.push("");
    lines.push("| Name | Effects | Description |");
    lines.push("|------|---------|-------------|");
    for (const s of styles.effectStyles) {
      const effects = s.effects.map((e: any) => e.type).join(", ");
      lines.push(`| ${s.name} | ${effects} | ${s.description || "-"} |`);
    }
    lines.push("");
  }

  // --- Components ---
  if (components?.components?.length) {
    lines.push("## Components");
    lines.push("");
    for (const c of components.components) {
      if (c.type === "COMPONENT_SET") {
        lines.push(`### ${c.name} (Component Set)`);
        lines.push("");
        if (c.description) lines.push(`${c.description}`);
        lines.push("");
        if (c.children?.length) {
          lines.push("| Variant | Key |");
          lines.push("|---------|-----|");
          for (const child of c.children) {
            lines.push(`| ${child.name} | \`${child.key}\` |`);
          }
          lines.push("");
        }
      } else {
        lines.push(`### ${c.name}`);
        lines.push(`- **Key**: \`${c.key}\``);
        if (c.description) lines.push(`- **Description**: ${c.description}`);
        lines.push("");
      }
    }
  }

  // --- Variables ---
  if (variables?.variables?.length) {
    lines.push("## Variables");
    lines.push("");
    for (const col of variables.collections || []) {
      lines.push(`### ${col.name}`);
      lines.push("");
      const collVars = variables.variables.filter(
        (v: any) => v.collection === col.name
      );
      lines.push("| Name | Type | Value |");
      lines.push("|------|------|-------|");
      for (const v of collVars) {
        const values = Object.values(v.valuesByMode || {})
          .map((val: any) => {
            if (typeof val === "object" && "r" in val) {
              return rgbToHex(val.r, val.g, val.b);
            }
            return String(val);
          })
          .join(", ");
        lines.push(`| ${v.name} | ${v.resolvedType} | ${values} |`);
      }
      lines.push("");
    }
  }

  lines.push("## Usage Rules");
  lines.push("");
  lines.push("<!-- PM: Add design system rules here -->");
  lines.push("");
  lines.push("## Anti-patterns");
  lines.push("");
  lines.push("<!-- PM: Add anti-patterns here -->");
  lines.push("");

  const markdown = lines.join("\n");

  const __dirname = dirname(fileURLToPath(import.meta.url));
  const outDir = join(__dirname, "..", "knowledge-base");
  mkdirSync(outDir, { recursive: true });

  const outFile = join(outDir, `${outputName}.md`);
  writeFileSync(outFile, markdown, "utf-8");
  console.log(`Written to: ${outFile}`);

  ws.close();
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
