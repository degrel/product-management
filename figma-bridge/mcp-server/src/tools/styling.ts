import { z } from "zod";
import { defineTool } from "./registry.js";

defineTool({
  name: "set_fill",
  description: "Set the fill color of a node.",
  action: "set_fill",
  schema: z.object({
    nodeId: z.string().describe("Target node ID"),
    color: z.string().describe("Hex color, e.g. #FF5733"),
    opacity: z.coerce.number().optional().describe("Opacity 0-1 (default 1)"),
  }),
});

defineTool({
  name: "set_stroke",
  description: "Set stroke on a node.",
  action: "set_stroke",
  schema: z.object({
    nodeId: z.string().describe("Target node ID"),
    color: z.string().describe("Hex color"),
    weight: z.coerce.number().optional().describe("Stroke weight (default 1)"),
    opacity: z.coerce.number().optional().describe("Opacity 0-1"),
  }),
});

defineTool({
  name: "set_opacity",
  description: "Set opacity of a node.",
  action: "set_opacity",
  schema: z.object({
    nodeId: z.string().describe("Target node ID"),
    opacity: z.coerce.number().describe("Opacity 0-1"),
  }),
});
