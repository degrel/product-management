import { z } from "zod";
import { defineTool } from "./registry.js";

defineTool({
  name: "create_frame",
  description: "Create a frame in Figma with optional auto-layout. Returns the new node ID.",
  action: "create_frame",
  schema: z.object({
    name: z.string().describe("Frame name"),
    x: z.coerce.number().optional().describe("X position (default 0)"),
    y: z.coerce.number().optional().describe("Y position (default 0)"),
    width: z.coerce.number().optional().describe("Width in px (default 400)"),
    height: z.coerce.number().optional().describe("Height in px (default 300)"),
    fill: z.string().optional().describe("Fill color as hex, e.g. #FFFFFF"),
    autoLayout: z.enum(["HORIZONTAL", "VERTICAL", "NONE"]).optional().describe("Auto-layout direction"),
    padding: z.coerce.number().optional().describe("Uniform padding for auto-layout"),
    itemSpacing: z.coerce.number().optional().describe("Spacing between children in auto-layout"),
    parentId: z.string().optional().describe("Parent node ID to append to"),
  }),
});

defineTool({
  name: "create_rectangle",
  description: "Create a rectangle in Figma. Returns the new node ID.",
  action: "create_rectangle",
  schema: z.object({
    name: z.string().optional().describe("Rectangle name"),
    x: z.coerce.number().optional().describe("X position"),
    y: z.coerce.number().optional().describe("Y position"),
    width: z.coerce.number().optional().describe("Width (default 100)"),
    height: z.coerce.number().optional().describe("Height (default 100)"),
    fill: z.string().optional().describe("Fill color as hex"),
    cornerRadius: z.coerce.number().optional().describe("Corner radius"),
    parentId: z.string().optional().describe("Parent node ID"),
  }),
});

defineTool({
  name: "create_text",
  description: "Create a text node in Figma. Returns the new node ID.",
  action: "add_text",
  schema: z.object({
    text: z.string().describe("Text content"),
    name: z.string().optional().describe("Node name"),
    x: z.coerce.number().optional().describe("X position"),
    y: z.coerce.number().optional().describe("Y position"),
    fontSize: z.coerce.number().optional().describe("Font size (default 16)"),
    fontFamily: z.string().optional().describe("Font family (default Inter)"),
    fontWeight: z.coerce.number().optional().describe("Font weight (default 400)"),
    fill: z.string().optional().describe("Text color as hex"),
    parentId: z.string().optional().describe("Parent node ID"),
  }),
});

defineTool({
  name: "create_ellipse",
  description: "Create an ellipse or circle in Figma. Returns the new node ID.",
  action: "create_ellipse",
  schema: z.object({
    name: z.string().optional().describe("Ellipse name"),
    x: z.coerce.number().optional().describe("X position"),
    y: z.coerce.number().optional().describe("Y position"),
    width: z.coerce.number().optional().describe("Width (default 100)"),
    height: z.coerce.number().optional().describe("Height (default 100)"),
    fill: z.string().optional().describe("Fill color as hex"),
    parentId: z.string().optional().describe("Parent node ID"),
  }),
});
