---
title: 'JMeter5.1更新内容'
tags:
  - JMeter
  - 性能测试
categories:
  - Translate
date: 2019-03-19 20:00:00
---

## 核心能力提升

- JDBC测试已被提升，可以直接设置SQL语句并支持查询超时功能。

![JDBC Connection](http://jmeter.apache.org/images/screenshots/changes/5.1/jdbc-connection-config-init-request.png)

- 变量问题已被修复，像使用`HTTP(S) Test Script Recorder`录制HTTPS请求时收集正确的请求头信息。
- 在5.0版本中，JMeter已调整使用自定义的命令策略来重命名子结果([BUG_62550](https://bz.apache.org/bugzilla/show_bug.cgi?id=62550))，这个变更对功能测试很麻烦，新的属性`subresults.disable_renaming=true`用于解决这个问题。替代方法是使用在功能测试的测试计划中校验([BUG_63055](https://bz.apache.org/bugzilla/show_bug.cgi?id=63055))。

<!--more-->

## 样式提升

在使用录制时，模板提供了参数化的功能。

![Templates](http://jmeter.apache.org/images/screenshots/changes/5.1/templates-parametes.png)

`工具`菜单被重新定义，用于相关JMeter功能的使用，如：
- Function Helper Dialog
- Export transactions for report
- Generate Schematic View
- Import from cURL
- Compile JSR223 Test Elements
- Create a heap dump
- Create a thread dump

![New_Tool_Menu(http://jmeter.apache.org/images/screenshots/changes/5.1/jmeter-new-menu-tools.png)

## 测试计划

可以使用`cURL`来创建测试计划

![Test Plan from cURL](http://jmeter.apache.org/images/screenshots/changes/5.1/http-request-from-curl-request.png)

## 脚本和调试增强

在`工具`菜单中新增用于编译所有`JSR223`的功能

## 实时报告和测试报告 

- 可以使用`-e`或`-g`来生成`JSON`格式的性能统计结果
- 百分比计算的方法已调整为在每次测试时重新计算
- 通过使用参数`-f`，更友好的处理报告在生成时空文件夹或文件夹已存在的处理


## 版本下载


[JMeter5.1](https://github.com/apache/jmeter/releases/tag/v5_1)