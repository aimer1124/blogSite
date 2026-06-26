#!/usr/bin/env bash
set -euo pipefail

# Resolve repo root so the script works regardless of CWD.
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

CMD=${1:-server}
shift || true

# Prefer the pnpm-provisioned Hugo Extended (devDependency "hugo-extended"),
# fall back to a system-installed hugo (e.g. `brew install hugo`).
LOCAL_HUGO="$ROOT/node_modules/.bin/hugo"
if [[ -x "$LOCAL_HUGO" ]]; then
  HUGO="$LOCAL_HUGO"
elif command -v hugo >/dev/null 2>&1; then
  HUGO="hugo"
else
  echo "未找到 Hugo。请先运行 'pnpm install'（会自动安装 Hugo Extended），" >&2
  echo "或手动安装：brew install hugo（需 extended 版本）。" >&2
  exit 1
fi

exec "$HUGO" "$CMD" "$@"
