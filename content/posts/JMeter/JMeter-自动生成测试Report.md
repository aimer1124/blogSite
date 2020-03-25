---
title: 'JMeter-自动生成测试Report'
tags:
  - JMeter
  - 性能测试
categories:
  - Tool
date: 2016-09-23 18:53:00
---

# Dashboard Report

[JMeter3.0](http://jmeter.apache.org/changes.html)版本发布后，开始支持`动态`报表报告。让测试人员编写`性能测试报告`更加容易。

- 支持在`测试结束`后，生成测试报告

- `导入`之前测试结果，生成测试报告

下面就看下如何使用这个`新特性`，生成测试报告

<!--more-->

## 测试结束后，生成本次测试的报告

- 执行测试文件

- 生成测试结果文件

- 生成最终的测试报告

```
jmeter -n -t test.jmx -l result.jtl -e -o /tmp/ResultReport
```

参数说明:
- `-n`: `非GUI`模式执行JMeter

- `-t`: 执行测试文件所在的`位置`

- `-l`: 指定生成测试结果的保存文件，`jtl`文件格式

- `-e`: 测试结束后，生成测试报告

- `-o`: 指定测试报告的存放位置

> `-l` `-o`指定的文件及文件夹，必须**不存在**，否则执行会失败

## 使用之前的测试结果，生成测试报告

将`已存在`的测试结果文件，生成测试报告

```
jmeter -g result.jtl -o /tmp/ResultReport
```

参数说明:

- `-g`: 指定`已存在`的测试结果文件

> 两种方式，其实最终都`依赖`生成的`测试报告`。双击`报告`文件夹中的`index.html`即可查看报告。


# 报告详解

## Dashboard

### Test and Report informations

测试和报告信息: 测试结果保存文件/测试开始时间/测试结束时间/展示过滤器。

### APDEX(Application Performance Index)

应用程序性能满意度的标准，范围在`0-1`之间，1表示达到所有用户均满意。是由[APDEX公司](http://www.apdex.org/)推出的。计算公式:

![Apdex](https://wikimedia.org/api/rest_v1/media/math/render/svg/7749342d1b53a253e3b4c0e55cd5b2f2208f89cb)

### Requests Summary

请求的`通过率(OK)`与`失败率(KO)`，百分比显示。

### Statistics

数据分析，基本将`Summary Report`和`Aggrerate Report`的结果合并。

### Errors

错误情况，依据不同的错误类型，将所有错误结果展示。

## Charts

用`图表`的形式展示测试数据，让测试报告更加`直观`。特点:

- 将测试过程中`经常`使用的数据，用图表的形式展示，让测试结果更加直观

- 每个图表数据，有`两种`展示形式。

- 支持`请求样例`过滤显示

- 支持导出`PNG`图片格式

### Over Time

- Response Times Over Time: `响应`时间

- Bytes Throughput Over Time: 字节`接收/发送`的数量

- Latencies Over Time:`延迟`时间

### Throughput

- Hits Per Second: 每秒点击率

- Codes Per Second: 每秒状态码数量

- Transactions Per Second: 每秒事务量

- Response Time Vs Request: 响应时间点请求的`成功/失败`数

- Latency Vs Request: 延迟时间点请求的`成功/失败`数

### Response Times

- Response Time Percentiles: 响应时间百分比

- Active Threads Over Time: 激活线程数

- Time Vs Threads: 测试过程中的线程数时续图

- Response Time Distribution: 响应时间分布

> 了解到每个报表的功能，就可以将需要的报表添加到`测试报告`中。

# 问题

- 报表中，中文命名的`Label`会显示乱码

# 总结

- [JMeter3.0](http://jmeter.apache.org/changes.html)中提供了丰富的报表展示，很便于编写`性能测试报告`中的数据展示

- 在生成测试报表时，[JMeter](http://jmeter.apache.org)还提供了`丰富`的参数配制，配制文件在`/bin/reportgenerator.properties`中。具体配制方法可参考: [http://jmeter.apache.org/usermanual/generating-dashboard.html](http://jmeter.apache.org/usermanual/generating-dashboard.html)

- [JMeter3.0](http://jmeter.apache.org/changes.html)中提供的报表功能，在[Plugin-Manager](https://jmeter-plugins.org/)中的`3 Basic Graphs`和`5 Additional Graphs`有**部分**功能是有重复的。

# 参考

- [Wikipedia-Apdex](https://en.wikipedia.org/wiki/Apdex)

- [JMeter-Generating Dashboard](http://jmeter.apache.org/usermanual/generating-dashboard.html)


本文首发于: [简书-JMeter-自动生成测试报告](http://www.jianshu.com/p/c9f9a06df5cb)
