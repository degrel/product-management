import { z } from "zod";
import { defineTool } from "./registry.js";

defineTool({
  name: "extract_local_styles",
  description: "Extract all local styles (color, text, effect, grid) from the current Figma file.",
  action: "extract_local_styles",
  schema: z.object({}),
});

defineTool({
  name: "extract_components",
  description: "Extract all local components with their variants, descriptions, and properties.",
  action: "extract_components",
  schema: z.object({}),
});

defineTool({
  name: "extract_local_variables",
  description: "Extract all local variables (colors, numbers, strings) from the current file.",
  action: "extract_local_variables",
  schema: z.object({}),
});

defineTool({
  name: "check_connection",
  description: "Check if the Figma plugin is connected to the bridge.",
  action: "ping",
  schema: z.object({}),
});
