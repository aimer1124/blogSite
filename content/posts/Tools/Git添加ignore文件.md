---
title: 'Git添加ignore文件'
tags:
 - Git
categories:
 - Tool
date: 2016-03-08 20:57:00
---

# Git Ignore

`忽略特殊指定的文件`

`gitignore - Specifies intentionally untracked files to ignore`

# 操作

## 全局忽略

* 直接使用命令`git config --global core.excludesfile ~/.gitignore_global`
<!-- more -->
## 未添加到仓库的文件

* 直接在仓库根目录创建`.gitignore`文件
* 在文件中配制所需要`ignore`的文件清单
* 还原的话，直接在`.gitignore`中删除对应的`配制行`即可

## 已提交到仓库的文件

* 先更新仓库至最新版本
* 添加指定指定的忽略文件`git update-index --assume-unchanged Gruntfile.js`，此处忽略`Gruntfile.js`文件
* 还原的话，使用命令`git update-index --no-assume-unchanged Gruntfile.js`，重新添加对`Gruntfile.js`文件的追踪


## 建议

* `Github`官方提供的常用各种`ignore`文件大全，[https://github.com/github/gitignore](https://github.com/github/gitignore)
* 将`.gitignore`文件提交到远程仓库中，便于整个项目的管理
* `.gitignore`添加文件的原则
 * 临时生成的文件
 * 本地调度需要经常变更的文件
 * 日志文件
 * 编译生成的中间文件，如`Java`的`.class`文件

## 参考

* Git之ignore文件: [http://www.douban.com/note/476292319/?type=like](http://www.douban.com/note/476292319/?type=like)
* Git官方推荐`ignore`内容：[https://github.com/github/gitignore](https://github.com/github/gitignore)
* Git官方配制`ignore`方法：[http://git-scm.com/docs/gitignore](http://git-scm.com/docs/gitignore)
