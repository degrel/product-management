import { WebSocketServer, WebSocket } from "ws";
import { v4 as uuidv4 } from "uuid";

const PORT = 3055;
const ACTION_TIMEOUT_MS = 15_000;
const QUEUE_EXPIRY_MS = 30_000;

interface PendingRequest {
  resolve: (value: any) => void;
  reject: (reason: Error) => void;
  timer: ReturnType<typeof setTimeout>;
}

interface QueuedMessage {
  data: string;
  expiresAt: number;
}

interface PluginInfo {
  fileKey?: string;
  fileName?: string;
}

export class Bridge {
  private wss: WebSocketServer | null = null;
  private pluginSocket: WebSocket | null = null;
  private pending = new Map<string, PendingRequest>();
  private queue: QueuedMessage[] = [];
  private pluginInfo: PluginInfo = {};

  get isConnected(): boolean {
    return (
      this.pluginSocket !== null &&
      this.pluginSocket.readyState === WebSocket.OPEN
    );
  }

  get fileInfo(): PluginInfo {
    return { ...this.pluginInfo };
  }

  start(): void {
    if (this.wss) return;

    this.wss = new WebSocketServer({ host: "127.0.0.1", port: PORT });

    this.wss.on("connection", (ws) => {
      // Only one plugin connection at a time
      if (this.pluginSocket && this.pluginSocket.readyState === WebSocket.OPEN) {
        this.pluginSocket.close();
      }

      this.pluginSocket = ws;

      ws.on("message", (raw) => {
        let msg: any;
        try {
          msg = JSON.parse(raw.toString());
        } catch {
          return;
        }

        // Handshake
        if (msg.hello === "from-plugin-ui") {
          this.pluginInfo = {
            fileKey: msg.fileKey,
            fileName: msg.fileName,
          };
          this.flushQueue();
          return;
        }

        // Response to a pending request
        if (msg.replyTo && this.pending.has(msg.replyTo)) {
          const req = this.pending.get(msg.replyTo)!;
          this.pending.delete(msg.replyTo);
          clearTimeout(req.timer);

          if (msg.error) {
            req.reject(new Error(msg.error));
          } else {
            req.resolve(msg.result ?? { ok: true });
          }
        }
      });

      ws.on("close", () => {
        if (this.pluginSocket === ws) {
          this.pluginSocket = null;
        }
      });

      ws.on("error", () => {
        if (this.pluginSocket === ws) {
          this.pluginSocket = null;
        }
      });
    });
  }

  stop(): void {
    // Reject all pending
    for (const [id, req] of this.pending) {
      clearTimeout(req.timer);
      req.reject(new Error("Bridge shutting down"));
    }
    this.pending.clear();
    this.queue = [];

    if (this.pluginSocket) {
      this.pluginSocket.close();
      this.pluginSocket = null;
    }
    if (this.wss) {
      this.wss.close();
      this.wss = null;
    }
  }

  sendToPlugin(action: string, args: Record<string, any> = {}): Promise<any> {
    const id = uuidv4();
    const payload = JSON.stringify({ id, action, args });

    return new Promise((resolve, reject) => {
      const timer = setTimeout(() => {
        this.pending.delete(id);
        reject(new Error(`Timeout after ${ACTION_TIMEOUT_MS}ms for action "${action}"`));
      }, ACTION_TIMEOUT_MS);

      this.pending.set(id, { resolve, reject, timer });

      if (this.isConnected) {
        this.pluginSocket!.send(payload);
      } else {
        // Queue for when plugin reconnects
        this.queue.push({
          data: payload,
          expiresAt: Date.now() + QUEUE_EXPIRY_MS,
        });
      }
    });
  }

  private flushQueue(): void {
    const now = Date.now();
    const live: QueuedMessage[] = [];

    for (const item of this.queue) {
      if (item.expiresAt > now && this.isConnected) {
        this.pluginSocket!.send(item.data);
      } else if (item.expiresAt > now) {
        live.push(item);
      } else {
        // Expired — reject the pending promise
        try {
          const msg = JSON.parse(item.data);
          const req = this.pending.get(msg.id);
          if (req) {
            clearTimeout(req.timer);
            req.reject(new Error("Queued message expired (plugin not connected)"));
            this.pending.delete(msg.id);
          }
        } catch {
          // ignore parse errors
        }
      }
    }

    this.queue = live;
  }
}
