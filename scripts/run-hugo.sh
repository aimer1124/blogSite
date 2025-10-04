#!/usr/bin/env bash
set -euo pipefail
CMD=${1:-server}
shift || true
if ! command -v hugo >/dev/null 2>&1; then
  echo "未找到系统 hugo，请先安装: brew install hugo (需要 extended 版本)" >&2
  exit 1
fi
exec hugo "$CMD" "$@"
