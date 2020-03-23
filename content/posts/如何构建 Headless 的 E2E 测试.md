---
title: '构建Headless 的 E2E 测试'
tags:
  - E2E
  - Chrome
  - Testing
  - CI
categories:
  - Testing
date: 2018-03-02 12:20:00
---


## 为什么要`构建 Headless 的 E2E 测试` 

```
A headless browser is a great tool for automated testing and server environments where you don't need a visible UI shell. For example, you may want to run some tests against a real web page, create a PDF of it, or just inspect how the browser renders an URL.
```

结合上面的原因，我们还可以
- Headless结合 E2E 测试，可以让E2E 测试在非 GUI 的操作系统中运行
- 可以集成至 CI 环境中。让版本得到快速验证

### Chrome Headless 的选取

- Mac/Linux 的Chrome从59版本后，已经支持 Healess 模式的运行。Windows 的从60版本开始支持
- 所以选择一个你想要的 Chrome 版本，便可以进行 Headless 的测试

```
chrome \
  --headless \                   # Runs Chrome in headless mode.
  --disable-gpu \                # Temporarily needed if running on Windows.
  https://www.chromestatus.com   # URL to open. Defaults to about:blank.
```

<!--more-->

### 编写 E2E 测试 - `BDD-Gauge`

#### BDD

- home.spec

```     
Search
----------------

* Search with 123
```

- home.cpt

```
# Search with 123
* Open Baidu homepage
* Search 123
* Check searching result
```

#### 编写测试实现

使用 Selenium 完成测试用例的实现过程。核心实现

```
System.setProperty("webdriver.chrome.driver", "Path/chromedriver");
ChromeOptions options = new ChromeOptions();
options.addArguments("--headless");
options.addArguments("--disable-gpu");
return new ChromeDriver(options);
```

### 执行测试

`./gradlew clean gauge`

```
:clean
:compileJava UP-TO-DATE
:processResources UP-TO-DATE
:classes UP-TO-DATE
:compileTestJava
:processTestResources UP-TO-DATE
:testClasses
:gauge
Feb 28, 2018 10:48:01 PM org.openqa.selenium.remote.DesiredCapabilities chrome
INFO: Using `new ChromeOptions()` is preferred to `DesiredCapabilities.chrome()`
Starting ChromeDriver 2.35.528157 (4429ca2590d6988c0745c24c8858745aaaec01ef) on port 26606
Only local connections are allowed.
Feb 28, 2018 10:48:02 PM org.openqa.selenium.remote.ProtocolHandshake createSession
INFO: Detected dialect: OSS
# Baidu HomePage
  ## Search   ✔ ✔ ✔auge

Successfully generated html-report to => /Users/yjshi/Documents/GaugeChromeHeadless/reports/html-report/index.html
Specifications:     1 executed      1 passed        0 failed        0 skipped
Scenarios:      1 executed      1 passed        0 failed        0 skipped

Total time taken: 3.097s

BUILD SUCCESSFUL

Total time: 7.313 secs
```

### 挂接 CI


由于现在主流的 CI 在执行 Job 时，都是在 Agent 中执行。因此在跑 Gauge 时，需要在 Agent 中做好`准备`工作。

#### 准备工作 - Agent
- 安装 Gauge 及 Java 插件
- 安装 Chrome 
- 替换`BrowserDriver`目录中的 driver 为匹配的版本

#### 跑起来

- 将代码通过 Job 拉取到本地
- 执行`./gradlew clean gauge`

#### 注意事项

- CI执行 Job 的用户不能用 `root`用户

## 完整代码

[GaugeChromeHeadless](https://github.com/aimer1124/GaugeChromeHeadless)

## 参考 

- [Gauge](https://gauge.org/index.html)
- [ChromeDriver](http://chromedriver.storage.googleapis.com/index.html)
- [Getting Started with Headless Chrome](https://developers.google.com/web/updates/2017/04/headless-chrome)
- [WebDriverException: unknown error: Chrome failed to start: exited abnormally](https://github.com/SeleniumHQ/selenium/issues/4961)