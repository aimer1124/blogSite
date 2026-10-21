---
title: "Video Publisher — DailyVideo"
description: "运行在个人 Mac 上的视频日记整理与 YouTube 私密上传工具。"
url: "/dailyvideo/"
type: "page"
hideMeta: true
hideSummary: true
hiddenInHomeList: true
searchHidden: true
ShowPostNavLinks: false
ShowShareButtons: false
ShowToc: false
comments: false
---

**Video Publisher 的 DailyVideo 模块，是 Yuanjie 自用的视频日记工具。** 它在个人 Mac 上整理视频，生成字幕、封面、标题和标签，并在获得频道所有者授权后，将成片及发布文案上传至指定 YouTube 频道。

## 当前功能

- 从指定 Google Drive 文件夹接收素材，在 Mac 上完成剪辑和字幕处理。
- 根据字幕检索参考资料，制作并插入相关图片及来源说明。
- 将成片、竖版封面和发布文案同步回 Google Drive。
- 使用 YouTube API Services 上传视频及标题、描述、标签，查询频道身份和上传处理状态，并在频道具备权限时设置封面。
- 将处理完成或失败的通知发送至所有者指定的邮箱。

**当前后续新视频自动公开上传。** 所有者已于 2026 年 10 月 21 日明确授权这一规则；上传包含标题、内容简介、录制日期、5 个标签及已有来源链接。公众可以在 YouTube 上观看已公开的视频及其发布信息。此前完成的私密测试视频保持原状态；手动测试仍默认私密。网站本身不托管视频。目前仅供所有者个人使用，不提供公众注册、在线上传或账号授权入口。

## 授权与数据

YouTube 模块使用 Google 官方授权页面，不接收 Google 密码。请求的权限为上传视频，以及读取频道和视频状态。授权凭据保存在个人 Mac 上，不写入本网站或公开代码仓库。

完整流程还使用 Google Drive、邮件服务，以及经所有者同意接收字幕文本的 OpenAI/Codex 资料检索服务。原始视频不会发送给该字幕检索模块；YouTube 上传的成片则会提交给 Google。

请阅读 **[DailyVideo 隐私政策](/dailyvideo/privacy/)**，了解数据访问、用途、存储、撤销授权和删除方式。

## 使用说明与联系

使用 YouTube 功能须遵守 [YouTube 服务条款](https://www.youtube.com/t/terms)；使用该功能即表示同意受其约束。YouTube 的数据处理同时适用 [Google 隐私政策](https://policies.google.com/privacy)。

开发与维护：Yuanjie（个人工具）  
联系：[jacksonshi1985@gmail.com](mailto:jacksonshi1985@gmail.com)

更新日期：2026 年 10 月 21 日
