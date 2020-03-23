---
title: 'MarkDown保存至印象笔记'
tags:
  - Evernote
  - MarkDown
categories:
  - Tool
date: 2017-10-15 14:30:00
---

```
通过 Sumlime Text3 来实现将 MarkDown 文件完美保存至 印象笔记中。
```

# Step1: 安装Evernote包

- 打开 Sumlime Text3
- `cmd + shift + p`打开command pattern
- 输入`Package Controll: Install Package`，回车
- 输入Evernote，等待安装成功。Evernote包地址：[https://packagecontrol.io/packages/Evernote](https://packagecontrol.io/packages/Evernote)
- 安装结束后，在`Package Setting`中会有`Evernote`
- `cmd + shift + p`打开command pattern，输入Evernote，查看是否有Evernote对应的功能列表显示

# Step2: 获取印象笔记的Developer Token

- 登录[https://app.yinxiang.com/api/DeveloperToken.action](https://app.yinxiang.com/api/DeveloperToken.action)
- 如果没有内容，选择新增一个developer token

# Step3: 配制Sublime Text中的 Evernote

- `Package Settings` --> `Evernote` --> `Settings User`
- 默认打开内容为空，设置内容如下(Step2中获取的内容)

```json
{
	"token": "Token内容，那一串长的字符",
	"noteStoreUrl": "StoreUrl"
}
```

至此，已经配制`完成`。

<!--more-->

## 通过Sublime Text新增内容至印象笔记

- 方法1
	- 在MarkDown文件头中添加

```json
---
title: 
notebook: 
tags: 
---
```

	- `cmd + shift + p`，输入`Evernote: Send to Evernote as a new note`
	
- 方法2
	- `cmd + shift + p`，输入`Evernote: Send to Evernote as a new note`
	- 在`Sublime Text`底部会出现`Title`/`Tags`，输入完成后，会直接保存至印象笔记中



