---
title: 'Locust快速入门'
tags:
  - Locust
  - 性能测试
  - Python
categories:
  - Translate
date: 2017-05-24 18:20:00
---

```
Locust，基于Python的性能测试工具。
```

- [什么是Locust](http://docs.locust.io/en/latest/what-is-locust.html)
- 本文[Locust](http://locust.io/)版本`0.7.5`
- 原文地址：[http://docs.locust.io/en/latest/quickstart.html#](http://docs.locust.io/en/latest/quickstart.html#)


## 示例`locustfile.py`

下面是一个简单的`locustfile.py`小示例:

```
from locust import HttpLocust, TaskSet

def login(l):
    l.client.post("/login", {"username":"ellen_key", "password":"education"})

def index(l):
    l.client.get("/")

def profile(l):
    l.client.get("/profile")

class UserBehavior(TaskSet):
    tasks = {index: 2, profile: 1}

    def on_start(self):
        login(self)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
```

<!--more-->

这里我们定义了一些带一个参数(`Locust`类实例)正常Python执行的Locust任务。这些任务在`task`属性中 `TaskSet`类被聚集。接下来，我们有一个代表一个用户的`HttpLocust`类，这里我们定义多久一个模拟用户应该等待在执行任务之间，同时`TaskSet`类应该定义用户`行为`.python类`TaskSet <locust.core.TaskSet>`可以被嵌入。

`HttpLocust`类从`Locust`类中继承，它有一个用于发送HTTP请求的`HttpSession`属性在客户端属性中。

另外一种方式，我们可以使用另外一种更简洁的方法声明任务，就是使用`@task`声明。下面的代码和上面的代码一致：

```
from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    def login(self):
        self.client.post("/login", {"username":"ellen_key", "password":"education"})

    @task(2)
    def index(self):
        self.client.get("/")

    @task(1)
    def profile(self):
        self.client.get("/profile")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
```

`Locust`类(在子类中也叫`HttpLocust`类)可以指定针对每一个模拟用户在执行任务之间设置最小和最大的等待时间(min_wait和max_wait)，像用户行为一样。

## 启动Locust

为了运行上面的Locust文件，如果文件被命名为`locustfile.py`并保存在当前目录，我们可以直接运行:

```
locust --host=http://example.com
```

如果Locust文件在子文件夹或命名与`locustfile.py`不一致时，可以通过参数`-f`:

```
locust -f locust_files/my_locust_file.py --host=http://example.com
```

运行Locust的分布式多线程，我们应该启动master通过参数`--master`:

```
locust -f locust_files/my_locust_file.py --master --host=http://example.com
```

接下来我们可以启动slave线程:
```
locust -f locust_files/my_locust_file.py --slave --host=http://example.com
```

如果我们想运行Locust在多台机器，在启动slaves时，我们应该指定master地址(这不是必须的，当运行Locust分布式在同一台机器时，master的默认地址是127.0.0.1):

```
locust -f locust_files/my_locust_file.py --slave --master-host=192.168.0.100 --host=http://example.com
```

查看所有的选项，输入:

```
locust  --help
```

## 打开Locust的Web界面

一旦你通过上面的命令启动了Locust，你应该打开浏览器并输入[http://127.0.0.1:8089](http://127.0.0.1:8089)(如果你是在本机运行的Locust)。接下来，你应该可以看到下面的页面:

![UI](http://docs.locust.io/en/latest/_images/webui-splash-screenshot.png)
