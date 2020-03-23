---
title: '获取Chrome浏览器'
tags:
  - Chrome
  - Google
categories:
  - Tool
date: 2017-01-18 14:50:00
---
## 由来

项目的测试需求，需要针对64位 Chrome 42+的各个`稳定版`本进行测试,但安装环境又无法`直接访问外网`进行`在线版本`安装，因此需要搜集已发布的`离线安装`版本。作为`安装源`。

> 首先，来认识下Chrome到底有哪些版本。

## [Chrome](www.google.com/chrome) VS [Chromium](www.chromium.org)

### 区别

> The Chromium projects include Chromium and Chromium OS, the open-source projects behind the Google Chrome browser and Google Chrome OS, respectively. This site houses the documentation and code related to the Chromium projects and is intended for developers interested in learning about and contributing to the open-source projects.

简而言之，Chrome是基于 **开源项目** Chromium的 。新功能会优先在Chromium发布。

<!--more-->

### 支持操作系统

- 均支持 **Windows32、Windows64、Mac、Linux、Android、IOS**
- [Chrome各版本下载地址](https://www.google.com/chrome/browser/desktop/index.html)，历史版本下载：[https://www.slimjet.com/chrome/google-chrome-old-version.php](https://www.slimjet.com/chrome/google-chrome-old-version.php)
- [Chromium各版本下载地址](https://www.chromium.org/getting-involved/dev-channel)

> 以下针对可以获取不同的维度，进行分类整理：官方的变更记录、下载地址、Wiki的ChangeList汇总

## 官方的变更记录

#### [https://chromereleases.googleblog.com/](https://chromereleases.googleblog.com/)

#### 内容涉及

- 官网用于发布每个版本的变更BLOG
- 包括 **Dev版本、Beta版本、稳定版本**
- 包括 **Android版本、IOS版本及PC版本**
- 每个版本，下面都会有`部分`用户的使用反馈，可以查看到其他用户对每个版本的使用反馈.
- 官方现在不提供历史版本的下载地址，需要自行收集各版本的下载地址

## 下载地址

#### [http://www.chrome64bit.com/](http://www.chrome64bit.com/)

##### 内容涉及

- 针对64位的各个不同OS的离线安装包
- 包括 **Linux、Mac、Windows、Portable版**
- 以及每个版本的 **32位与64位** 的区别
- [Windows下载列表](http://www.chrome64bit.com/index.php/chromium-64-bit-for-windows)
- [Mac下载列表](http://www.chrome64bit.com/index.php/google-chrome-64-bit-for-mac)
- [Linux下载列表](http://www.chrome64bit.com/index.php/google-chrome-64-bit-for-linux)
- [Portable下载列有](http://www.chrome64bit.com/index.php/chrome-64-bit-portable)

#### [http://google-chrome.en.uptodown.com/windows/old](http://google-chrome.en.uptodown.com/windows/old)

#### 内容涉及

- 32位及64位的针对Windows中的各个Chrome版本，版本总量相对比较`全`
- 下载速度很`慢`，会出现`其它语言包`的安装包，但不影响使用

## Wiki的ChangeList汇总

#### [https://en.wikipedia.org/wiki/Google_Chrome_version_history](https://en.wikipedia.org/wiki/Google_Chrome_version_history)

#### 内容涉及
- 主版本号
- 发布时间
- Layout引擎版本
- V8引擎版本
- 官方变更说明

> Wiki的数据来源是Google的官方网站，仅将每个版本的内容进行汇总。


## Summary
- 本文主要针对需要下载Windows64位各个离线版本的Chrome，进行汇总
- 从搜集内容的过程中，可以看出：Chrome的各个版本的变更内容，也`不是`特别详细。
- [https://chromereleases.googleblog.com/](https://chromereleases.googleblog.com/)中会有用户进行使用反馈，但`每少`看到`官方人员`给予回复
- Chrome官方更建议用户使用最新版本，不提供`历史版本`的下载地址

## 参考

- [http://www.howtogeek.com/202825/what%E2%80%99s-the-difference-between-chromium-and-chrome/](http://www.howtogeek.com/202825/what%E2%80%99s-the-difference-between-chromium-and-chrome/)
- [http://www.diffen.com/difference/Chromium_vs_Google_Chrome](http://www.diffen.com/difference/Chromium_vs_Google_Chrome)
- [https://www.chromium.org/](https://www.chromium.org/)
- [https://en.wikipedia.org/wiki/Google_Chrome_version_history#cite_note-Chrome_50-116](https://en.wikipedia.org/wiki/Google_Chrome_version_history#cite_note-Chrome_50-116)
