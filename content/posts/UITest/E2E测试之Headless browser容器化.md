---
title: 'E2E测试之Headless browser容器化'
tags:
  - E2E
  - Docker
  - Protractor
  - Testing
categories:
  - Testing
date: 2016-08-01 20:00:00
---

# 目的

- E2E测试执行过程中**不依赖UI**界面
- 可在*nix系统中运行
- 为什么不用`PhantomJS`,[Protractor官方不推荐使用`PhantomJS`来测试](http://www.protractortest.org/#/browser-setup#setting-up-phantomjs)

```
We recommend against using PhantomJS for tests with Protractor. There are many reported issues with PhantomJS crashing and behaving differently from real browsers.
```

# Docker
## 安装
- 下载系统所需要的安装包，下载地址：[https://www.docker.com/products/docker](https://www.docker.com/products/docker)
- 注册[https://hub.docker.com/](https://hub.docker.com/)账号
- 使用`pull`来获取docker 镜像`protractor-headless`，此过程会比较慢，耐心等待
docker hub地址：[https://hub.docker.com/r/webnicer/protractor-headless/](https://hub.docker.com/r/webnicer/protractor-headless/)
git hub地址：[https://github.com/jciolek/docker-protractor-headless](https://github.com/jciolek/docker-protractor-headless)

```
docker pull webnicer/protractor-headless
```

<!--more-->


# E2E之Protractor

## 可视化运行E2E测试

- 安装`Protractor`

```
npm install -g protractor
```
- 更新`webdriver-manager`

```
webdriver-manager update
```

- 创建`conf.js`配制文件

```
// conf.js
exports.config = {
  framework: 'jasmine',
  seleniumAddress: 'http://127.0.0.1:4444/wd/hub',
  specs: ['**/**.js'],
  capabilities: {
    browserName: 'chrome'
  },
  jasmineNodeOpts: {
    showColors: true,
  }
};
```

- 创建`test-spec.js`测试脚本

```
describe('angularjs homepage todo list', function() {
  it('should add a todo', function() {
    browser.get('https://angularjs.org');

    element(by.model('todoList.todoText')).sendKeys('write first protractor test');
    element(by.css('[value="add"]')).click();

    var todoList = element.all(by.repeater('todo in todoList.todos'));
    expect(todoList.count()).toEqual(3);
    expect(todoList.get(2).getText()).toEqual('write first protractor test');

    // You wrote your first test, cross it off the list
    todoList.get(2).element(by.css('input')).click();
    var completedAmount = element.all(by.css('.done-true'));
    expect(completedAmount.count()).toEqual(2);
  });
});
```

- 运行`E2E测试`: `protractor conf.js`，会**启动chrome浏览器**，并在控制台显示对应的执行结果

```
➜  protractorHeadless git:(master) ✗ protractor conf.js
[17:23:41] I/hosted - Using the selenium server at http://127.0.0.1:4444/wd/hub
[17:23:41] I/launcher - Running 1 instances of WebDriver
Started
.


1 spec, 0 failures
Finished in 19.912 seconds
[17:24:01] I/launcher - 0 instance(s) of WebDriver still running
[17:24:01] I/launcher - chrome #01 passed
```

- E2E的可视化测试完成

## Headless运行E2E测试
- 将下面内容保存为可执行程序，shell文件(unix)或bat文件(windows)

```
#!/bin/bashdocker run -it --privileged --rm --net=host -v /dev/shm:/dev/shm -v $(pwd):/protractor webnicer/protractor-headless $@
```

- 进入控制台，输入`protractor.sh --version`，查看版本号，以确定配制成功。**务必要启动docker服务**

- 修改`conf.js`文件内容，启用docker镜像内部的`selenium server`

```
// conf.js
exports.config = {
  framework: 'jasmine',
//  seleniumAddress: 'http://127.0.0.1:4444/wd/hub',
  specs: ['**/**.js'],
  capabilities: {
    browserName: 'chrome'
  },
  jasmineNodeOpts: {
    showColors: true,
  }
};
```

- 进入`protractor`的脚本根目录，执行`protractor.sh conf.js`,**不会启动chrome浏览器**，且在控制台显示对应的执行结果

```
➜  protractorHeadless git:(master) ✗ protractor.sh conf.js
[09:31:08] I/local - Starting selenium standalone server...
[09:31:08] I/launcher - Running 1 instances of WebDriver
[09:31:09] I/local - Selenium standalone server started at http://192.168.65.2:37226/wd/hub
Started
.


1 spec, 0 failures
Finished in 11.403 seconds
[09:31:23] I/local - Shutting down selenium standalone server.
[09:31:23] I/launcher - 0 instance(s) of WebDriver still running
[09:31:23] I/launcher - chrome #01 passed
```

- E2E的Headless测试完成

# 详解

## Dockerfile文件

```
FROM node:slim
MAINTAINER Yuanjie
WORKDIR /tmp
RUN npm install -g protractor mocha jasmine && \
    webdriver-manager update && \
    apt-get update && \
    apt-get install -y xvfb wget openjdk-7-jre && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    dpkg --unpack google-chrome-stable_current_amd64.deb && \
    apt-get install -f -y && \
    apt-get clean && \
    rm google-chrome-stable_current_amd64.deb && \
    mkdir /protractor
ADD protractor.sh /protractor.sh
# Fix for the issue with Selenium, as described here:
# https://github.com/SeleniumHQ/docker-selenium/issues/87
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null
WORKDIR /protractor
ENTRYPOINT ["/protractor.sh"]
```

镜像主要配制说明
- 获取基准镜像: `node:slim`
- 安装`protractor,mocha,jasmine`: E2E测试执行所需
- 更新driver: `webdriver-manager update`
- 安装Xvfb：apt-get install -y xvfb，[headless的核心](https://www.x.org/releases/X11R7.6/doc/man/man1/Xvfb.1.xhtml)，使用虚拟内存，来模拟UI显示
- 安装wget，jdk
- 使用`wget`下载chrome的`deb`版本

```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
```

- 使用`dpkg`安装chrome
- 添加`Xvfb`的运行参数: `ADD protractor.sh /protractor.sh`,`protractor.sh`文件内容

```
#!/bin/bash
xvfb-run --server-args='-screen 0 1280x1024x24' protractor $@
```

**源代码地址：**[https://github.com/aimer1124/protractor-headless](https://github.com/aimer1124/protractor-headless)

# 参考
- [Headless Browser Testing With Xvfb](http://tobyho.com/2015/01/09/headless-browser-testing-xvfb/)
- [docker hub protractor-headless](https://hub.docker.com/r/webnicer/protractor-headless/)
- [Protractor browser setting up](http://www.protractortest.org/#/browser-setup#setting-up-phantomjs)
- [XVFB](https://www.x.org/releases/X11R7.6/doc/man/man1/Xvfb.1.xhtml)


----------


**本文首发于简书： [E2E测试之Headless browser容器化](http://www.jianshu.com/p/4a830d22614d)**
