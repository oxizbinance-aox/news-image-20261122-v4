import { execFileSync } from "node:child_process";
import { createHash } from "node:crypto";
import { existsSync, readFileSync, statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

// Entry point: render the broadsheet by running the deterministic PIL
// drawing script next to this file, then check the output fits the
// competition limits (1024x1024 PNG, at most 1 MiB).
const root = dirname(fileURLToPath(import.meta.url));
const script = join(root, "draw_news22_v4.py");
const out = join(root, "entry.png");

execFileSync("python3", [script], { cwd: root, stdio: "inherit" });

if (!existsSync(out)) {
  throw new Error("draw script did not write entry.png");
}
const size = statSync(out).size;
if (size > 1048576) {
  throw new Error(`entry.png is ${size} bytes, over the 1 MiB limit`);
}
// Verify the PNG header itself: 8-byte signature, then the IHDR chunk
// (width and height as big-endian uint32 at offsets 16 and 20).
const buf = readFileSync(out);
const pngSig = Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]);
if (!buf.subarray(0, 8).equals(pngSig) || buf.toString("ascii", 12, 16) !== "IHDR") {
  throw new Error("entry.png is not a PNG file");
}
const width = buf.readUInt32BE(16);
const height = buf.readUInt32BE(20);
if (width !== 1024 || height !== 1024) {
  throw new Error(`entry.png is ${width}x${height}, must be 1024x1024`);
}
const sha = createHash("sha256").update(buf).digest("hex");
console.log(`entry.png OK: ${size} bytes, 1024x1024, sha256 ${sha}`);
