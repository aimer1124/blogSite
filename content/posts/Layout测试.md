---
title: 'Layout测试'
tags:
  - Layout测试
  - E2E
  - Node.js
  - Galen
categories:
  - Tool
date: 2016-11-28 15:40:00
---


Web页面Layout测试，一直是测试人员比较头疼的事情。原因有
- 当前市面中设备的`分辨率`千差万别
- 浏览器版本众多，工作量很大

如何使用`高效`的方式来测试Web Layout是否能正常，下面来看下[Galen](http://galenframework.com/)是如何帮助我们的

## [Galen](http://galenframework.com/)的特点

- 开源项目，License基于[Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0)
- 可测试页面布局、响应式设计，支持功能测试
- 基于[Selenium](http://www.seleniumhq.org/)，对Selenium Grid支持很好，可直接在[Sauce Labs](https://saucelabs.com/)和 [BrowserStack](https://www.browserstack.com/)
- 支持并行测试，减少测试时间
- 语法简洁

<!--more-->

```
@objects
    comments            #comments
    article-content     div.article

= Main section =
    @on mobile, tablet
        comments:
            width 300px
            inside screen 10 to 30px top right
            near article-content > 10px right

    @on desktop
        comments:
            width ~ 100% of screen/width
            below article-content > 20px
```

## 使用

### 安装
- `Java 1.8`或更新版本
- NPM安装
```
sudo npm install -g galenframework-cli
```
- 验证安装
```
➜  Downloads galen -v
Galen Framework
Version: 2.3.2
JavaScript executor: Rhino 1.7 release 5 2015 01 29
```

### 第一个测试项目

- 测试页面: [http://samples.galenframework.com/tutorial1/tutorial1.html](http://samples.galenframework.com/tutorial1/tutorial1.html)
- 创建一个`空文件夹`，新增一个文件`home-page.gspec`
- `home-page.gspec`内容如下

```
@objects
    header              id      header

= Main section =
    header:
        height 100px
```

- 测试验证的内容是`header`元素的高为`100px`
- 下载一个`driver`，本次测试以下载`chromedriver`为例
  - [geckodriver](https://github.com/mozilla/geckodriver)
  - [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/)
- 修改配制: `~/.galen.config`
  - 浏览器配制
  ```
  # Default browser
  # ~~~~~~~~~~~~~~~~~~~~~~~~
  # A browser that should be used by default in case it was not specified in galen test
  galen.default.browser=chrome
  ```
  - 在配制文件内，追加`driver`本机路径
  ```
  $.webdriver.chrome.driver=~/Documents/All/Software/driver/chromedriver
  ```
- 执行测试

```
galen check home-page.gspec
     --url http://samples.galenframework.com/tutorial1/tutorial1.html
     --size 640x480  
     --htmlreport .
```
  - 执行测试时，会先将浏览器启动
  - 浏览器的大小为`640x480`
  - 对比`header`元素的height是否为100px
  - 在当前`home-page.gspec`的文件夹中，会生成测试报告
  - 以下为执行过程日志

```
➜  galenDemo galen check home-page.gspec --url http://samples.galenframework.com/tutorial1/tutorial1.html --size 640x480 --htmlreport .
========================================
Test: home-page.gspec
========================================
Starting ChromeDriver 2.25.426935 (820a95b0b81d33e42712f9198c215f703412e1a1) on port 7505
Only local connections are allowed.
Nov 28, 2016 3:15:04 PM org.openqa.selenium.remote.ProtocolHandshake createSession
INFO: Attempting bi-dialect session, assuming Postel's Law holds true on the remote end
Nov 28, 2016 3:15:05 PM org.openqa.selenium.remote.ProtocolHandshake createSession
INFO: Detected dialect: OSS
check  home-page.gspec --url http://samples.galenframework.com/tutorial1/tutorial1.html --size 640x480 --htmlreport . -Dwebdriver.chrome.driver=/usr/local/lib/node_modules/galenframework-cli/node_modules/chromedriver/lib/chromedriver/chromedriver
= Main section =
    header:
        height 100px


========================================
----------------------------------------
========================================
Suite status: PASS
Total tests: 1
Total failed tests: 0
Total failures: 0
```

- 查看测试报告

![测试报告](/img/Galen/TestReport.png)

> 至此，使用Galen进行单个页面布局的测试就已经结束了。下面再进行一次测试`修改元素高度`

- 修改`header`元素的height是否为40px，`home-page.gspec`

```
@objects
    header        id    header
= Main section =
    header:
        height 40px

```

－ 再次执行测试，查看测试结果

```
➜  galenDemo galen check home-page.gspec --url http://samples.galenframework.com/tutorial1/tutorial1.html --size 640x480 --htmlreport .
========================================
Test: home-page.gspec
========================================
Starting ChromeDriver 2.25.426935 (820a95b0b81d33e42712f9198c215f703412e1a1) on port 9809
Only local connections are allowed.
Nov 28, 2016 3:24:11 PM org.openqa.selenium.remote.ProtocolHandshake createSession
INFO: Attempting bi-dialect session, assuming Postel's Law holds true on the remote end
Nov 28, 2016 3:24:12 PM org.openqa.selenium.remote.ProtocolHandshake createSession
INFO: Detected dialect: OSS
check  home-page.gspec --url http://samples.galenframework.com/tutorial1/tutorial1.html --size 640x480 --htmlreport . -Dwebdriver.chrome.driver=/usr/local/lib/node_modules/galenframework-cli/node_modules/chromedriver/lib/chromedriver/chromedriver
= Main section =
    header:
->      height 40px
->      :   "header" height is 100px instead of 40px


========================================
----------------------------------------
========================================
Failed tests:
    home-page.gspec

Suite status: FAIL
Total tests: 1
Total failed tests: 1
Total failures: 1
There were failures in galen tests
```

- 测试失败`FAIL`，查看测试报告中具体报告
  - 选择`Tests`页签
  - 点击`home-page.gspec`，会自动显示具体的报错信息
![测试失败，报告显示](/img/Galen/TestFailReport.png)

> 到目前为止，我们可以发现，使用Galen进行页面布局测试会很方便和快速，且错误信息显示足够详细

## 总结

- 使用Galen进行测试时，可以很快速的切换不同的`浏览器`和`浏览器大小`，来支持Layout测试
- Galen自带的测试报告，可以帮助测试人员，`快速定位`出具体的问题在哪。
- Galen基于Selenium，还可用来进行功能测试，可以将`Layout`测试与`Function`测试结合一起使用

## 参考

- [Galen](http://galenframework.com/)
- [Install Galen](http://galenframework.com/docs/getting-started-install-galen/)
- [First Project-Galen](http://galenframework.com/docs/tutorial-first-project/)
