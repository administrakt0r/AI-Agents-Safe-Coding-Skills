const assert = require("assert");
const { spawnSync } = require("child_process");
const path = require("path");

const repoRoot = path.resolve(__dirname, "..", "..", "..");

function runNpmPackDryRunJson() {
  const result =
    process.platform === "win32"
      ? spawnSync(process.env.ComSpec || "cmd.exe", ["/d", "/s", "/c", "npm pack --dry-run --json"], {
          cwd: repoRoot,
          encoding: "utf8",
        })
      : spawnSync("npm", ["pack", "--dry-run", "--json"], {
          cwd: repoRoot,
          encoding: "utf8",
        });

  if (result.error) {
    throw result.error;
  }

  if (typeof result.status !== "number" || result.status !== 0) {
    throw new Error(result.stderr.trim() || "npm pack --dry-run --json failed");
  }

  return JSON.parse(result.stdout);
}

const packOutput = runNpmPackDryRunJson();
assert.ok(Array.isArray(packOutput) && packOutput.length > 0, "npm pack should return package metadata");

const packagedFiles = new Set(packOutput[0].files.map((file) => file.path));

assert.ok(packagedFiles.has("tools/bin/install.js"), "published package must include tools/bin/install.js");
assert.ok(
  packagedFiles.has("tools/lib/symlink-safety.js"),
  "published package must include tools/lib/symlink-safety.js",
);
