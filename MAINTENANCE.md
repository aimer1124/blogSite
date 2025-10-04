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

## 2. 主题更新节奏
- 每季度执行一次：`(cd themes/PaperMod && git pull origin master)`
- 观察 Release Note 是否有破坏性变更
- 本地 `hugo server` 验证后再提交

## 3. 访问统计/性能
- 可接入 Cloudflare 免费加速（含 HTTPS 证书 & 缓存）
- 若使用 Cloudflare：Pages 自签 HTTPS 与 CF 共存正常（注意开启“始终使用 HTTPS”）

## 4. 自动化扩展想法
| 方向 | 描述 |
|------|------|
| 链接检查 | 定期 Action 运行 `lychee` 检测死链 |
| 图像优化 | 构建阶段将大图转换为 WebP/AVIF |
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

---
保持“少即是多”：仅在确有价值时增加新功能，保证写作体验优先。
