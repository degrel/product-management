import { z, ZodObject, ZodRawShape } from "zod";
import { Bridge } from "../bridge.js";

export interface ToolDef {
  name: string;
  description: string;
  schema: ZodObject<ZodRawShape>;
  action: string;
  /** Optional transform before sending to plugin. Default: pass input as-is. */
  transform?: (input: Record<string, any>) => Record<string, any>;
}

const tools: ToolDef[] = [];

export function defineTool(def: ToolDef): void {
  tools.push(def);
}

export function getAllTools(): ToolDef[] {
  return [...tools];
}

export function findTool(name: string): ToolDef | undefined {
  return tools.find((t) => t.name === name);
}

/** Convert Zod schema to JSON Schema (simplified, for MCP registration) */
export function zodToJsonSchema(schema: ZodObject<ZodRawShape>): Record<string, any> {
  const shape = schema.shape;
  const properties: Record<string, any> = {};
  const required: string[] = [];

  for (const [key, val] of Object.entries(shape)) {
    const zodVal = val as z.ZodTypeAny;
    properties[key] = zodFieldToJson(zodVal);
    if (!zodVal.isOptional()) {
      required.push(key);
    }
  }

  return {
    type: "object",
    properties,
    ...(required.length > 0 ? { required } : {}),
  };
}

function zodFieldToJson(field: z.ZodTypeAny): Record<string, any> {
  // Unwrap optional
  if (field instanceof z.ZodOptional) {
    return zodFieldToJson(field.unwrap());
  }
  // Unwrap default
  if (field instanceof z.ZodDefault) {
    const inner = zodFieldToJson((field as any)._def.innerType);
    return { ...inner, default: (field as any)._def.defaultValue() };
  }
  if (field instanceof z.ZodString) {
    return { type: "string", description: field.description };
  }
  if (field instanceof z.ZodNumber) {
    return { type: "number", description: field.description };
  }
  if (field instanceof z.ZodBoolean) {
    return { type: "boolean", description: field.description };
  }
  if (field instanceof z.ZodEnum) {
    return { type: "string", enum: field.options, description: field.description };
  }
  if (field instanceof z.ZodArray) {
    return { type: "array", items: zodFieldToJson(field.element), description: field.description };
  }
  // Fallback
  return { type: "string" };
}
