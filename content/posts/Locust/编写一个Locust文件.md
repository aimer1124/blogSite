---
title: '编写一个Locust文件'
tags:
  - Locust
  - 性能测试
  - Python
categories:
  - Translate
date: 2017-06-02 21:30:00
---

Locust文件就是一般的Python文件。唯一的需求就是它至少需要一个继承于`Locust`的类.

## Locust类

Locust类代表一个用户(如果愿意，也可以是一个准备出动的蝗虫)。Locust会为每一个模拟用户生成一个locust类实例。同时会有一些locust类属性被定义。

### `task_set`属性

`task_set`属性是指向一个定义用户行为的`TaskSet`类，下面会有详细的介绍。

### `min_wait`和`max_wait`属性

除了`task_set`属性，另外一个经常被使用的就是`min_wait`和`max_wait`属性。是用于各自以毫秒为单位的最小值和最大值，一个模拟用户将会在每个任务执行时的等待执行的时间间隔。`min_wait`和`max_wait`默认设置为`1000`，如果不声明的话，Locust会默认在每个任务间等待`1秒`。

参考下面的代码，每个用户将会在每个任务间等待`5至15`秒:

```
from locust import Locust, TaskSet, task_set

class MyTaskSet(TaskSet):
    @task
    def my_task(self):
        print "executing my_task"

class MyLocust(Locust):
    task_set = MyTaskSet
    min_wait = 5000
    max_wait = 15000
```

`min_wait`和`max_wait`属性可以用于重写`TaskSet`类。

<!--more-->

### `weight`属性

你可以通过同一个文件来运行两个locust，就像这样:

```
locust -f locust_file.py WebUserLocust MobileUserLocust
```

如果你更倾向于用这种方法来运行，便可以在这些类中尝试`weight`属性。比如，就像这样来定义web用户比Mobile用户多`3倍`：

```
class WebUserLocust(Locust):
    weight = 3
    ...

class MobileUserLocust(Locust):
    weight = 1
    ...
```

### `host`属性

`host`属性是到要加载目标`URL`的前缀(如:"[http://google.com](http://google.com)")。通常情况下，当Locust被启动时，在命令行中是需要通过`--host`来指定的。如果`host`属性在locustfile文件中被声明，则在命令行中则不需要使用`--host`属性来再次声明。

## `TaskSet`类

如果Locust类代表一只准备出动的蝗虫，那么你可以说`TaskSet`类代表蝗虫的大脑。每一个Locust类中必须要包含一个指向`TaskSet`的`task_set`属性设置。

`TaskSet`就像它的名字一样，是一个任务集合。这些任务是常规的Python调用,如果我们压力测试一个拍卖网站，便可以做这些操作`加载启动页面`、`搜索一些产品`、`竞标`。

当一个压力测试被启动时，每一个准备的Locust类实例将会开始执行它们的`TaskSet`。接下来是每一个`TaskSet`找到它的`task`并调用它。它将在`min_wait`和`max_wait`属性值之间随机等待几毫秒(除非`min_wait`和`max_wait`被定义在TaskSet中，在这种情况下将会使用TaskSet设置的值)。然后，它将会找到一个新`task`并调用，再次等待，一直这样持续下去。

### 声明task

对于`TaskSet`来说，典型的声明`task`的方法是直接使用`task`。

参考这个例子:

```
from locust import Locust, TaskSet, task
class MyTaskSet(TaskSet):
    @task
    def my_task(self):
        print "Locust instance (%r) executing my_task" % (self.locust)

class MyLocust(Locust):
    task_set = MyTaskSet
```

**@task** 将会获取一个可选的权重参数，用于说明任务执行的比率。在下面的例子中 _task2_ 将会比 _task1_ 执行的次数多两倍:

```
from locust import Locust, TaskSet, task
class MyTaskSet(TaskSet):
    min_wait = 5000
    max_wait = 15000

    @task(3)
    def task1(self):
        pass

    @task(6)
    def task2(self):
        password

class MyLocust(Locust):
    task_set = MyTaskSet

```

### `task`属性

使用`@task`操作符来声明task是一种便捷的方法，并且经常是最好的方式。然而，也可以定义`TaskSet`中的task通过设置tasks属性(使用操作符@task比tasks属性更流行)。

_tasks_ 属性不是python列表的调用就是一个<callbale:int>字典。tasks是python调用接收执行task的TaskSet类实例参数。下面是一个极其简单的示例(不会影响任何测试):

```
from locust import Locust, TaskSet

def my_task(l):
    pass

class MyTaskSet(TaskSet):
    tasks = [my_task]

class MyLocust(Locust):
    task_set = MyTaskSet
```

如果task属性被定义在列表中，每次任务被执行时，将会`随机`从 _tasks_ 属性中选择。如果 _tasks_ 是一个带有关健字和数值调用的字典，被执行的任务将会被随机选择以数字的比率来执行。就像下面的这样:

```
{my_task: 3, another_task:1}
```

__my_task__ 将会比 __another_task__ 多执行三倍。

### `TaskSet`可以嵌套

`TaskSet`有一个重要的属性就是可以被嵌套，由于真实的网站是有一定的业务层级结构的，并带有一些子模块。嵌套的TaskSet将会帮助我们来定义更加真实的用户行为。比如，我们可以定义`TaskSet`像下面的结构

- Main user behaviour
  - Index page
  - Forum page
    - Read thread
      - Reply
    - New thread
    - View next page
  - Browser categories
    - Watch movies
    - Filter movies
  - About page

嵌套TaskSet的方法就像使用`task`属性来说明task一样，但代替参考Python函数，你可以参考下面的`TaskSet`:

```
class ForumPage(TaskSet):
    @task(20)
    def read_thread(self):
        pass

    @task(1)
    def new_thread(self):
        pass

    @task(5)
    def stop(self):
        self.interrupt()

class UserBehaviour(TaskSet):
    tasks = {ForumPage:10}

    @task
    def index(self):
        pass
```

在上面的示例中，当UserBehaviour的TaskSet执行时，ForumPage会被选中来执行，接下来ForumPage的TaskSet将会开始执行。ForumPage的TaskSet会找到它的tasks并执行它，再等待，一直这样持续下去。

针对上面的例子中有一个重要的事情要注意，就是在ForumPage页面中的Stop方法中调用`self.interrupt()`。这个做的事情是停止执行ForumPage任务并在UserBehaviour实例中继续执行。如果在ForumPage中，我们没有调用`interrupt()`方法，除非被调用否则Locust不会调用ForumPage任务。但通过`interrupt`函数 ，我们可以结合`weight`任务来定义模拟用户离开Forum.

也可以在类内部声明嵌套TaskSet,通过使用`@task`操作符，像声明正常的task一样：

```
class MyTaskSet(TaskSet):
    @task
    class SubTaskSet(TaskSet):
        @task
        def my_task(self):
            pass
```

### `on_start`函数

TaskSet可以选择声明`on_start`函数。如果这样的话，当模拟用户开始执行TaskSet类时，函数被调用。

### 关联`Locust`实例，或父`TaskSet`实例

`TaskSet`实例有`locust`属性来指向它的`Locust`实例，属性`parent`用来指向它的父`TaskSet`（它会指向Locsut实例，在基类TaskSet中）。

## `HTTP`请求

到现在为止，我们仅覆盖了一个Locsut用户的部分任务计划。为了真实的压力测试一个系统时，我们需要生成`HTTP`请求。为了帮助我们实现这个功能，可以使用`HttpLocust`类。当使用这个类时，每一个实例将会获得一个用于生成`Http`请求的`HttpSession`实例的`client`属性。

```
class HttpLocust
```

表示一个用于压力测试的孵化和攻击系统的`HTTP` `用户`。

这个用户的行为通过`task_set`属性来定义，直接指向`TaskSet`类。

这个类创建一个`client`属性，在初始化时，`HTTP`客户端支持为每一个用户在请求间保存session。

```
   client=None
```

HttpSession实例在Locust初始化时被创建。`client`支持`cookies`，同时在请求间会保存session。

当从`HttpLocust`类继承时，我们可以使用`client`属性来对服务器生成`HTTP`请求。下面是一个locust文件示例用于在一个网站的两个URL **/** 和 **/about/** 。

```
from locust import HttpLocust, TaskSet, task

class MyTaskSet(TaskSet):
    @task(2)
    def index(self):
        self.client.get('/')

    @task(1)
    def about(self):
        self.client.get('/about/')
class MyLocust(HttpLocust):
    task_set = MyTaskSet
    min_wait = 5000
    max_wait = 15000
```

使用上面的Locust类，每一个模拟用户将间隔5-15秒内请求，并且`/`将会比`/about/`请求数量多`2倍`。

细心的读者会发现有一些奇怪，我们使用`self.client`关联`HttpSession`实例，而不是`TaskSet`,也不是`self.locust.client`。我们可以这样做，是因为`TaskSet`类有一个属性调用`client`简单的返回`self.locust.client`。

### 使用`HTTP client`

每一个`HttpLocust`实例在`client`属性中有一个`HttpSession`实例。`HttpSession`类实际上是`requests.Session`的子类，可使用`get` `post` `put` `delete` `head` `patch` 和 `options`方法来生成`HTTP`请求，用于Locust的数据统计。`HttpSession`实例在请求间维护cookies，因此可用于登录网站并保存session在请求之间。`client`可以通过Locust实例的TaskSet实例来关联，因此很容易获取client并在任务中生成HTTP请求。

下面是一个生成`GET`请求到 _/about_ 路径的示例(在这里，我们可以假设 _self_ 是一个`TaskSet` 或 `HttpLocust` 类的实例):

```
response = self.client.get("/about")
print "Response staus code:", response.status_code
print "Response content:", response.content
```

下面是一个生成`POST`请求的示例:

```
response = self.client.post("/login", {"username": "testuser", "password": "password"})
```

### 安全模式

`HTTP` client被配制运行在`safe_mode`。这样做是任何请求在连接超时、错误、相似失败时将不会抛出异常，而是返回一个空的假Response对象。请求将会在Locust统计中算做一次失败。返回假Response内容属性将会被设置为None，并且它的status_code将会是0.

### 手动设置请求是成功或失败

默认情况下，请求被标记为失败除非在返回状态码是OK(2XX)。大部分时间内，这个默认就是你所需要的。然而，比如在测试一个URL节点，你期待返回状态码为404，或者测试一个即使错误发生也会返回200的系统，因此，需要手工控制locust来判断是成功还是失败。

一个可以生成失败请求，即使当响应代码是`OK`，通过使用`catch_response`参数和`with`语法:

```
with client.get("/", catch_response = True) as response:
    if response.content != "Success":
        response.failure("Got wrong response")
```

就像一个可以使用响应为`OK`的请求当做失败来处理，一个方法就是可以使用`catch_response`参数和`with`语法来让请求HTTP错误时，仍然统计数据为成功:

```
with client.get("/does_not_exist/", catch_response = True) as response:
    if response.status_code = 404:
        response.success()
```

### 使用动态参数来分组URL请求

针对网站，有一个常用的功能是获取URL中包含一些动态参数的页面数据。通常情况下，在Locust统计中，使用动态分组在URL中是很有意义的。通过`name`参数来给`HttpSession`传递不同的请求方法。

比如:

```
# Statistics for these requests will be grouped under: /blog/?id=[id]
for i in range(10):
  client.get("/blog?id=%i" % i, name = "/blog?id=[id]")
```

### 常用库

通常，大家想分享多个locust文件用于分享常用的库。在这种情况下，定义`项目根目录`用于调用Locsut是很重要的，建议将所有的locust文件有些话在项目的根目录中。

一个平铺的结构像下面这样:

- 项目根目录
  - `commonlib_conf.py`
  - `commonlib_auth.py`
  - `locustfile_web_app.py`
  - `locsutfile_api.py`
  - `locustfile_ecommerce.py`

locust文件可以调用常用的库通过使用`import commonlib_auth`.然而，这种方法不会从locust文件中，清晰分辨出常用库。

子文件夹可以有一个清晰的方法(查看下面的示例)，但是locust仅会有运行locsut文件的位置引用相关的模块。如果你想从你的根目录导入(如，你运行locust命令的位置)，确保在任何locust文件中添加常用库前有代码`sys.path.append(os.getcwd())`，会生成导入根目录(如，当前工作目录)。

- project root
  - `__init__.py`
  - `common/`
    - `__init__.py`
    - `config.py`
    - `auth.py`
  - `locustfiles/`
    - `__init__.py`
    - `web_app.py`
    - `api.py`
    - `ecommerce.py`

使用上面的项目结构，你的locust文件可以通过下面代码导入常用的库:

```
sys.path.append(os.getcwd())
import common.auth
```  

- 本文[Locust](http://locust.io/)版本`0.7.5`
- 原文地址：[http://docs.locust.io/en/latest/writing-a-locustfile.html](http://docs.locust.io/en/latest/writing-a-locustfile.html)
