import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { Bridge } from "./bridge.js";
import { getAllTools, findTool } from "./tools/registry.js";

// Import tool definitions (side-effect: registers them)
import "./tools/creation.js";
import "./tools/styling.js";
import "./tools/layout.js";
import "./tools/components.js";
import "./tools/query.js";
import "./tools/ds-tools.js";

const bridge = new Bridge();

const server = new McpServer({
  name: "figma-bridge",
  version: "0.1.0",
});

// Register all tools with the MCP server
for (const tool of getAllTools()) {
  server.tool(
    tool.name,
    tool.description,
    tool.schema.shape,
    async (input: Record<string, any>) => {
      // Special case: check_connection doesn't need a real plugin round-trip
      if (tool.name === "check_connection") {
        if (bridge.isConnected) {
          try {
            const result = await bridge.sendToPlugin("ping", {});
            return {
              content: [
                {
                  type: "text" as const,
                  text: JSON.stringify({ ok: true, ...bridge.fileInfo, ...result }, null, 2),
                },
              ],
            };
          } catch (e: any) {
            return {
              content: [
                {
                  type: "text" as const,
                  text: JSON.stringify({ ok: false, error: e.message }),
                },
              ],
            };
          }
        } else {
          return {
            content: [
              {
                type: "text" as const,
                text: JSON.stringify({
                  ok: false,
                  error: "Plugin not connected. Open Figma and run the Figma Bridge plugin.",
                }),
              },
            ],
          };
        }
      }

      // Standard tool: forward to plugin
      try {
        const args = tool.transform ? tool.transform(input) : input;
        const result = await bridge.sendToPlugin(tool.action, args);
        return {
          content: [
            {
              type: "text" as const,
              text: JSON.stringify(result, null, 2),
            },
          ],
        };
      } catch (e: any) {
        return {
          content: [
            {
              type: "text" as const,
              text: JSON.stringify({ ok: false, error: e.message }),
            },
          ],
          isError: true,
        };
      }
    }
  );
}

async function main() {
  bridge.start();

  const transport = new StdioServerTransport();
  await server.connect(transport);

  // Graceful shutdown
  process.on("SIGINT", () => {
    bridge.stop();
    process.exit(0);
  });
  process.on("SIGTERM", () => {
    bridge.stop();
    process.exit(0);
  });
}

main().catch((err) => {
  console.error("Fatal error:", err);
  process.exit(1);
});
