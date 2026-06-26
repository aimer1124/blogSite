#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
把一篇 Hugo 文章转成「可直接粘进微信公众号编辑器」的 Markdown。

做两件事：
  1) 去掉 front matter（YAML --- 或 TOML +++）。
  2) 把正文里的相对图片引用改写成 https://<站点>/... 绝对地址，
     这样公众号粘贴时能自动抓取并转存图片（外链图保持不变）。

文章 URL 通过 `hugo list all` 精确获取（不靠猜路径），保证与线上一致。

用法:
  pnpm wechat content/posts/Upgrade/word-practice/index.md   # 直接给路径
  pnpm wechat word-practice                                  # 或给 slug/目录关键字
输出:
  写入 dist/wechat/<slug>.md，同时打印到标准输出（可重定向/管道）。
"""
import sys, os, re, csv, io, subprocess, urllib.parse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def find_md(arg):
    """把入参解析为某篇文章的 markdown 文件路径。"""
    if os.path.isfile(arg):
        return os.path.abspath(arg)
    hits = []
    for dp, _, fs in os.walk(os.path.join(ROOT, "content")):
        for f in fs:
            if not f.endswith(".md"):
                continue
            full = os.path.join(dp, f)
            # 关键字命中目录名（page bundle）或文件名
            if arg in os.path.basename(dp) or arg in f:
                # 优先 index.md（page bundle）
                hits.insert(0 if f == "index.md" else len(hits), full)
    return hits[0] if hits else None


def permalink_for(md):
    """用 `hugo list all` 查这篇文章的线上绝对 URL。"""
    hugo = os.path.join(ROOT, "node_modules/.bin/hugo")
    if not os.path.exists(hugo):
        hugo = "hugo"
    out = subprocess.run([hugo, "list", "all"], cwd=ROOT,
                         capture_output=True, text=True).stdout
    rel = os.path.relpath(md, ROOT)
    for row in csv.DictReader(io.StringIO(out)):
        if os.path.normpath(row.get("path", "")) == os.path.normpath(rel):
            return row.get("permalink")
    return None


def strip_front_matter(text):
    for fence in ("---", "+++"):
        if text.startswith(fence):
            m = re.match(r"^" + re.escape(fence) + r"\r?\n.*?\r?\n" +
                         re.escape(fence) + r"\r?\n", text, re.S)
            if m:
                return text[m.end():].lstrip("\n")
    return text


def _is_remote(u):
    return bool(re.match(r"^(https?:)?//|^data:|^mailto:", u.strip(), re.I))


def _abs_image(base, dest):
    """把相对图片 dest 变成绝对 URL；保留可能的 ` "title"` 部分。"""
    dest = dest.strip()
    parts = dest.split(None, 1)              # 拆出可选的标题
    url = parts[0]
    title = (" " + parts[1]) if len(parts) > 1 else ""
    if _is_remote(url) or url.startswith("/"):
        # 远程图原样；绝对站内路径也原样（已可访问）
        return url + title if not url.startswith("/") else base.rstrip("/") + url + title
    url = url.lstrip("./")
    # 规范化百分号编码（先解码再编码，避免对已编码的 %20 双重编码）
    enc = urllib.parse.quote(urllib.parse.unquote(url), safe="/-_.~")
    return base + enc + title


def rewrite_images(text, base):
    if not base.endswith("/"):
        base += "/"
    # markdown: ![alt](dest)
    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)",
                  lambda m: "![%s](%s)" % (m.group(1), _abs_image(base, m.group(2))),
                  text)
    # 裸 <img src="...">
    def img_repl(m):
        src = m.group(1)
        if _is_remote(src):
            return m.group(0)
        newsrc = _abs_image(base, src).split(" ")[0]
        return m.group(0).replace(src, newsrc, 1)
    text = re.sub(r'(?i)<img[^>]*?src=["\']([^"\']+)["\']', img_repl, text)
    return text


def main():
    if len(sys.argv) < 2:
        sys.exit("用法: pnpm wechat <文章 index.md 路径或 slug 关键字>")
    md = find_md(sys.argv[1])
    if not md:
        sys.exit("找不到文章: %s" % sys.argv[1])
    base = permalink_for(md)
    if not base:
        sys.exit("无法解析文章 URL（hugo list all 未匹配到 %s）。先确认它不是 draft。"
                 % os.path.relpath(md, ROOT))
    body = rewrite_images(strip_front_matter(open(md, encoding="utf-8").read()), base)

    outdir = os.path.join(ROOT, "dist", "wechat")
    os.makedirs(outdir, exist_ok=True)
    slug = os.path.basename(os.path.dirname(md)) if os.path.basename(md) == "index.md" \
        else os.path.splitext(os.path.basename(md))[0]
    outfile = os.path.join(outdir, slug + ".md")
    with open(outfile, "w", encoding="utf-8") as f:
        f.write(body)

    # 提示信息走 stderr，正文走 stdout（方便 `pnpm wechat xxx | pbcopy`）
    print("✓ 已生成: %s" % os.path.relpath(outfile, ROOT), file=sys.stderr)
    print("  文章 URL: %s" % base, file=sys.stderr)
    print("  下一步: 复制内容 → 粘进 https://doocs.github.io/md/ → 选主题 → 复制到公众号后台",
          file=sys.stderr)
    print("  (macOS 可直接: pnpm wechat %s | pbcopy)" % sys.argv[1], file=sys.stderr)
    sys.stdout.write(body)


if __name__ == "__main__":
    main()
