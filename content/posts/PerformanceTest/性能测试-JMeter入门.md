---
title: '性能测试-JMeter入门手册'
tags:
  - JMeter
  - 性能测试
categories:
  - Mark
date: 2017-02-28 16:15:00
---


[原文地址](http://shiyuanjie.cn/jmeter-tutorial/)

---

# 本文目的  [![Build Status](https://travis-ci.org/aimer1124/jmeter-tutorial.svg?branch=JMeter5.0)](https://travis-ci.org/aimer1124/jmeter-tutorial) 

- 面向新手，学习后可以使用[JMeter](http://jmeter.apache.org/)**独立**完成项目的性能测试
- 快速分析并使用[JMeter](http://jmeter.apache.org/)定位出项目**性能测试结果**
- 产出**有价值**的性能测试报告

# 目录

- [简介](http://shiyuanjie.cn/jmeter-tutorial/)

- [认识JMeter](http://shiyuanjie.cn/jmeter-tutorial/chapter1)
  - [了解并启动JMeter](chapter1http://shiyuanjie.cn/jmeter-tutorial/chapter1/了解并启动JMeter.html)
  - [认识JMeter](http://shiyuanjie.cn/jmeter-tutorial/chapter1/认识JMeter.html)
  - [第一个测试](http://shiyuanjie.cn/jmeter-tutorial/chapter1/第一个测试.html)

- [提高JMeter](http://shiyuanjie.cn/jmeter-tutorial/chapter2)

  - [线程高并发](http://shiyuanjie.cn/jmeter-tutorial/chapter2/线程高并发.html)
  - [逻辑控件器](http://shiyuanjie.cn/jmeter-tutorial/chapter2/逻辑控件器.html)
  - [断言测试](http://shiyuanjie.cn/jmeter-tutorial/chapter2/断言测试.html)
  - [结果分析](http://shiyuanjie.cn/jmeter-tutorial/chapter2/结果分析.html)

- [完善JMeter](http://shiyuanjie.cn/jmeter-tutorial/chapter3)
  - [HTTP信息头管理](http://shiyuanjie.cn/jmeter-tutorial/chapter3/HTTP信息头管理.html)
  - [数据获取](http://shiyuanjie.cn/jmeter-tutorial/chapter3/数据获取.html)
  - [实战性能测试](http://shiyuanjie.cn/jmeter-tutorial/chapter3/实战性能测试.html)

- [分析测试](http://shiyuanjie.cn/jmeter-tutorial/chapter4)

  - [断言结果详细分析](http://shiyuanjie.cn/jmeter-tutorial/chapter4/断言结果详细分析.html)
  - [结果详细分析](http://shiyuanjie.cn/jmeter-tutorial/chapter4/结果详细分析.html)
  - [服务器分析](http://shiyuanjie.cn/jmeter-tutorial/chapter4/服务器分析.html)
  - [扩展插件](http://shiyuanjie.cn/jmeter-tutorial/chapter4/扩展插件.html)

- [进阶使用](http://shiyuanjie.cn/jmeter-tutorial/chapter5)

  - [命令行执行JMeter](http://shiyuanjie.cn/jmeter-tutorial/chapter5/命令行执行JMeter.html)
  - [性能测试常用专业述语](http://shiyuanjie.cn/jmeter-tutorial/chapter5/性能测试常用专业述语.html)
  - [JMeter最佳实践](http://shiyuanjie.cn/jmeter-tutorial/chapter5/JMeter官方最佳实践.html)
  - [性能测试最佳实践](http://shiyuanjie.cn/jmeter-tutorial/chapter5/性能测试最佳实践.html)
  - [测试报告](http://shiyuanjie.cn/jmeter-tutorial/chapter5/测试报告.html)

- [结束语](http://shiyuanjie.cn/jmeter-tutorial/end)

# 说明

- 基础环境信息：
    - OS:macOS Mojave 10.14.2
    - JDK:11.0.1
    - JMeter：5.0
- QQ交流群：**478527666**
- 文中关于[JMeter](http://jmeter.apache.org/)的功能，不会很详尽，**够用足以**
- 源GitBook地址:[https://aimer1124.gitbooks.io/jmeter-tutorial/content/](https://aimer1124.gitbooks.io/jmeter-tutorial/content/)，停止更新