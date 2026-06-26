#!/usr/bin/env bash
# 将一篇 Hugo 文章转成公众号可粘贴的 Markdown（详见 scripts/to-wechat.py）。
# 用法: pnpm wechat <文章 index.md 路径或 slug 关键字>
set -euo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)"
exec python3 "$DIR/to-wechat.py" "$@"
