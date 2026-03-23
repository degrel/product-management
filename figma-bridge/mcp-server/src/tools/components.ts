import { z } from "zod";
import { defineTool } from "./registry.js";

defineTool({
  name: "create_instance",
  description: "Create an instance of a component by its key. Returns the new node ID.",
  action: "create_instance",
  schema: z.object({
    componentKey: z.string().describe("Component key from the design system"),
    x: z.coerce.number().optional().describe("X position"),
    y: z.coerce.number().optional().describe("Y position"),
    parentId: z.string().optional().describe("Parent node ID"),
  }),
});

defineTool({
  name: "set_text_content",
  description: "Set the text content of an existing text node.",
  action: "set_text_content",
  schema: z.object({
    nodeId: z.string().describe("Target text node ID"),
    text: z.string().describe("New text content"),
  }),
});

defineTool({
  name: "delete_node",
  description: "Delete a node by ID.",
  action: "delete_node",
  schema: z.object({
    nodeId: z.string().describe("Node ID to delete"),
  }),
});
