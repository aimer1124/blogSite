#!/usr/bin/env bash
set -euo pipefail

# Scaffold a new post as a Hugo page bundle:
#   content/posts/<分类>/<slug>/index.md
# Front matter (ISO8601 date, draft:true, explicit slug, category) comes from
# archetypes/posts.md. Co-locate this post's images next to index.md.
#
# Usage:
#   pnpm new "文章标题"                 # 分类默认 Blog，slug 由标题推导
#   pnpm new "文章标题" Run             # 指定分类
#   pnpm new "文章标题" Run my-slug     # 指定分类与 slug（英文 slug 更利于 URL）

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

TITLE="${1:-}"
CATEGORY="${2:-Blog}"
SLUG="${3:-}"

if [[ -z "$TITLE" ]]; then
  echo '用法: pnpm new "文章标题" [分类] [slug]' >&2
  exit 1
fi

# Derive a slug from the title when not provided.
# ASCII titles become kebab-case; non-ASCII (中文) is kept as-is (站点已允许中文路径)。
if [[ -z "$SLUG" ]]; then
  SLUG="$(printf '%s' "$TITLE" \
    | tr '[:upper:]' '[:lower:]' \
    | sed -E 's/[[:space:]]+/-/g; s#[/\\?%*:|"<>.,]+#-#g; s/-+/-/g; s/^-+//; s/-+$//')"
fi

REL="posts/${CATEGORY}/${SLUG}/index.md"
TARGET="$ROOT/content/$REL"

if [[ -e "$TARGET" ]]; then
  echo "已存在，换个 slug 或分类: content/$REL" >&2
  exit 1
fi

HUGO_POST_TITLE="$TITLE" HUGO_POST_CATEGORY="$CATEGORY" "$ROOT/scripts/run-hugo.sh" new "$REL"

echo "✓ 已创建: content/$REL"
echo "  写完后把 draft 改成 false，图片放在同目录用相对路径引用。"
echo "  本地预览: pnpm dev  →  http://localhost:1313"
