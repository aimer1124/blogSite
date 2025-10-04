# 个人博客站点 (Hugo + PaperMod)

使用 [Hugo](https://gohugo.io/) 与现代主题 [PaperMod](https://github.com/adityatelange/hugo-PaperMod) 构建，自动部署到 GitHub Pages，并绑定自定义域名 `shiyuanjie.cn`。所有使用的服务与资源均为免费方案。

## 功能概览
- 主题：PaperMod（自适应浅/深色、目录、代码复制按钮、阅读时长）
- 评论：Utterances (GitHub Issues)
- 访问统计：不蒜子 (自定义扩展插槽, 需补充脚本)
- ICP 备案号展示
- 自定义域名 CNAME 已配置
- GitHub Actions 自动构建与发布

## 本地开发
本仓库使用 pnpm 脚本管理，不内置 hugo 二进制；请先安装 Hugo Extended。

### 1. 安装工具
```bash
corepack enable
brew install hugo   # macOS, 安装 extended 版本
```
验证：
```bash
pnpm run check:hugo
```

### 2. 克隆与初始化
```bash
git clone --recurse-submodules git@github.com:aimer1124/blogSite.git
cd blogSite
git submodule update --init --recursive
pnpm install
```

### 3. 启动预览 (默认 http://localhost:1313)
```bash
pnpm dev
```
`pnpm dev` 等价 `hugo server -D`，`-D` 会包含草稿。

## 新建文章
```bash
hugo new posts/your-folder/your-post.md
```
Front Matter 可参考：
```yaml
---
title: "文章标题"
date: 2025-10-03T10:00:00+08:00
draft: false
tags: ["跑步", "学习"]
categories: ["Blog"]
summary: "简短摘要用于列表展示"
---
```

## 部署流程（CI）
同仓库分支管理：源码在 `master`，构建产物发布到 `gh-pages` 分支（GitHub Pages）。

流程：
1. Push 到 `master`
2. Actions：Checkout (含子模块)
3. 安装 Hugo（使用 `peaceiris/actions-hugo`）
4. `hugo --minify` 生成 `public/`
5. 自动写入 `public/CNAME` -> `shiyuanjie.cn`
6. 使用 `peaceiris/actions-gh-pages` 推送到本仓库 `gh-pages` 分支

无需额外 PAT，使用默认的 `GITHUB_TOKEN` 即可。工作流文件：`.github/workflows/gh-pages.yml`。
GitHub -> Repository Settings -> Pages：Source 选择 `Deploy from a branch`，Branch 选择 `gh-pages`。

## 自定义域名 DNS 记录
在域名解析商添加：
- `A` 记录：`@` 指向 GitHub Pages IP（推荐使用 `CNAME` 到 `<username>.github.io` 更易维护）
- 或 `CNAME` 记录：`www` 指向 `aimer1124.github.io`
- 根域名 (@) 若需 301/ALIAS 支持，可使用 DNS 提供商的 ALIAS/ANAME 功能，否则加一条 A 记录指向 GitHub Pages 公共 IP：`185.199.108.153/109.153/110.153/111.153`（四条都加）

GitHub 仓库设置 -> Pages 中确保 Custom domain 填写 `shiyuanjie.cn` 并勾选 Enforce HTTPS。

## 更新主题
```bash
cd themes/PaperMod
git pull origin master
cd ../../
# 提交子模块引用更新
git add themes/PaperMod
git commit -m "chore(theme): update PaperMod"
```

若想锁定特定版本，可在子模块目录 checkout tag。

## 添加/修改导航菜单
在 `config.toml` 的 `[menu.main]` 块添加：
```toml
[[menu.main]]
  identifier = "about"
  name = "关于"
  url = "/about/"
  weight = 4
```

## 不蒜子统计脚本
在 `layouts/partials/extend_head.html` (需新建) 中插入：
```html
<script async src="//busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js"></script>
```
在想显示的位置 (如 `layouts/partials/footer.html` 扩展) 中放：
```html
<span id="busuanzi_container_site_pv">总访问量 <span id="busuanzi_value_site_pv"></span></span>
```
PaperMod 支持通过 `layouts/partials/` 下的同名文件进行覆盖。若后续我已补充将保留在仓库。

## Utterances 评论
确保在配置中：
```toml
[params.utteranc]
  enable = true
  repo = "aimer1124/comments-blog"
  issueTerm = "pathname"
  theme = "github-light"
```

## 备份 & 安全
- 主干内容即 Markdown + 主题子模块引用，Git 即备份
- 建议开启仓库保护 (branch protection) 防止误删
- 定期导出：`git bundle create blogSite.bundle master`

## 内容工作流建议
1. 建立新分支 `post/slug`
2. 写作 & 本地预览 `pnpm dev`
3. 提 PR 自审 -> Merge -> 自动部署
4. 使用标签与分类保持聚合清晰

## 免费资源说明
- 构建与托管：GitHub + GitHub Actions (免费额度足够博客使用)
- 域名：已自购；DNS 解析使用域名注册商或 Cloudflare 免费方案
- 评论：Utterances（依赖 GitHub Issues）
- 统计：不蒜子（免费）

## 后续可选增强
- 引入 Algolia / lunr.js 本地搜索
- 添加 sitemap.xml（Hugo 默认已生成）与 robots.txt（默认生成）
- 添加 RSS (Hugo 已默认 /index.xml)
- Dark Mode Logo / Favicon 定制
- 自动图像压缩（GitHub Action 调用 imagemin 或 webp）
- 定期主题更新检查 (Dependabot for submodules 尚不直接支持，可写自定义 Action)

## 常见问题
| 问题 | 解决 |
|------|------|
| 首页无文章 | 确认文章 `draft: false` 且日期不在未来 |
| 样式未生效 | 检查主题子模块是否初始化 & PaperMod 路径正确 |
| 评论不显示 | 确认公共仓库、Utterances 安装过应用、issueTerm 正确 |
| 自定义域名 404/未 HTTPS | Pages 设置里重新保存域名并等待证书签发（最长 1h） |

---
如需进一步定制（短代码、数据驱动页面、SEO 微数据），可继续在 `layouts/` 目录下添加覆盖模板。
