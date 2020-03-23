---
title: '什么是Locust'
tags:
  - Locust
  - 性能测试
  - Python
categories:
  - Translate
date: 2017-06-08 18:30:00
---

- 原文地址：[http://docs.locust.io/en/latest/what-is-locust.html#](http://docs.locust.io/en/latest/what-is-locust.html#)

## 什么是Locust

Locust是一个容易使用、分布式的压力测试工具。它是用于网站压力测试(或其它系统)并找出多少用户一个系统可以承载。

在测试过程中，策略就是一个Locust的蠕虫将会攻击你的网站。每一个locust的行为(或你使用的测试用户)是你自己定义的，并且蠕虫进程从一个网页视图中被实时监测。这样会帮助你来实现测试，在真实用户使用前定义系统的瓶颈。

Locust是完全基于事件的，因此可以在单台机器中支持数以千计的用户在线。和其它基于事件的程序相比较，它是不需要使用回调的。相反，它通过[gevent](http://www.gevent.org/)使用轻量级的进程。每一个locust测试你的网站时，实际上是真实的在内部运行它自己的进程(或greenlet,准确的说)。这样就允许你不使用复杂的回调方法，而是使用Python编写复杂的场景。

<!--more-->

### 特性

- **使用纯Python脚本编写测试场景**

  不需要笨重的UI或臃肿的XML，只需要你平时编写的代码即可。使用协和来代替回调，你的代码看起来更像正常的Python代码块。

- **分布式 & 大量级 - 支持数以千计的用户**

  Locust支持跨多台机器来运行压力测试。当然由于基于事件，一个Locust节点也可以在单进程下支持好几千用户。这背后的原因是即使你模拟了这么多用户，但并不是所有的用户都是活跃在攻击你的系统。通常，用户是空闲的，在等待下一次的动作。`每秒的请求 != 在线用户数`。

- **基于Web的UI**

  Locust有一个整洁的 `HTML + JS` 用户交互界面，用于实时展示对应的测试明细。并且，由于UI是基于Web的，所以它是跨平台并容易扩展的。

- **可测试任何系统**

  即使Locust是面向Web的，但它可用于测试大部分系统。只需要针对你要测试的系统写一个client，再使用Locust来压测它。真的很容易！

- **可改造的**

  Locust是一个非常小巧并可改造的，并且我们计划一直保持这样。所有重量级的事件I/O和协程都被委托给[gevent](http://www.gevent.org/)。容易改造的测试工具是我们创建Locust的初衷。

## 背景

Locust被创建是因为我们要解决已经存在的问题。没有一个对于来说可以解决正确的问题，它们没找到核心点。我们尝试了[JMeter](http://jmeter.apache.org)和[Tsung](http://tsung.erlang-projects.org/)。这两个工具使用起来都很不错；在工作中，我们多次使用了前者来测试基准。[JMeter](http://jmeter.apache.org)。JMeter自带了UI交互，这一秒你可能认识这是一件好事。但你很快就会认识到，这是一个PITA，通过一些点击界面箅编码测试场景。第二，JMeter是基于线程的。这就是所有你想模拟的用户，你需要一个独立的线程。不用说，在一台机器实现几千用户是相当产灵活的。

另一方面，由于是使用Erlang编写的，Tsung没有线程问题。它通过使用BEAM自身来实现轻量级线程，并很容易将量级提升。但，当定义测试场景时，Tsung和JMeter一样被限制了。它提供一个基于XML的动态描述语言来定义，在测试时的用户行为。我猜，你可以想像编码实现它的荣耀。当完成你的post请求并从测试日志中生成日志，展示任何图形排序或报告。接下来你就可以理解测试是怎么运行的。

无论如何，在创建Locust时，我们已经尝试罗列这些问题。希望上面的痛点都不存在。

我猜，你会说我们真的只是罗列了我们的好处。我们希望尽可能的实现一些有用的。

## 作者

- [Jonatan Heyman](http://heyman.info/)([@jonatanheyman](http://twitter.com/jonatanheyman) on Twitter)
- Carl Byström ([@cgbystrom](http://twitter.com/cgbystrom) on Twitter)
- Joakim Hamrén ([@Jahaaja](http://twitter.com/Jahaaja) on Twitter)
- Hugo Heyman ([@hugoheyman](http://twitter.com/hugoheyman) on Twitter)

## 许可证

在MIT许可证下的开源许可(查看许可证明细)
