import { z } from "zod";
import { defineTool } from "./registry.js";

defineTool({
  name: "set_auto_layout",
  description: "Set auto-layout on a frame.",
  action: "set_auto_layout",
  schema: z.object({
    nodeId: z.string().describe("Target frame node ID"),
    direction: z.enum(["HORIZONTAL", "VERTICAL"]).describe("Layout direction"),
    padding: z.coerce.number().optional().describe("Uniform padding"),
    paddingTop: z.coerce.number().optional(),
    paddingBottom: z.coerce.number().optional(),
    paddingLeft: z.coerce.number().optional(),
    paddingRight: z.coerce.number().optional(),
    itemSpacing: z.coerce.number().optional().describe("Gap between children"),
    primaryAlignItems: z.enum(["MIN", "CENTER", "MAX", "SPACE_BETWEEN"]).optional(),
    counterAlignItems: z.enum(["MIN", "CENTER", "MAX"]).optional(),
  }),
});

defineTool({
  name: "resize_node",
  description: "Resize a node.",
  action: "resize_node",
  schema: z.object({
    nodeId: z.string().describe("Target node ID"),
    width: z.coerce.number().describe("New width"),
    height: z.coerce.number().describe("New height"),
  }),
});

defineTool({
  name: "set_position",
  description: "Move a node to a new position.",
  action: "set_position",
  schema: z.object({
    nodeId: z.string().describe("Target node ID"),
    x: z.coerce.number().describe("New X position"),
    y: z.coerce.number().describe("New Y position"),
  }),
});
