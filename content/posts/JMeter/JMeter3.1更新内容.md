---
title: 'JMeter3.1更新内容'
tags:
  - JMeter
  - 性能测试
categories:
  - Translate
date: 2017-03-09 16:30:00
---


> `2016.11.20`，[JMeter](http://jmeter.apache.org/)官网已经正式发布了3.1的版本，今天尝试翻译下更新内容，内容中肯定还有很多不足，希望大家多多谅解。
 - 原文地址：[Apache JMeter 3.1 Release Notes ](http://jmeter.apache.org/changes.html),
 - 下载地址： [Download Apache JMeter](http://jmeter.apache.org/download_jmeter.cgi)

## 提升报告和仪表盘
仪表盘新增三个图表和一个概要表格
- 连接时间
![](http://jmeter.apache.org/images/screenshots/dashboard/report_connect_time_over_time.png)
- 成功百分比响应时间
![](http://jmeter.apache.org/images/screenshots/dashboard/response_time_percentiles_over_time.png)
- 响应时间分布
![](http://jmeter.apache.org/images/screenshots/dashboard/response_time_overview.png)
- 执行样例中的错误Top5
![](http://jmeter.apache.org/images/screenshots/dashboard/top_5_errors_by_sampler.png)

<!--more-->

- 细化错误表中的错误信息
- 静态分析表中添加`平均响应时间`
![](http://jmeter.apache.org/images/screenshots/dashboard/report_statistics.png)
- 激活线程表中显示堆叠线程数
![](http://jmeter.apache.org/images/screenshots/dashboard/report_active_threads_over_time.png)

## 新的维度
- `sent_bytes`被添加至发送服务器的数据统计中。
- `connect_time`在本版本中默认可用。

## 处理大的响应
JMeter现在可以处理大于2GB的响应数据，最大限制是9223372TB。为了处理大响应，当可以缩减响应来避免内存溢出。具体查看`httpsampler.max_bytes_to_store_per_request`属性.

## 新函数`__groovy`
介绍一个新函数`__groovy`来使用Groovy可用。当在使用高并发测试时，这个会很有用。就像JavaScript脚本会很平滑一样(同样适用于BeanShell)。

## 对于`JSR-223`元素默认使用Groovy
Groovy是JSR-223元素使用的默认语言。如果你想使用其它的语言，你必须要做出明确的选择：
> 虽然我们建议你来检查它来确保你没有使用`${varName}`语法而是用`vars.get("varName")`来代替。默认情况下通常`如果可用的编译缓存数据`是不需要检查的，

## 在结果树中格式化HTML显示
在结果树中的HTML代码现在可以格式化来查看。这是相当有用的，在网页中的代码已被删除多余的空格代码。
![](http://jmeter.apache.org/images/screenshots/html-formatted-tree-view.png)

## 使用一个属性来更新所有的定时器
新的属性`timer.factor=1.0f`已被添加，用于来`倍数`调整计数器，如`Gaussian,Uniform和Poisson计数器`。它可使用一处的调整来更新整个产品的`Think Time`。


## 主要提升
- 大量样式和布局内容修复
- 内存使用提升
- JDBC请求现在可以返回Blob/Clob，并且可计算延迟和连接时间
- 在3.0版本中的CSS转化已经优化至内存级别
- HTTP请求现在可以处理在Get请求中的数据体，比如这个针对`Elastic`请求很有用

## 文档更新
- 文档的审查和改进更容易
- 新增[属性文档](http://jmeter.apache.org/usermanual/properties_reference.html)
