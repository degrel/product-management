// Figma Bridge — Plugin Sandbox Code
// Receives actions from the UI iframe (which relays from the MCP WebSocket server)
// Executes figma.* API calls and sends results back

figma.showUI(__html__, { visible: true, width: 200, height: 50 });

// --- Helpers ---

function hexToRgb(hex: string): RGB {
  const h = hex.replace("#", "");
  return {
    r: parseInt(h.substring(0, 2), 16) / 255,
    g: parseInt(h.substring(2, 4), 16) / 255,
    b: parseInt(h.substring(4, 6), 16) / 255,
  };
}

function rgbToHex(r: number, g: number, b: number): string {
  const toHex = (v: number) =>
    Math.round(v * 255)
      .toString(16)
      .padStart(2, "0");
  return `#${toHex(r)}${toHex(g)}${toHex(b)}`;
}

function findNodeById(id: string): BaseNode | null {
  return figma.getNodeById(id);
}

function getParent(parentId?: string): BaseNode & ChildrenMixin {
  if (parentId) {
    const node = findNodeById(parentId);
    if (node && "children" in node) return node as BaseNode & ChildrenMixin;
  }
  return figma.currentPage;
}

function nodeInfo(node: SceneNode): Record<string, any> {
  return {
    ok: true,
    nodeId: node.id,
    name: node.name,
    type: node.type,
  };
}

async function loadFont(family: string, style: string = "Regular"): Promise<FontName> {
  const candidates = [
    { family, style },
    { family: "Inter", style: "Regular" },
    { family: "Roboto", style: "Regular" },
    { family: "Arial", style: "Regular" },
  ];
  for (const font of candidates) {
    try {
      await figma.loadFontAsync(font);
      return font;
    } catch (_e) {
      continue;
    }
  }
  throw new Error("No available font found");
}

// --- Action Handlers ---

type ActionHandler = (args: Record<string, any>) => Promise<any>;

const actions: Record<string, ActionHandler> = {
  // --- Ping ---
  async ping() {
    return { ok: true, timestamp: Date.now() };
  },

  // --- Creation ---
  async create_frame(args) {
    const frame = figma.createFrame();
    frame.name = args.name || "Frame";
    frame.x = args.x ?? 0;
    frame.y = args.y ?? 0;
    frame.resize(args.width ?? 400, args.height ?? 300);

    if (args.fill) {
      frame.fills = [{ type: "SOLID", color: hexToRgb(args.fill) }];
    }

    if (args.autoLayout && args.autoLayout !== "NONE") {
      frame.layoutMode = args.autoLayout;
      if (args.padding !== undefined) {
        frame.paddingTop = args.padding;
        frame.paddingBottom = args.padding;
        frame.paddingLeft = args.padding;
        frame.paddingRight = args.padding;
      }
      if (args.itemSpacing !== undefined) {
        frame.itemSpacing = args.itemSpacing;
      }
    }

    getParent(args.parentId).appendChild(frame);
    return nodeInfo(frame);
  },

  async create_rectangle(args) {
    const rect = figma.createRectangle();
    rect.name = args.name || "Rectangle";
    rect.x = args.x ?? 0;
    rect.y = args.y ?? 0;
    rect.resize(args.width ?? 100, args.height ?? 100);

    if (args.fill) {
      rect.fills = [{ type: "SOLID", color: hexToRgb(args.fill) }];
    }
    if (args.cornerRadius !== undefined) {
      rect.cornerRadius = args.cornerRadius;
    }

    getParent(args.parentId).appendChild(rect);
    return nodeInfo(rect);
  },

  async add_text(args) {
    const text = figma.createText();
    const fontFamily = args.fontFamily || "Inter";
    const fontStyle = args.fontWeight && args.fontWeight >= 700 ? "Bold" : "Regular";
    const loadedFont = await loadFont(fontFamily, fontStyle);

    text.fontName = loadedFont;
    text.characters = args.text;
    text.name = args.name || args.text.substring(0, 30);
    text.x = args.x ?? 0;
    text.y = args.y ?? 0;
    text.fontSize = args.fontSize ?? 16;

    if (args.fill) {
      text.fills = [{ type: "SOLID", color: hexToRgb(args.fill) }];
    }

    getParent(args.parentId).appendChild(text);
    return nodeInfo(text);
  },

  async create_ellipse(args) {
    const ellipse = figma.createEllipse();
    ellipse.name = args.name || "Ellipse";
    ellipse.x = args.x ?? 0;
    ellipse.y = args.y ?? 0;
    ellipse.resize(args.width ?? 100, args.height ?? 100);

    if (args.fill) {
      ellipse.fills = [{ type: "SOLID", color: hexToRgb(args.fill) }];
    }

    getParent(args.parentId).appendChild(ellipse);
    return nodeInfo(ellipse);
  },

  // --- Styling ---
  async set_fill(args) {
    const node = findNodeById(args.nodeId);
    if (!node || !("fills" in node)) return { ok: false, error: "Node not found or not fillable" };

    const paint: SolidPaint = {
      type: "SOLID",
      color: hexToRgb(args.color),
      opacity: args.opacity ?? 1,
    };
    (node as GeometryMixin).fills = [paint];
    return { ok: true, nodeId: args.nodeId };
  },

  async set_stroke(args) {
    const node = findNodeById(args.nodeId);
    if (!node || !("strokes" in node)) return { ok: false, error: "Node not found or no strokes" };

    const geo = node as GeometryMixin;
    geo.strokes = [
      { type: "SOLID", color: hexToRgb(args.color), opacity: args.opacity ?? 1 },
    ];
    geo.strokeWeight = args.weight ?? 1;
    return { ok: true, nodeId: args.nodeId };
  },

  async set_opacity(args) {
    const node = findNodeById(args.nodeId) as SceneNode;
    if (!node) return { ok: false, error: "Node not found" };
    node.opacity = args.opacity;
    return { ok: true, nodeId: args.nodeId };
  },

  // --- Layout ---
  async set_auto_layout(args) {
    const node = findNodeById(args.nodeId) as FrameNode;
    if (!node || node.type !== "FRAME") return { ok: false, error: "Node not found or not a frame" };

    node.layoutMode = args.direction;
    if (args.padding !== undefined) {
      node.paddingTop = args.padding;
      node.paddingBottom = args.padding;
      node.paddingLeft = args.padding;
      node.paddingRight = args.padding;
    }
    if (args.paddingTop !== undefined) node.paddingTop = args.paddingTop;
    if (args.paddingBottom !== undefined) node.paddingBottom = args.paddingBottom;
    if (args.paddingLeft !== undefined) node.paddingLeft = args.paddingLeft;
    if (args.paddingRight !== undefined) node.paddingRight = args.paddingRight;
    if (args.itemSpacing !== undefined) node.itemSpacing = args.itemSpacing;
    if (args.primaryAlignItems) node.primaryAxisAlignItems = args.primaryAlignItems;
    if (args.counterAlignItems) node.counterAxisAlignItems = args.counterAlignItems;

    return { ok: true, nodeId: args.nodeId };
  },

  async resize_node(args) {
    const node = findNodeById(args.nodeId) as SceneNode;
    if (!node || !("resize" in node)) return { ok: false, error: "Node not found or not resizable" };
    (node as any).resize(args.width, args.height);
    return { ok: true, nodeId: args.nodeId };
  },

  async set_position(args) {
    const node = findNodeById(args.nodeId) as SceneNode;
    if (!node) return { ok: false, error: "Node not found" };
    node.x = args.x;
    node.y = args.y;
    return { ok: true, nodeId: args.nodeId };
  },

  // --- Components ---
  async create_instance(args) {
    try {
      const component = await figma.importComponentByKeyAsync(args.componentKey);
      const instance = component.createInstance();
      instance.x = args.x ?? 0;
      instance.y = args.y ?? 0;
      getParent(args.parentId).appendChild(instance);
      return nodeInfo(instance);
    } catch (e: any) {
      // Try to list available components for auto-correction
      const components = figma.currentPage.findAll(
        (n) => n.type === "COMPONENT"
      ) as ComponentNode[];
      const available = components.slice(0, 20).map((c) => ({
        name: c.name,
        key: c.key,
      }));
      return {
        ok: false,
        error: `Component key not found: ${e.message}`,
        availableComponents: available,
      };
    }
  },

  async set_text_content(args) {
    const node = findNodeById(args.nodeId) as TextNode;
    if (!node || node.type !== "TEXT") return { ok: false, error: "Node not found or not a text node" };

    await loadFont(
      (node.fontName as FontName).family,
      (node.fontName as FontName).style
    );
    node.characters = args.text;
    return { ok: true, nodeId: args.nodeId };
  },

  async delete_node(args) {
    const node = findNodeById(args.nodeId) as SceneNode;
    if (!node) return { ok: false, error: "Node not found" };
    node.remove();
    return { ok: true };
  },

  // --- Query ---
  async find_nodes(args) {
    const parent = args.parentId
      ? (findNodeById(args.parentId) as BaseNode & ChildrenMixin)
      : figma.currentPage;

    if (!parent || !("findAll" in parent)) {
      return { ok: false, error: "Parent not found" };
    }

    const nodes = parent.findAll((n: BaseNode) => {
      if (args.type && n.type !== args.type) return false;
      if (args.name && !n.name.toLowerCase().includes(args.name.toLowerCase())) return false;
      return true;
    }) as SceneNode[];

    return {
      ok: true,
      count: nodes.length,
      nodes: nodes.slice(0, 50).map((n) => ({
        nodeId: n.id,
        name: n.name,
        type: n.type,
      })),
    };
  },

  async get_selection() {
    const sel = figma.currentPage.selection;
    return {
      ok: true,
      count: sel.length,
      nodes: sel.map((n) => ({
        nodeId: n.id,
        name: n.name,
        type: n.type,
      })),
    };
  },

  async get_node_properties(args) {
    const node = findNodeById(args.nodeId) as SceneNode;
    if (!node) return { ok: false, error: "Node not found" };

    const props: Record<string, any> = {
      ok: true,
      nodeId: node.id,
      name: node.name,
      type: node.type,
      x: node.x,
      y: node.y,
      width: node.width,
      height: node.height,
      visible: node.visible,
      opacity: node.opacity,
    };

    if ("fills" in node) {
      const fills = (node as GeometryMixin).fills;
      if (Array.isArray(fills)) {
        props.fills = fills.map((f: Paint) => {
          if (f.type === "SOLID") {
            return { type: "SOLID", color: rgbToHex(f.color.r, f.color.g, f.color.b), opacity: f.opacity };
          }
          return { type: f.type };
        });
      }
    }

    if ("strokes" in node) {
      const strokes = (node as GeometryMixin).strokes;
      if (Array.isArray(strokes)) {
        props.strokes = strokes.map((s: Paint) => {
          if (s.type === "SOLID") {
            return { type: "SOLID", color: rgbToHex(s.color.r, s.color.g, s.color.b) };
          }
          return { type: s.type };
        });
      }
      props.strokeWeight = (node as GeometryMixin).strokeWeight;
    }

    if ("layoutMode" in node) {
      const frame = node as FrameNode;
      props.layoutMode = frame.layoutMode;
      props.paddingTop = frame.paddingTop;
      props.paddingBottom = frame.paddingBottom;
      props.paddingLeft = frame.paddingLeft;
      props.paddingRight = frame.paddingRight;
      props.itemSpacing = frame.itemSpacing;
    }

    if ("characters" in node) {
      props.characters = (node as TextNode).characters;
      props.fontSize = (node as TextNode).fontSize;
    }

    if ("children" in node) {
      props.childCount = (node as FrameNode).children.length;
    }

    return props;
  },

  async get_children(args) {
    const node = findNodeById(args.nodeId) as BaseNode & ChildrenMixin;
    if (!node || !("children" in node)) {
      return { ok: false, error: "Node not found or has no children" };
    }

    return {
      ok: true,
      count: node.children.length,
      children: node.children.map((c: SceneNode) => ({
        nodeId: c.id,
        name: c.name,
        type: c.type,
      })),
    };
  },

  // --- Design System Extraction ---
  async extract_local_styles() {
    const paintStyles = figma.getLocalPaintStyles();
    const textStyles = figma.getLocalTextStyles();
    const effectStyles = figma.getLocalEffectStyles();

    return {
      ok: true,
      paintStyles: paintStyles.map((s) => ({
        name: s.name,
        description: s.description,
        paints: s.paints.map((p: Paint) => {
          if (p.type === "SOLID") {
            return { type: "SOLID", color: rgbToHex(p.color.r, p.color.g, p.color.b), opacity: p.opacity };
          }
          return { type: p.type };
        }),
      })),
      textStyles: textStyles.map((s) => ({
        name: s.name,
        description: s.description,
        fontFamily: s.fontName.family,
        fontStyle: s.fontName.style,
        fontSize: s.fontSize,
        lineHeight: s.lineHeight,
        letterSpacing: s.letterSpacing,
      })),
      effectStyles: effectStyles.map((s) => ({
        name: s.name,
        description: s.description,
        effects: s.effects.map((e) => ({ type: e.type, visible: e.visible })),
      })),
    };
  },

  async extract_components() {
    const components = figma.currentPage.findAll(
      (n) => n.type === "COMPONENT" || n.type === "COMPONENT_SET"
    );

    return {
      ok: true,
      count: components.length,
      components: components.slice(0, 100).map((c) => {
        const base: Record<string, any> = {
          nodeId: c.id,
          name: c.name,
          type: c.type,
        };
        if (c.type === "COMPONENT") {
          const comp = c as ComponentNode;
          base.key = comp.key;
          base.description = comp.description;
        }
        if (c.type === "COMPONENT_SET") {
          const set = c as ComponentSetNode;
          base.description = set.description;
          base.children = set.children.map((child) => ({
            nodeId: child.id,
            name: child.name,
            key: (child as ComponentNode).key,
          }));
        }
        return base;
      }),
    };
  },

  async extract_local_variables() {
    try {
      const variables = await figma.variables.getLocalVariablesAsync();
      const collections = await figma.variables.getLocalVariableCollectionsAsync();

      const collectionMap = new Map<string, string>();
      for (const c of collections) {
        collectionMap.set(c.id, c.name);
      }

      return {
        ok: true,
        count: variables.length,
        collections: collections.map((c) => ({
          id: c.id,
          name: c.name,
          modes: c.modes,
        })),
        variables: variables.slice(0, 200).map((v) => ({
          id: v.id,
          name: v.name,
          resolvedType: v.resolvedType,
          collection: collectionMap.get(v.variableCollectionId) || v.variableCollectionId,
          valuesByMode: v.valuesByMode,
        })),
      };
    } catch (e: any) {
      return { ok: false, error: `Variables API not available: ${e.message}` };
    }
  },
};

// --- Message Dispatcher ---

figma.ui.onmessage = async (msg: any) => {
  const { id, action, args } = msg;

  if (!id || !action) return;

  const handler = actions[action];
  if (!handler) {
    figma.ui.postMessage({ replyTo: id, error: `Unknown action: ${action}` });
    return;
  }

  try {
    const result = await handler(args || {});
    figma.ui.postMessage({ replyTo: id, result });
  } catch (e: any) {
    figma.ui.postMessage({ replyTo: id, error: e.message || String(e) });
  }
};
