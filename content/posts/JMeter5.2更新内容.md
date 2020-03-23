---
title: 'JMeter5.2更新内容'
tags:
  - JMeter
  - 性能测试
categories:
  - Translate
date: 2020-01-08 15:30:00
---

```
版本发布时间于20191008，本次版本基本没有什么更新，主要是切换版本号。
```

## 主要内容

本次为版本发布，更新内容参考5.1.1

## 提升

- HTTP(S) Test Script Recorder 会在名字后追加数字显示，参考[Bug 64350](https://bz.apache.org/bugzilla/show_bug.cgi?id=63450)
- 修复：当在XPath表达式中使用XPath Assertion返回Boolean值时，True if nothing matches没有生效并返回值为True。参考[Bug 63455](https://bz.apache.org/bugzilla/show_bug.cgi?id=63455)
- XML现在拒绝不安全的XMl内容，会影响
    - XMLAssertion
    - XMLSchemAssertion
    - XPath function
    - XPath 1 & 2 Extractors
    - XPath 1 & 2 Assertions

## 版本下载

[JMeter5.2](https://github.com/apache/jmeter/archive/v5.2-rc1.zip)