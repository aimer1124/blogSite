---
title: 'JMeter3.3更新内容'
tags:
  - JMeter
  - 性能测试
categories:
  - Translate
date: 2017-10-09 10:50:00
---


 - `2017.9.21`，JMeter3.3版本发布。
 - 原文地址：[Apache JMeter 3.3 Release Notes ](http://jmeter.apache.org/changes.html),历史版本变更记录[http://jmeter.apache.org/changes_history.html](http://jmeter.apache.org/changes_history.html)
- 下载地址： [Download Apache JMeter 3.3](http://jmeter.apache.org/download_jmeter.cgi)

## 重要变更

```
JMeter 还不支持 Java9，下个版本将会支持，你可以给出帮助并查看此跟踪记录[Bug 61529](https://bz.apache.org/bugzilla/show_bug.cgi?id=61529)。
```

```
建议：使用最新版本的 Java8 ，避免出现 JDK 的问题。
```

### 主要提升

HTTP 样例支持[Brotli](https://news.ycombinator.com/item?id=10257305)解压算法。

CacheManager 现在完全支持变量头方式。

InfluxDB BackendListener 现在支持通过 UDP 协议发送结果至 InfluxDB。

![InfluxDB BackendListener](http://jmeter.apache.org/images/screenshots/changes/3.3/influxdb_udp.png)

已经被增强来通过响应状态码和消息针对每一个 Transaction 发送错误数量。

TCP 样例现在可以计算延迟，详情查看[Bug 60156](https://bz.apache.org/bugzilla/show_bug.cgi?id=60156)

更新依赖至最新版本，用于提升性能和修复 BUG。

持续提升代码质量和测试覆盖率。查看[质量报告](https://builds.apache.org/analysis/overview?id=12927)

<!--more-->

### 样式提升

花费更多的工作，用于提升对 HiDPI 的支持。

一些 BUG，像在低内存中使用 View Results Tree 会很慢的，已经被修复。

常量 **DEFAULT_IMPLEMENTATION** 被从 CookieManager 中删除，删除它是为了在最新版本中支持`HTTP Client` 的改变。

JDBC 样例中的样式被提升，添加选择框来选择驱动器和验证查询。

![JDBC 样例 选择框](http://jmeter.apache.org/images/screenshots/changes/3.3/jdbc_config_validation_driver_url.png)

![JDBC 样例 验证查询](http://jmeter.apache.org/images/screenshots/changes/3.3/jdbc_config_validation_query.png)

If 控制器和 While 控制器的样式也被提升了。

![If 控制器](http://jmeter.apache.org/images/screenshots/changes/3.3/jmeter_if_controller.png)

### 报告和仪表盘提升

新的Help 菜单按钮被添加，用于快速配制报告的生成规则。

![Help 菜单按钮](http://jmeter.apache.org/images/screenshots/changes/3.3/jmeter_export_transactions_menu.png)

![Help 规则配制](http://jmeter.apache.org/images/screenshots/changes/3.3/jmeter_export_transactions_result.png)

### 文档提升

合并关于不清晰的文档反馈信息


### 功能

Function Helper 对话框：新增区域用于展示执行结果 

![Function Helper](http://jmeter.apache.org/images/screenshots/changes/3.3/jmeter_function_result.png)

**新功能：**

- `_timeShift` - 返回变量时间计算后的时间模式
![_timeShift](http://jmeter.apache.org/images/screenshots/changes/3.3/jmeter_function_add_time.png)
- `_RandomDate` - 在特定时间范围内生成随机时间
![_RandomDate](http://jmeter.apache.org/images/screenshots/changes/3.3/jmeter_function_random_date.png)