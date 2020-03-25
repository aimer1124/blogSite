---
title: 'JMeter与BeanShell的化学反应'
tags:
  - JMeter
  - 性能测试
categories:
  - Tool
date: 2016-11-01 15:53:00
---

## JMeter是什么
[http://jmeter.apache.org/](http://jmeter.apache.org/)，性能测试工具。
- 基于`Java`的`开源`性能测试工具
- 支持测试的协议
  - Web - HTTP, HTTPS
  - SOAP / REST
  - FTP
  - Database
  - LDAP
  - Message-oriented middleware (MOM)
  - Mail
  - Native commands or shell scripts
  - TCP
- 支持多线程并发
- 完善的GUI界面，用于快速设计测试计划和调试测试脚本
- 完整测试结果，便于结果分析
- JMeter不会执行HTML中的JavaScript脚本

## BeanShell是什么
[http://beanshell.org/](http://beanshell.org/)
- 基于`Java`的免费解释器
- 松散类型的脚本语言
- 动态执行的Java代码
- 只有150K大小的JAR包

> BeanShell既然可以编写Java代码，那么我们就可以在使用JMeter测试的过程中，使用Java语法功能，且支持关键字`高亮`，进行业务逻辑的处理，进而达到`场景`功能的设计。

<!--more-->

## BeanShell与JMeter的化学反应

### JMeter提供`5`种方式使用BeanShell

- BeanShell Sampler
直接使用BeanShell来编写`样例`。
- BeanShell  PreProcessor
在`样例`触发前，使用BeanShell进行加工处理。
- BeanShell  PostProcessor
在`样例`触发后，使用BeanShell进行加工处理。
- BeanShell  Assertion
使用BeanShell进行`断言`处理。
- BeanShell  Listener
使用BeanShell做`监听器`。

> JMeter提供的BeanShell功能，遍布整个测试的`各个阶段`。只要你需要的时候，它都可以直接`拿`来用。

### 变量处理
- JMeter中已有变量名`name`，值为`testBeanShell`
![变量](/img/JMeter-BeanShell/Variable.png)
- 配制BeanShell的`Parameters`，传入参数`test`。并`编写`变量内容输出代码，log不是Java内置的对象，但是JMeter的内置对象。
```
log.info("Test is " + vars.get("test"));
```
![输出变量内容](/img/JMeter-BeanShell/GetVariable.png)
- 执行测试，便可查看出变量内容的输出
![变量内容的输出](/img/JMeter-BeanShell/LogVariable.png)

> 通过上面的BeanShell脚本，我们可以发现BeanShell可以直接获取JMeter的变量内容。下面我们针对变量内容进行加工，看下如何实现

- 将`test`变量的值获取后，再随机在原变量值后`追加`随机数，并再次赋值给`test`变量
```
log.info("Init test: " + vars.get("test"));
Random ran = new Random();
int x = ran.nextInt(6);
vars.put("test",vars.get("test")+x);
log.info("Random test: " + vars.get("test"));
```
- 执行测试，查看结果
![加工后的变量结果](/img/JMeter-BeanShell/RefactorVariable.png)

### 使用自定义的JAR包

- `Java`源文件
  >`appendString`类中有方法`append`: 将参数的内容追加`-Append`后，返回`追加后`的字符串

```Java
package com.test;
public class appendString {
  public String append(String sourceString){
    return sourceString + "-Append";
  }
}

```

- 生成Jar包
  > 利用其它工具将此源文件打包成`Jar`文件

- JMeter中`引用`Jar包功能
  > 将`Jar`包`复制`至JMeter下方`lib/ext`下

- `重新打开`JMeter，进入`BeanShell`中，添加调试代码：输出`加工`后的内容

```
import com.test.appendString;
log.info(new appendString().append("111"));
```

- 查看JMeter的日志输出：加工后的字符为`111-Append`
![JarWithBeanShell](/img/JMeter-BeanShell/JarWithBeanShell.png)

> 通过上面的方法，我们可以看出，通过JMeter与BeanShell的结合，可以将外部的代码与JMeter结合，也可直接使用BeanShell来操作JMeter内部的数据处理。
下面我们再看下`BeanShell`提供了哪些内置的操作对象

### BeanShell的内置对象

| 对象名  | 存在元素  | 功能  |
|:---|:---|:---|
|  log | BeanShell Sampler <br> BeanShell PreProcessor <br> BeanShell PostProcessor <br> BeanShell Assertion <br> BeanShell Listener  |日志信息输出   |
|  Label | BeanShell Sampler  |样例   |
|  FileName | BeanShell Sampler  |文件名   |
|  Parameters | BeanShell Sampler  |参数   |
|  bsh.args | BeanShell Sampler  |BeanShell脚本   |
|  SampleResult | BeanShell Sampler <br> BeanShell Assertion <br> BeanShell Listener  |样例结果   |
|  ResponseCode | BeanShell Sampler <br> BeanShell Assertion  |返回的状态码   |
|  ResponseMessage | BeanShell Sampler <br> BeanShell Assertion  |返回信息   |
|  IsSucess | BeanShell Sampler  |是否成功   |
|  ctx | BeanShell Sampler <br> BeanShell PreProcessor <br> BeanShell PostProcessor <br> BeanShell Assertion <br> BeanShell Listener  |JMeter的上下文   |
|  vars | BeanShell Sampler,BeanShell PreProcessor <br> BeanShell PostProcessor <br> BeanShell Assertion <br> BeanShell Listener  |变量操作   |
|  props | BeanShell Sampler <br> BeanShell PreProcessor <br> BeanShell PostProcessor <br> BeanShell Assertion <br> BeanShell Listener  |JMeter属性   |
|  prev | BeanShell PreProcessor <br> BeanShell PostProcessor <br> BeanShell Listener |样例的`前置`结果`读取`   |
|  sampler | BeanShell PreProcessor <br> BeanShell PostProcessor  |当前样例   |
|  Response |  BeanShell Assertion |返回的对象，读-写 |
|  Failure |  BeanShell Assertion |是否失败   |
|  FailureMessage |  BeanShell Assertion |失败信息   |
|  ResponseData |  BeanShell Assertion |返回数据体，字节形式   |
|  ResponseHeader |  BeanShell Assertion |返回信息头  |
|  RequestHeader |  BeanShell Assertion |请求信息头  |
|  SampleLabel |  BeanShell Assertion |样例名称  |
|  SampleData |  BeanShell Assertion |发送至服务器的数据  |
|  SampleEvent |  BeanShell Listener |读取当前样例的事件 |

> 有了上面的操作对象，可以在测试过程中，对测试的内容，进行更加详细的`加工`。
完善的对象使用方法，可查阅[JMeter官方API文档](https://jmeter.apache.org/api/)

## 后期应用扩展

- 将请求的数据进行`个性化`加工
- 将获取的数据进行扩展`保存`
- `完善`业务场景

## 参考

- [http://jmeter.apache.org/](http://jmeter.apache.org/)
- [https://jmeter.apache.org/api/](https://jmeter.apache.org/api/)
- [http://beanshell.org/](http://beanshell.org/)
