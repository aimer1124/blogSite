---
title: 'JMeter3.2更新内容'
tags:
  - JMeter
  - 性能测试
categories:
  - Translate
date: 2017-05-13 14:50:00
---

 - `2017.4.14`，JMeter3.2版本发布。
 - 原文地址：[Apache JMeter 3.2 Release Notes ](http://jmeter.apache.org/changes.html),
 - 下载地址： [Download Apache JMeter 3.2](http://jmeter.apache.org/download_jmeter.cgi)

## 重要变更
JMeter现在需要`Java8`。确保你使用的最新版本的Java。
JMeter日志已经被迁移至SLF4J和Log4j 2。这个影响配制和第三方插件，查看下面的『日志变更』.
在使用JMeter的3.2版本时，在结果树中的结果数里从默认修改为500.如果你想查看更多，必须修改属性`view.results.tree.max_results`为一个更高的数值或者你不想限制数量可改为0。你可以在`bin/user.properties`中设置。更多的信息可查看[这里](http://jmeter.apache.org/usermanual/component_reference.html#View_Results_Tree)



### 主要提升
- JMeter现在提供一个新的`BackendListener`与`InfluxDB`交互
![BackendListener](http://jmeter.apache.org/images/screenshots/changes/3.2/backend_influxdb.png)
这个功能使用异步的HTTP请求发送数据至InfluxDB通过[HTTP API](https://docs.influxdata.com/influxdb/v1.2/guides/writing_data/)并提供下面的图形展示结果
![Graph](http://jmeter.apache.org/images/screenshots/backend_listener_influxdb_graph.png)

<!--more-->

- DNS缓存管理器提供静态表来管理host
![DNS Cache Manager](http://jmeter.apache.org/images/screenshots/changes/3.2/dns_cache_manager_static_hosts.png)
- JMS Publisher和Subscriber现在允许在暂停的错误情况下，重新链接
![JMS Publisher](http://jmeter.apache.org/images/screenshots/changes/3.2/jms_publisher_reconnect.png)
![JMS Subscriber](http://jmeter.apache.org/images/screenshots/changes/3.2/jms_subscriber_reconnect_pause.png)
- JMS Publisher中的变量支持所有类型的信息。添加编码类型来转换内容中的类型
![JMS Publisher Encoding](http://jmeter.apache.org/images/screenshots/changes/3.2/jms_subscriber_content_encoding.png)
- XPath提取器允许随机提取，通过索引或者所有的匹配
![XPath Extractor](http://jmeter.apache.org/images/screenshots/changes/3.2/xpath_extractor_matchno.png)
- 响应断言现在支持在请求头中，提供一种`或`的组合方式。
![Response Header Assertion](http://jmeter.apache.org/images/screenshots/changes/3.2/response_assertion.png)
- JMeter现在使用Oracle Nashorn Javascript引擎来替代Rhino。新引擎提供更快速的Javascript招待。
- HTTP HC4默认提供基础验证。
- 在CSS中的内嵌资源下载已经被改进，减少在查找资源时的重复转换。
- 在测试代码质量和代码覆盖率中也有一个重要的提升，自Sonar已经被内置。你可以在这里查看Sonar的[报告](https://builds.apache.org/analysis/overview?id=12927)

### 样式提升
- 当运行测试时，由于Sample Reults监听器数量限制和GUI的工作方式的更新，GUI模式将会有更快的响应和对内存更少的影响。
- HTTP请求的样式被精简并提供更多的位置用于参数和请求体的配制。
![HTTP Request](http://jmeter.apache.org/images/screenshots/changes/3.2/http_request.png)
- HTTP(S) Test Script Recorder更加精简和清晰。
![HTTP(S) Test Script Recorder](http://jmeter.apache.org/images/screenshots/changes/3.2/http_recorder_2.png)
- `Replace`特性被添加至搜索功能中，用于替换一些元素。
![Search](http://jmeter.apache.org/images/screenshots/changes/3.2/search_replace.png)

```
ReplaceAll不会在所有的元素中生效，只会在：
- HeaderManager： 替换值
- Http Request： 替换参数，路径和地址
```

- 查看结果树现在提供一种需要JavaFX的更实时的浏览方式。
- 你可以添加一个上下文的思考时间，它会添加思考时间在sampler和Transaction控制器的选择节点之间。
![Think Time](http://jmeter.apache.org/images/screenshots/changes/3.2/menu_add_think_times.png)
- 你现在可以针对Transaction控制器应用一种命名策略。默认策略时存在的，但你可以增强你自己的策略通过[org.apache.jmeter.gui.action.TreeNodeNamingPolicy](http://jmeter.apache.org/api/org/apache/jmeter/gui/action/TreeNodeNamingPolicy.html)和配制`naming_policy.impl`属性。
![naming_policy](http://jmeter.apache.org/images/screenshots/changes/3.2/menu_apply_naming_policy.png)
- 在View Results in Table、Summary Report、 Aggregate Report and Aggregate Graph中，现在支持针对每个价值流的排序。
![Sorter](http://jmeter.apache.org/images/screenshots/changes/3.2/sorting.png)

### 报告和仪表盘提升
- 统计数据已经被重新组装，使报告更加清晰：
![Statistics](http://jmeter.apache.org/images/screenshots/dashboard/report_statistics.png)
- 现在可以基于正则表达式或sample名来定制每一个Transaction的APDEX阀值。下面这个示例用于应用在对于Sampler的样式中不同的阀值，sampleA、scenarioB和默认的(500至1500应用于静态分析和容量阀值)被声明：

```
jmeter.reportgenerator.apdex_satisfied_threshold=500
jmeter.reportgenerator.apdex_tolerated_threshold=1500
jmeter.reportgenerator.apdex_per_transaction=sample(\\d+):1000|2000;\
    sampleA:3000|4000;\
    scenarioB:5000|6000
```

### 文档提升
- PDF文档已经被合并且更新到HTML的用户手册中。
