---
title: 'SuperTestWithGulp'
tags:
  - SuperTest
  - Gulp
  - API测试
  - Testing
categories:
  - Tool
date: 2016-04-15 15:51:00
---

# Gulp

 Automate and enhance your workflow

`用自动化构建工具增强你的工作流程！`

* 官网：[http://gulpjs.com/](http://gulpjs.com/)
* 中文官网：[http://www.gulpjs.com.cn/](http://www.gulpjs.com.cn/)
* 简体中文文档: [https://github.com/lisposter/gulp-docs-zh-cn](https://github.com/lisposter/gulp-docs-zh-cn)
* 安装`npm install --global gulp`
* 验证

```
➜  Downloads gulp -v
[15:59:38] CLI version 3.9.1
[15:59:38] Local version 3.9.1

```

<!--more-->



# SuperTest

[API测试](http://aimer1124.github.io/2016/01/17/Tool-SuperTest/)

# SuperTestWithGulp
Use [Gulp](http://gulpjs.com/) to run [SuperTest](https://github.com/visionmedia/supertest) API testing scripts

## 准备

* 仅需要`clone`这个[repo demo](https://github.com/aimer1124/SuperTestWithGulp.git),就可以了.

## 运行

* 使用命令`gulp master`,查看结果:

```
[15:28:55] Using gulpfile ~/Downloads/SuperTestWithGulp/gulpfile.js
[15:28:55] Starting 'master'...
[15:28:55] Finished 'master' after 24 ms
You are in master


  Test Demo.
    ✓ Visit http://aimer1124.github.io/ (775ms)


  1 passing (779ms)

```
* 使用命令`gulp branch`,可以查看到 `branch` 环境的运行结果:

```
[15:30:34] Using gulpfile ~/Downloads/SuperTestWithGulp/gulpfile.js
[15:30:34] Starting 'branch'...
[15:30:34] Finished 'branch' after 22 ms
You are in branch


  Test Demo.
    ✓ Visit http://aimer1124.github.io/2016/01/17/Tool-SuperTest/ (780ms)


  1 passing (784ms)

```
## 增强

* Modify the visit url,you just need to modify the `url` property in `master.js` or `branch.js`
* Add more environment,you just need to `three` steps:
 * add the gulp task in `gulpfile.js` like this

	```
	gulp.task('newBranch', function() {
		require('./config/endpoints')('newBranch');
		runTest();
	});

	```

 * add the host config in `endpoints.js`

	```
	...
	var host = {
	    master: require('./master.js'),
	    branch: require('./branch.js'),
	    newBranch: require('./newBranch.js')
	};
	...
	```

 * add one javascript file named `newBranch` under `config` folder,and config this file like others
