---
title: 'API开发神器-Postman'
tags:
  - API测试
  - Chrome
  - Testing
  - Node.js
  - CI
categories:
  - Tool
date: 2016-06-24 19:50:00
---

`Postman helps you develop APIs faster.`

# 豪华午餐

![Postman](/img/Postman.png)

## Postman
`构建、管理、文档化`API
* 在线安装
 * Chrome插件版
[https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop)
 * MAC版
[https://www.getpostman.com/app/postman-osx](https://www.getpostman.com/app/postman-osx)
* 离线安装
  使用已经安装好的Postman文件夹，`机器`默认存放目录：/Library/Application\ Support/Google/Chrome/Default/Extensions
   进入`chrome://extensions/`，选择`Load unpacked extensions`，加载Postman的文件夹

![Newman(我真的不是MP3)](/img/Postman-Newman.png)

<!--more-->

## Newman

Newman is a command-line collection runner for[Postman](http://getpostman.com/). It allows you to effortlessly run and test a Postman collection directly from the command-line. It is built with extensibility in mind so that you can easily integrate it with your continuous integration servers and build systems.
* 安装： `newman`:`npm install -g newman`
* 功能： 直接运行Postman的接口[Collection](http://www.getpostman.com/docs/collections)数据(**本地或远程**)
* 运行： **本地**Postman保存的Collection内容

```
➜  Downloads newman -c Demo.postman_collection.json

Iteration 1 of 1
200 1479ms Open the url of Baidu. [GET] http://www.baidu.com
    ✔ Status code is 200

Summary:

Parent                   	Pass Count	 FailCount
-------------------------------------------------------------
Collection Demo          	         1	         0

Total                    	         1	         0
```
* 运行**远程**Postman

```
➜  ~ newman -u https://www.getpostman.com/collections/676a42223e14bf54ad84

Iteration 1 of 1
200 240ms Open the url of Baidu. [GET] http://www.baidu.com
    ✔ Status code is 200

Summary:

Parent                   	Pass Count	 FailCount
-------------------------------------------------------------
Collection Demo          	         1	         0

Total                    	         1	         0
```

![Interceptor](/img/Postman-Interceptor.png)
## Interceptor
Postman interceptor brings the power of your Chrome window to Postman! You can set custom headers (including cookies) from within Postman, and view cookies already set on the domain. You can also capture requests being sent from Chrome and import them into Postman. This makes building APIs a breeze!
* 安装
[https://chrome.google.com/webstore/detail/postman-interceptor/aicmkgpgakddgnaphhhpliifpcfhicfo/](https://chrome.google.com/webstore/detail/postman-interceptor/aicmkgpgakddgnaphhhpliifpcfhicfo/)
* 功能
 * 记录浏览器请求并直接导入到Postman
 * 可添加`Filter`，对浏览器中的请求进行过滤

# 初级使用
## 录制API-`Interceptor`
* 设置浏览器中的`Interceptor`：打开`开关`、设置`Filter`（仅过滤`www.jianshu.com`）

![Chrome中设置Interceptor](/img/Postman-Chrome-Interceptor-Setting.png)

* 设置`Postman`中的`Interceptor`：打开`开关`

![Postmsn中打开Interceptor](/img/Postman-Interceptor-Setting.png)

* 开始`录制`：在`Chrome`浏览器中输入[http://www.jianshu.com/p/4a677c5f79f1](http://www.jianshu.com/p/4a677c5f79f1)，回车后，查看`Postman`的请求录入

![录制API结果](/img/Postman-Record.png)

## 回放API-`Postman`
* 选择`Postman`中的API:`Get http://www.jianshu.com/p/4a677c5f79f1`

![指定API](/img/Postman-Replay.png)

* 点击`Send`，进行`回放`。可查看到请求的返回状态码`200`、数据`Body`
![回放结果](/img/Postman-Replay-Result.png)

## 指定API请求-`Postman`
* 在`URL`输入框中，输入`目标地址`:[http://www.jianshu.com/p/4a677c5f79f1](http://www.jianshu.com/p/4a677c5f79f1)。点击`Send`按钮

![1步搞定指定API请求](/img/Postman-Your-API.png)

# 高级使用
## 规划管理API-`Postman`+`Collection`
将所有的API进行分类管理，如按**模块、系统、类型**。

### 保存API至`Collection`
 * 选中需要保存的API，点击请求列表中的`Save to collection`

![Save to collection](/img/Postman-Save-to-Collection.png)
 * 可将此API保存至`已有的Collection`或`新增Collection`

### 重命令API请求-便于**管理和查看**
 * 切换到`Collections`列表，点击API请求的操作区，选择`Edit`
![Edit-API信息](/img/Postman-Edit-Collection.png)

## 常用权限应用尽有-`Authorization`

![Authorization设置](/img/Postman-Auth.png)

* Postman在请求时，可指定`此次`请求**Auth**方式
* 可设置**Auth**中的具体内容，完全自行`定义`。如设置`Basic Auth`中的**用户名和密码**

![Basic Auth](/img/Postman-Auth-Basic.png)

## 完全自定义的头-`header`

![Header设置](/img/Postman-Header.png)

*  编辑已有Header中的元素
* 新增Header中请求时，需要的**Key:Value**
* 禁用及启用Header中的元素，对于不清楚API请求时，具体哪些是`必须`要传递的比较有用

## 完美的数据体-`body`

![Body设置](/img/Postman-Body.png)

* 在请求需要发送数据体时，可通过设置`body`内容
* 支持form-data/x-www-urlencoded/raw/binary，格式的数据

## 请求前还能做点事-`Pre-request Script`

![Pre-request Script设置](/img/Postman-Pre-Request.png)
* 请求发送前，可进行一些脚本设置。如：设置或清除参数、变量

## 验证API请求结果-`Tests`
`Postman`提供了常用的测试功能：返回内容处理、状态码判断、请求超时等。点击后`自动`添加到Test脚本中
![Test命令集合](/img/Postman-Verify-Response.png)

# 进阶使用
## 带你快速走向各个环境-`Environment`
* 添加`QA环境`的`URL`地址变量

![添加QA环境的地址变量](/img/Postman-Environment.png)

* 添加`DEV`环境的`URL`地址变量。此时就有两个环境地址

![QA、DEV，两个环境](/img/Postman-Environment-AllEnv.png)

* 修改请求中的`URL`地址为：`{{URL}}p/4a677c5f79f1`，切换环境至`QA环境`

![变更URL、切换环境](/img/Postman-Environment-Change.png)

* 点击`Send`，请求`QA环境`中的数据

![真实的请求QA环境](/img/Postman-Environment-Test.png)

**使用Evnironment，可设置环境地址及环境中的不同数据，便于在跨环境后， 相同API可快速使用，减少调整API的成本**

## 分享你的成果-`导出/导入` or `share`
### 导出-`Download`
* Postman中有`Download`功能（即`导出`功能），且`Download`后的可直接`导入`
* 可将`Collection`、`Environment`的数据进行`Download`
PS：导出的数据其实是`JSON数据格式`，可**随意**玩

### 导入-`Import`
* 导入`所有导出`的数据
* 被导入的数据格式与内容与导出时，**完全一致**。

### 分享-`share`
* `share`功能需要登录后，才能使用。且shared成功后，对应的链接会保存到用户数据中

![share-link](/img/Postman-Share.png)

* 点击链接，会直接打开share的API设置内容

**导出/导入、share，便于在团队内部协作时使用，API的请求及管理团队化**
## 海量执行你的请求-`Runner`
当你有`大量`的API时，肯定想`一次执行多个`、`多次执行多个`，Postman的`Runner`可以满足你的需求。
* 调整API的结构、添加必要的`测试验证`

![添加验证](/img/Postman-Add-Test.png)

* 打开`Runner`，设置执行`参数`：选择要执行的`Collection`、执行多少次`Interation`、请求的延迟`Delay`、数据文件、变量控件

![执行参数](/img/Postman-Add-Testing-Parameters.png)

* `Start Test`查看运行结果`RESULTS`

![Results](/img/Postman-Add-Test-Results.png)

## CI挂起来-`Newman`
直接使用`Newman`命令，快速把Postman与CI集成起来(直接使用shell命令，即可)。

```
newman -c demo.postman_collection --exitCode 1
```


----

PS:

* 从**3.2.0**版本之后，将原来的Jetpack(Runner/Newman)功能免费，以上所提到的功能`全部免费`使用
* 本文使用版本为**4.2.2**

# 参考
* Postman官网
[http://getpostman.com/](http://getpostman.com/)
* Newman
[https://www.npmjs.com/package/newman](https://www.npmjs.com/package/newman)
* Postman Collection
[http://www.getpostman.com/docs/collections](http://www.getpostman.com/docs/collections)
* Postman Environment
[https://www.getpostman.com/docs/test_multi_environments](https://www.getpostman.com/docs/test_multi_environments)
* How to write powerful automated API tests with Postman, Newman and Jenkins
[http://blog.getpostman.com/2015/09/03/how-to-write-powerful-automated-api-tests-with-postman-newman-and-jenkins/](http://blog.getpostman.com/2015/09/03/how-to-write-powerful-automated-api-tests-with-postman-newman-and-jenkins/)
