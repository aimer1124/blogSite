---
title: "Video Publisher — DailyVideo 隐私政策"
description: "DailyVideo 个人视频处理及 YouTube 上传模块的数据处理说明。"
url: "/dailyvideo/privacy/"
type: "page"
hideMeta: true
hiddenInHomeList: true
searchHidden: true
ShowPostNavLinks: false
ShowShareButtons: false
ShowToc: true
comments: false
---

更新日期：2026 年 10 月 21 日

本政策适用于 Yuanjie 维护的 Video Publisher 中的 DailyVideo 个人视频工作流及 YouTube 上传模块。当前工具仅供所有者个人使用。[返回应用说明](/dailyvideo/)。

## 访问和处理的信息

| 信息 | 用途与处理位置 |
| --- | --- |
| 原视频、音频、字幕、参考图片、封面及成片 | 在个人 Mac 上剪辑、转写、校对和制作发布素材；指定的输入、输出文件夹通过 Google Drive 同步。 |
| 字幕文本及检索请求 | 经所有者明确同意，发送给 OpenAI/Codex，用于查找资料、核对来源与图片匹配；该检索模块不接收原始视频。 |
| YouTube 频道标识和名称 | 使用 YouTube API Services 核对目标频道，防止上传至错误频道。 |
| 成片、标题、描述、标签和封面 | 经所有者授权，通过 YouTube API Services 提交给 Google；所有者已授权后续新视频以公开状态上传，视频及标题、描述和标签可被公众查看；此前完成的私密测试保持原状态，手动测试仍默认私密。封面设置受频道权限限制。 |
| YouTube 视频标识、链接、隐私状态、处理状态和错误信息 | 在 Mac 上确认上传结果、重试任务、防止重复上传并生成通知。 |
| OAuth 授权凭据和上传会话信息 | 在 Mac 上完成获准的后台上传与状态查询。凭据保存在受本机文件权限保护的目录，不写入公开网站或公开仓库。 |
| 指定收件邮箱、任务状态及结果链接 | 通过邮件服务向所有者发送完成或失败通知。 |

YouTube 模块请求 `youtube.upload` 与 `youtube.readonly` 权限，用于上述上传、频道核对及状态查询。Google 密码由 Google 官方页面处理，DailyVideo 不索取或保存密码。

## 数据共享与用途限制

数据仅在完成上述功能所需的范围内，提交给 Google Drive、YouTube、邮件服务和经同意的 OpenAI/Codex 服务。公共资料检索还会访问第三方来源网站；访问行为受各来源的政策约束。工具不将私人视频放在此公开网站上。

本工具不出售用户数据，不将 Google 用户数据用于广告定位，也不将其用于训练通用人工智能或机器学习模型。第三方服务如何处理其接收的数据，以其适用条款、隐私政策与所用账号设置为准。本政策不承诺第三方服务具有本工具无法控制的保留或删除行为。

DailyVideo 对从 Google API 获得的信息的使用和向其他应用的传输，将遵守 [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy)，包括其中的 Limited Use 要求。

## 存储与安全

素材、工作缓存、任务记录、处理日志及授权文件保存在所有者的 Mac 上；指定素材和输出也存储于 Google Drive，已上传的视频保存在 YouTube。当前本地任务记录与缓存没有统一的自动清理期限，由所有者管理和清理。不能将删除本地文件理解为第三方服务副本已同时删除。

本机授权文件使用受限文件权限，服务通信使用 HTTPS。授权凭据不会嵌入视频、封面、邮件正文或公开网页。设备所有者仍需保护本机账号和备份。

## 停止使用、撤销授权与删除

1. 在 [Google 账号的第三方连接设置](https://myaccount.google.com/connections) 中找到对应的 Video Publisher 应用并撤销授权，可以阻止后续使用该 Google 授权。仅删除本机授权文件不等同于向 Google 撤销授权。
2. 停用 Mac 上的 DailyVideo 上传与处理后台任务，避免继续处理新素材。需要帮助时可联系下方邮箱。
3. 删除 Mac 上的授权文件、上传任务记录、缓存及不再需要的素材；删除时也应检查自行建立的备份。
4. 在 Google Drive 中删除不再需要的输入、输出文件，并按需要清空回收站；在 YouTube Studio 中另行删除已上传视频。撤销授权、停用工具或删除本地文件，都不会自动删除这些云端内容。

当前为个人部署，所有者可直接管理本机和云端数据。如对工具保存的数据需要查询或删除协助，请通过下方邮箱联系维护者。

## 本网站的访问数据

本说明页托管于 GitHub Pages，沿用博客现有的 Cloudflare Web Analytics 配置。托管和统计服务可能处理访问 IP、请求信息、浏览器及页面访问数据，用于安全、运行和访问统计。页面不提供 Google 登录、视频上传或授权凭据提交表单。

有关网站服务，请参阅 [GitHub 隐私声明](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement) 和 [Cloudflare 隐私政策](https://www.cloudflare.com/privacypolicy/)。

## 第三方条款与联系

本工具使用 YouTube API Services。请参阅 [YouTube 服务条款](https://www.youtube.com/t/terms)、[Google 隐私政策](https://policies.google.com/privacy) 和 [OpenAI 隐私政策](https://openai.com/policies/privacy-policy/)。

维护者：Yuanjie  
联系：[jacksonshi1985@gmail.com](mailto:jacksonshi1985@gmail.com)

本政策会随实际功能和数据处理方式更新，并在本页标明更新日期。
