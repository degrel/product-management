import { z } from "zod";
import { defineTool } from "./registry.js";

defineTool({
  name: "find_nodes",
  description: "Find nodes by name and/or type. Returns matching node IDs and names.",
  action: "find_nodes",
  schema: z.object({
    name: z.string().optional().describe("Name pattern to search for (contains match)"),
    type: z.string().optional().describe("Node type filter: FRAME, TEXT, RECTANGLE, INSTANCE, COMPONENT, etc."),
    parentId: z.string().optional().describe("Scope search to children of this node"),
  }),
});

defineTool({
  name: "get_selection",
  description: "Get currently selected nodes in Figma.",
  action: "get_selection",
  schema: z.object({}),
});

defineTool({
  name: "get_node_properties",
  description: "Get all properties of a node (type, size, position, fills, strokes, effects, etc.).",
  action: "get_node_properties",
  schema: z.object({
    nodeId: z.string().describe("Node ID to inspect"),
  }),
});

defineTool({
  name: "get_children",
  description: "List direct children of a frame or group.",
  action: "get_children",
  schema: z.object({
    nodeId: z.string().describe("Parent node ID"),
  }),
});
