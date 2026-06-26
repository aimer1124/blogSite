# 后续维护建议

## 1. 写作流程模板
```bash
# 新分支
git checkout -b post/slug
hugo new posts/slug/index.md
# 编辑 & 预览（使用 pnpm 脚本）
pnpm dev
# 提交
git add content/posts/slug
git commit -m "post: 添加 <标题>"
# 推送 & 合并
```

## 2. 主题更新节奏（带兼容校验的“故意锁定”）
主题以 git 子模块形式按**精确 commit SHA** 锁定（这本身就保证了构建可复现）。
当前锁定：`themes/PaperMod` = `v8.0-48-g6e10fae`（master 上 v8.0 之后第 48 个提交）。

> ⚠️ 重要：PaperMod 最后一个正式 release `v8.0` **无法在本仓库 CI 的 Hugo 0.151.0 下构建**
> （报错 `partial "partials/templates/_funcs/get-page-images" not found`）。
> 当前锁定的 master 提交才与 Hugo 0.151.0 兼容、构建零告警。
> 所以**不要因为“用 release 更稳”而回退到 v8.0**——升级/降级主题前务必本地用同款 Hugo 验证。

更新流程（每季度或有需要时，故意而非自动）：
```bash
(cd themes/PaperMod && git fetch && git checkout <目标 commit 或 tag>)
pnpm build           # 必须用 CI 同款 Hugo（pnpm 已锁 hugo-extended@0.151.0）
# 构建零 error / 关注 deprecation WARN，OK 再提交子模块引用
git add themes/PaperMod && git commit -m "chore(theme): bump PaperMod to <ref>"
```
若主题与 Hugo 版本要一起升，先在分支里同时改 `package.json` 的 `hugo-extended` 与
`.github/workflows/gh-pages.yml` 的 `hugo-version`，本地验证通过再合并。

## 3. 访问统计/性能
- 可接入 Cloudflare 免费加速（含 HTTPS 证书 & 缓存）
- 若使用 Cloudflare：Pages 自签 HTTPS 与 CF 共存正常（注意开启“始终使用 HTTPS”）

## 4. 自动化扩展想法
| 方向 | 描述 |
|------|------|
| 链接检查 | 定期 Action 运行 `lychee` 检测死链 |
| ~~图像优化~~ | ✅ 已实现：构建期转 WebP（见第 11 节）。AVIF 可后续再加 |
| TOC 优化 | 针对中文标题生成锚点 slugify 规则自定义 |
| SEO | 增加 JSON-LD（文章、BreadcrumbList） |
| 备份 | 每月 Action 打包 zip 上传到 Release Draft |

## 5. 备份策略
```bash
git bundle create backup-`date +%Y%m`.bundle master
```
存放到本地硬盘/网盘。

## 6. 监控与错误
- 访问激增：查看 GitHub Pages 状态 或 加 Cloudflare 分析
- 评论异常：检查 Utterances OAuth 安装、GitHub API 速率限制

## 7. 升级 Hugo
```bash
# 查看当前版本
hugo version
# 修改 `.github/workflows/gh-pages.yml` 中 `hugo-version` 字段
```
升级后重点检查：
- 语法弃用 (WARN)
- 生成速度变化

## 8. 本地主题二次开发
放置自定义样式：`assets/css/extended/xxx.css`
```bash
assets/css/extended/custom.css  # Hugo 会自动打包
```
放置自定义 JS：`assets/js/extended/custom.js`

## 9. 数据驱动内容
若需要如“GR记录”自动聚合：
- 可在 `data/` 目录放置 YAML/JSON/TOML
- 在自定义模板中 `{{ site.Data.xxx }}` 渲染

## 10. 安全
- 开启仓库 Settings -> Branch protection (最少 1 Review 可选)
- 避免在公开仓库存放未授权图片/受版权限制内容

## 11. 图片 WebP 优化（构建期，已实现）
钩子：`layouts/_default/_markup/render-image.html`（覆盖 PaperMod 默认 render-image）。
- **作用范围**：仅 Markdown 图片语法 `![alt](xxx.png)`，且引用的是**本篇 page-bundle 内**的 jpeg/png。
  这类图会被转成**同尺寸 WebP**，输出 `<picture><source ...webp><img ...原图></picture>`。
- **原样放行（不转码、不阻断构建）**：外链图（http/https）、gif（保留动画）、未匹配到的引用。
- **依赖 Hugo Extended**（WebP 编码）。CI 已 `extended: true`；本地 `pnpm` 装的也是 extended，无需额外操作。
- **配套 CSS**：`assets/css/extended/custom.css` 里 `.post-content picture{display:block}`，
  让 `<picture>` 包裹后仍保持图片的居中/限宽。删钩子时这条也可一并删。
- **构建缓存**：WebP 生成物在 `resources/_gen/`（已 gitignore），CI 每次重建，无需提交。

> ⚠️ 写作约定：插图请用 **Markdown 语法** `![](图片.png)`，**不要**用裸 `<img src="图片.png">`。
> 裸 HTML `<img>` 引用 bundle 内图片时，Hugo 不会把该图发布到 `public/` → **线上 404**，
> 且不经过本钩子、拿不到 WebP。（外链图用裸 `<img>` 没问题。）

---
保持“少即是多”：仅在确有价值时增加新功能，保证写作体验优先。
