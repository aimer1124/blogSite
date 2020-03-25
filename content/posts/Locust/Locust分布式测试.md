---
title: '分布式测试'
tags:
  - Locust
  - 性能测试
  - Python
categories:
  - Translate
date: 2017-06-03 21:30:00
---

## 分布式运行Locust

一旦单台机器不够模拟足够多的用户时，Locust支持运行在多台机器中进行压力测试。

为了实现这个，你应该在`master`模式中使用`--master`标记来启用一个Locust实例。这个实例将会运行你启动测试的Locust交互网站并查看实时统计数据。`master`节点的机器自身不会模拟任何用户。相反，你必须使用`--slave`标记启动一台到多台Locust`slave`机器节点，与标记`--master-host`一起使用(指出`master`机器的`IP/hostname`)。

常用的做法是在一台独立的机器中运行master，在`slave`机器中每个处理器内核运行一个`slave`实例。

** !Note **

** `master`和每一台`slave`机器，在运行分布式测试时都`必须`要有locust的测试文件。**

<!--more-->

### 示例

使用`master`模式启动:

```
locust -f my_loucstfile.py --master
```

在每个`slave`中执行(使用`master`机器的IP替换`192.168.0.14`):

```
locust -f my_locustfile.py --slave --master-host=192.168.0.14
```

### 参数

#### `--master`

设置locust为`master`模式。网页交互会在这台节点机器中运行。

#### `--slave`

设置locust为`slave`模式。

#### `--master-host=X.X.X.X`

可选项，与`--slave`一起结合使用，用于设置`master`模式下的`master`机器的IP/hostname(默认设置为127.0.0.1)

#### `--master-port=5557`

可选项，与`--slave`一起结合使用，用于设置`master`模式下的`master`机器中Locust的端口(默认为5557)。注意，locust将会使用这个指定的端口号，同时指定端口+1的号也会被占用。因此，5557会被使用，Locust将会使用5557和5558。

#### `--master-bind-host`=X.X.X.X`

可选项，与`--master`一起结合使用。决定在master模式下将会绑定什么网络接口。默认设置为*(所有可用的接口)。

#### `--master-bind-port=5557`

可选项，与`--master`一起结合使用。决定哪个网络端口`master`模式将会监听。默认设置为5557。注意Locust会使用指定的端口号，同时指定端口+1的号也会被占用。因此，5557会被使用，Locust将会使用5557和5558。


- 本文[Locust](http://locust.io/)版本`0.7.5`
- 原文地址：[http://docs.locust.io/en/latest/running-locust-distributed.html](http://docs.locust.io/en/latest/running-locust-distributed.html)
