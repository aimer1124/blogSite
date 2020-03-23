---
title: '性能测试最佳实践之JMeter'
tags:
 - JMeter
 - 性能测试
categories:
 - Translate
date: 2016-08-31 20:45:38
---

# 保持使用最新版本
JMeter被经常推荐用来测试性能，鼓励用户使用最新的版本。

确保你要经常去阅读[变更记录](http://jmeter.apache.org/changes.html)中的新功能和模块的提升。你不应该再使用3.0之前的版本了

# 使用正确的线程数
你硬件设备的能力及测试计划将都会影响你的JMeter可运行的线程数。数量也依赖于你的服务有多快(一个可快速响应的服务可以让JMeter变更更加给力)。像其它性能测试工具一样，如果你没有正确的线程数，你将面对不准备或错误结果的`Coordinated Omission`问题。如果你需要大数量级的压力测试，考虑使用分布式模式在多台机器上运行无GUI的JMeter实例。当使用分布式模式时，结果将被聚合在控制器的结果中，如果使用多个自已的实例，结果文件可以聚合用于持续性分析。对于如何在一个给定的平台上使用JMeter测试，`JavaTest Sampler`可以考虑使用。它不需要任何网络请求便可返回一些信息在最大的吞吐量。

JMeter有选项用于延迟线程创建直到线程正常启动，如在其它线程组延迟之后和线程自身的启动时间。这样就允许一个非常大数量级的线程数，不需要太多的线程同时并发。

<!--more-->

# Cookie管理器的位置
可在[构建一个Web测试](http://jmeter.apache.org/usermanual/build-web-test-plan.html#adding_cookie_support)中查看

# Authorization管理器的位置
可在[构建一个高级Web测试](http://jmeter.apache.org/usermanual/build-adv-web-test-plan.html#header_manager)中查看

# 使用`HTTP(S) Test Script Recorder`录制
关于[HTTP(S) Test Script Recorder](http://jmeter.apache.org/usermanual/component_reference.html)的细节在建议录制器中。最重要的事情是，剔除你不感兴趣的。比如，不关心在录制过程中的图片请求(JMeter可以下载一个页面中的所有图片-具体查看[HTTP Request](http://jmeter.apache.org/usermanual/component_reference.html#HTTP_Request))。这些内容将会让你的测试计划一团糟糕。大部人都会这样，有一个扩展对你的所有文件集，如`.jsp,.asp,.php,.html`或者其它。这些内容你通过输入`.*\.jsp`在`Include Pattern`中**引入**。

或者，你也可以剔除图片通过输入`.*\.gif`在`Exclude Pattern`中。具体依据你的应用程序，你可以选择一种更好的方案去执行。你也可以去剔除`stylesheets,javascritpt文件和其它文件类型`。测试你的配制来验证你的录入内容是你想要的，接着清除内容并且开始刷新页面。

`HTTP(S) Test Script Recorder`期望用于使用`Recording Controller`发现`HTTP Request`记录的元素至一个线程组元素中。这样便于你可以直接将所有的样例打包至一个控制器下，当然可以再给出一个可描述测试用例的名称。

现在，执行测试用例的步骤。如果你有无前置步骤的测试用例，使用JMeter来录制你的操作定义你的测试用例。一旦你完成了一系列特定的操作，保存整个测试用例至一个合适的文件名中。接着，清理记录开始一个新的测试用例。通过这样操作，你可以快速记录大量`粗糙的`测试用例。

`HTTP(S) Test Script Recorder`最有用的一个特性是你可以通过录制的样例来抽象出通用的元素。通过定义[自定义的用户变量](http://jmeter.apache.org/usermanual/functions.html)在测试计划级别或在[用户自定义变量](http://jmeter.apache.org/usermanual/component_reference.html#User_Defined_Variables)元素中，你可以用JMeter自动替换你录制样例中的值。比如，如果你测试一个`APP`在服务**xxx.example.com**，你可以定义一个变量`server`的值为**xxx.example.com**，再所有在录制样例中的值将会被替换为**${server}**

```
匹配时，注意大小写敏感
```
如果JMeter没有录制到任何请求，检查你的浏览器是否启用代理设置。如果在JMeter没有启动时，浏览器可正常使用，那浏览器一定是没有使用代理设置。一些浏览器忽略了代理设置`localhost`或`127.0.0.1`，那么请使用本机名或IP代替。

错误`unknown_ca`可以是你正试图录入`HTTPS`，浏览器不接收JMeter的代理服务证书。

# 用户变量
一些测试计划中，需要使用不同的值对于不同的用户/线程。如，你想测试需要每个用户登录后的一系列步骤。这个使用JMeter可以很容易实现。

比如:
 * 创建一个文件，包含用户名和密码且使用逗号分隔。存放到与你的测试计划在同一文件夹。
 * 添加一个`CSV DataSet`的配制元素至你的测试计划。定义变量名为`USER`和`PASS`。
 * 替换登录名为**${USER}**和密码为**${PASS}**

`CSV DataSet`元素将会为每个线程读取一新行内容。

# 减少资源使用
减少资源使用的一些建议:
  * 使用无GUI的模式: `jmeter -n -t test.jmx -l test.jtl`
  * 尽量少使用监听器`Listener`;如果使用上面的`-l`标记，他们均可以被删除或禁用
  * 在压力测试过程中，不要使用`查看结果树`或`在Table中查看结果`监听器，仅在脚本调试阶段使用即可
  * 相比使用大量相似的样例，在一个循环中使用相同的样例，并使用变量(CSV DataSet)来实现样例的不同。[`Include Controller`在此步骤没有任何用，它在文件中添加所有的测试元素至测试计划中]
  * 不要使用功能模式
  * 使用`CSV`格式输出要优于`XML`
  * 仅保存需要的数据
  * 尽可能使用少的断言
  * 使用最优的脚本语言(查看`JSR223`部分)

如果你的测试需要大量的数据 - 特别是如果需要随机化的 - 创建测试数据在可被读取的CSV文件中。这样会避免浪费资源在运行时。

# BeanShell服务
`BeanShell`解释器有一个很有用的特性 - 当可以用来扮演`server`，可被`telnet`或`http`访问。

```
没有安全性。能连接至端口的任何人都可以发布任何BeanShell命令。这些可以提供无限制的访问至JMeter程序和目标。
不要启用服务除非端口被限制访问，如，被防火墙。
```

如果你想使用服务，在`jmeter.properties`中定义下面内容:

```
beanshell.server.port=9000
beanshell.server.file=../extras/startup.bsh
```
在上面的例子中，服务将会被启动，将会监听端口`9000`和`9001`。端口`9000`用于`http`访问，端口`9001`用于`telnet`访问。`startup.bsh`文件将会被服务处理，可被用于定义功能和启动时的变量。启动文件定义用于启动和输出JMter和系统属性的方法。这些是你将在JMeter控制台看到的:
```
Startup script running
Startup script completed
Session started on port: 9001
```
有一个样例脚本(`extras/remote.bsh`)你可以用来测试服务。[看看它怎么工作的]

当启动当在JMeter`bin`目录(调整目录，如果你在其它位置)，输出会像这样:

```
$ java -jar ../lib/bshclient.jar localhost 9000 ../extras/remote.bsh
Connecting to BSH server on localhost:9000
Reading responses from server …
BeanShell 2.0b5 - by Pat Niemeyer (pat@pat.net)
bsh % remote.bsh starting
user.home = C:\Documents and Settings\User
user.dir = D:\eclipseworkspaces\main\JMeter_trunk\bin
log_level.jmeter = INFO
log_level.jorphan = INFO
Setting property 'EXAMPLE' to '0'.
Setting property 'EXAMPLE' to '1'.
Setting property 'EXAMPLE' to '2'.
Setting property 'EXAMPLE' to '3'.
Setting property 'EXAMPLE' to '4'.
Setting property 'EXAMPLE' to '5'.
Setting property 'EXAMPLE' to '6'.
Setting property 'EXAMPLE' to '7'.
Setting property 'EXAMPLE' to '8'.
Setting property 'EXAMPLE' to '9'.
EXAMPLE = 9
remote.bsh ended
bsh % … disconnected from server.
```

举个例子，假设你有一个运行时间较长的非GUI运行模式测试，并且你想让吞吐量在测试过程中不同。测试计划包括`Constant Throughout Timer`定义属性，如`${__P(thoughput)}`。下面的`BeanShell`可用于改变测试:

```
printprop("throughput");
curr = Integer.decode(args[0]);  // Start value
inc  = Integer.decode(args[1]);  // Increment
end  = Integer.decode(args[2]);  // Final value
secs = Integer.decode(args[3]);  // Wait between changes
while(curr <= end) {
  setprop("throughput",curr.toString()); // Needs to be a string here
  Thread.sleep(secs*1000);
  curr += inc;
}
printprop("throughput");
```

脚本可以被存储在一个文件中(如，`throughput.bsh`)，使用`bshclient.jar`发送至服务。参考:

```
java -jar ../lib/bshclient.jar localhost 9000 throughput.bsh 70 5 100 60
```

# BeanShell脚本
## 概述
每一个`BeanShell`测试元素在解释器中的每个线程中均有自己的副本。如果测试元素被重复调用，如: 在`loop`中，那么元素会被解释器存储在报文中除非`Reset bsh.Interpreter before each call`选项被勾选。对扩展的压力测试，推荐使用脚本引擎集成了可编译的JSR223脚本语言，可在JSR223中查看详情。

一些运行时间较长的测试会导致解释器使用大量的内存;如果真的要这样做，尝试使用reset选项。

你可以测试`BeanShell`脚本使用命令行解释器，不依赖于JMeter:
```
$ java -cp bsh-xxx.jar[;other jars as needed] bsh.Interpreter file.bsh [parameters]
```
或
```
$ java -cp bsh-xxx.jar bsh.Interpreter
bsh% source("file.bsh");
bsh% exit(); // or use EOF key (e.g. ^Z or ^D)
```

## 共享变量
变量可以被定义在启动(安装)脚本。这些数据将会被存储在测试元素的报文中，除非你使用reset选项。

脚本也可以读取JMeter的变量通过使用`get()`和`put()`方法，如:
```
vars.get("HOST");
vars.put("MSG","Successful");
```

`get()`和`put()`方法仅支持字符串变量，但有`getObject()`和`putObject()`方法可以处理其它类型。JMeter变量对于线程是局部的，但可以被所有的测试元素使用（不适用于BeanShell）。

如果你需要共享变量在线程间，JMeter的属性可以使用:

```
import org.apache.jmeter.util.JMeterUtils;
String value = JMeterUtils.getPropDefault("name","");
JMeterUtils.setProperty("name", "value");
```

样例`.bshrc`文件包括样例`getprop()`和`setprop()`的方法定义。

其它可用于共享变量的方法，使用`bsh.shared`共享命名空间。参考:

```
if (bsh.shared.myObj == void){
    // not yet defined, so create it:
    myObj = new AnyObject();
}
bsh.shared.myObj.process();
```

相比在测试元素中创建对象，可通过JMeter的属性`beanshell.init.file`文件配制在启动时创建。这个仅会执行一次。

# 使用`BeanShell` `Javascript` `Jexl`脚本开发功能
像功能一样编写和测试脚本是很困难的。然而，JMeter有`JSR223`，`BSF`和`BeanShell`可用来尝试。

创建一个简单的测试计划包括`JSR223`或`BSF`样例和结果树监听器。在样例板块编写脚本，通过运行测试来测试它。如果有很多错误，这些结果将会被展示在结果树中。同时运行脚本的结果将会被展示像返回内容一样。

一旦脚本调试通过，可以当一个变量被存储在测试计划中。脚本的变量可被用于创建功能调用。如，支持一个`BeanShell`脚本被存储在变量`RANDOM_NAME`。功能调用可以被编写为`${__BeanShell($RANDOM_NAME)}`。不需要其它的逗号在脚本中，因为在变量值被添加之前，功能调用已经被转化。

# 参数化测试
经常对于重复运行一个测试在不同的配制中是很有用的。比如，改变线程数/循环数/改变地址名。

一种方式是在测试计划中定义变量集，并在测试元素中使用这些变量。比如，一个可以定义变量`LOOPS=10`，关联`${LOOPS}`至线程组中。为了运行测试循环20次，只需要调整`LOOPS`在测试计划中的值。

这个会快变得糟糕，如果你想在非GUI模式运行的话。一个解决方案是，定义测试计划变量在属性中，如`LOOPS=${__P(loop,10)}`。这个使用属性`loops`的值，如果没找到的话默认为`10`。`loops`属性也可被JMeter的控制台命令定义:

```
jmeter ... -Jloops=12 ...
```

如果有大量的属性在一次变更的话，一种实现方式是使用`属性文件`。`属性文件`可通过使用`-q`在命令行模式下传递至JMeter。

# `JSR223`元素
为了扩展压力测试，推荐的脚本语言是一种脚本引擎实现可编译接口的脚本语言。`Groovy`脚本引擎可编译。然而，在JMeter 2.13版本无论是`BeanShell`还是`Javascript`都没有实现，因此最好不要使用它们来扩展压力测试。

```
提醒: BeanShell继承可编译接口但还没有被实现，方法会抛异常。JMeter有一个明确的说明关于这个问题。
```

当使用`JSR223`元素时，经常设置存储一个值至一个唯一的变量中，如果语言支持它。确保脚本没有使用变量`${varName}`来存储将会获取第一个值，将会获取`${varName}`的第一个值。替换使用:

```
vars.get("varName")
```
你也可以传递他们像参数一样到脚本中，并且像这样使用它们。

# 线程组之间共享变量
变量对于线程是局部的;在一个线程中的一个变量集不能被其它线程读取。设计就是这样的。针对变量，可以在测试启动前进行明确，查看[参考化测试](#参数化测试)。如果值直到测试启动都不知道，有如下选项:
 * 存储变量在属性中 - 属性对于JMter实例是全局的
 * 写变量至文件中，重新读取他们
 * 使用`bsh.shared`命令空间 - 查看[共享变量](#共享变量)
 * 写自己的Java类

# 属性配制管理
当你需要修改JMeter属性，确保你没有修改`jmeter.properties`文件。**替换拷贝属性从`jmter.properties`并修改在`user.properties`中的值。**
这样做的话，会很容易合并至下一个JMeter版本。
注意`jmeter.properties`文件中经常涉及但被理解“从jmeter.properties拷贝到user.properties你想修改且这样做的属性。”
```
user.properties file supersedes the properties defined in jmeter.properties
```

# 过时的元素
建议不要使用过时的元素(被这样标记在[变更记录](http://jmeter.apache.org/changes.html)和在[组件相关](http://jmeter.apache.org/usermanual/component_reference.html))，并且合并使用新的元素如果可用的话，或新的方式可以实现相同的事情。
过时的元素被删除从菜单在版本`N`中，但通过修改`user.properties`中`not_in_menu`中属性可被启用，并且从那删除完整的类名。
```
请注意过滤时的元素地版本`N`将会被删除在确定的版本`N+1`中，因此尽早确保你没有使用。
```

------------------------
原文地址: [JMeter best-practices](http://jmeter.apache.org/usermanual/best-practices.html)

本文首发地址: [[译]性能测试最佳实践之JMeter](http://www.jianshu.com/p/705e850b633c)
