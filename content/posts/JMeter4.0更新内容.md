---
title: 'JMeter4.0更新内容'
tags:
  - JMeter
  - 性能测试
categories:
  - Translate
date: 2018-02-28 15:20:00
---

```
等了这么久，20180210，终于有较大的更新。无论是从 UI 还是功能优化，都让人耳目一新。下面我们就详细看下具体变化。
```

原文地址：[http://jmeter.apache.org/changes.html](http://jmeter.apache.org/changes.html)
下载地址：[apache-jmeter-4.0.zip](http://ftp.cuhk.edu.hk/pub/packages/apache.org//jmeter/binaries/apache-jmeter-4.0.zip)

## 重要更新

### 主要变更

JMeter 现在支持 JAVA 9.

新的[Boundary Extractor](http://jmeter.apache.org/usermanual/component_reference.html#Boundary_Extractor)元素可以提供更好的元素提取性能

![](http://jmeter.apache.org/images/screenshots/changes/4.0/boundary_extractor.png)

新的[JSON Assertion](http://jmeter.apache.org/usermanual/component_reference.html#JSON_Assertion)元素可用于 JSON 响应的断言。

![](http://jmeter.apache.org/images/screenshots/changes/4.0/json_assertion.png)

JMS Point-to-Point 样例增加了**read,browser,clear**选项。

![](http://jmeter.apache.org/images/screenshots/changes/4.0/jmsptp_communication_styles.png)

<!--more-->

将许多测试元素的最佳选项已设置为默认选中内容，如：

- 新增**If Controller**控制器使用最佳性能选择的默认表达式。

![](http://jmeter.apache.org/images/screenshots/changes/4.0/if_controller_condition.png)

![](http://jmeter.apache.org/images/screenshots/changes/4.0/if_controller_expression.png)

- 新增JSR223测试元素，在语言使用支持的情况下，默认缓存编写的脚本。

[Loop controller](http://jmeter.apache.org/usermanual/component_reference.html#Loop_Controller)和[ForEach Controller](http://jmeter.apache.org/usermanual/component_reference.html#ForEach_Controller)会使用 `__jm__<Name of your element>__idx`来暴露循环的遍历次数，可以像下面的方式来使用一个名为 MyLoopController 的 Loop Controller：

`${__jm__MyLoopController__idx}`	

详见[Bug 61802](https://bz.apache.org/bugzilla/show_bug.cgi?id=61802).

Cookies 在录制过程中，会展示在**View Results Tree**中。之前他们总是显示为空。

[Response Assertion](http://jmeter.apache.org/usermanual/component_reference.html#Response_Assertion)允许定制断言信息和请求数据。

![](http://jmeter.apache.org/images/screenshots/changes/4.0/response_assertion_enhancements.png)

### UX 提升

JMeter 现在默认使用[Darcula LAF](https://github.com/bulenkov/Darcula)UI样式。

Wokbench 已经被从 UI 中去掉，你可以使用**Test Plan**中**Non Test Elements**的子元素来添加对应 Workbench 中的功能。

![](http://jmeter.apache.org/images/screenshots/changes/4.0/goodbye_workbench.png)

菜单样式将最常用元素调整为快速进行操作。

![](http://jmeter.apache.org/images/screenshots/changes/4.0/menu_organization.png)

**HTTP(S) Test Script Recorder** 允许在录制时，定制更加人性化的 **transactions**的名称。

![](http://jmeter.apache.org/images/screenshots/changes/4.0/recorder_naming_samplers.png)

UX样式还有以下提升：

- `Module Controller `会提示用户最少需要有一个`Controller`。
- `Function Helper Dialog`(帮助使用和测试功能的说明)在多个位置有提升。

![](http://jmeter.apache.org/images/screenshots/changes/4.0/function_helper_dialog_enhancements.png)

- `Swich Controller`会自动`trim`字符串前后的空格，减少问题出现。
- `Test Plan`在运行前会保存。

### 函数

新函数 [__digest](http://jmeter.apache.org/usermanual/functions.html#__digest) 用户快速提升 SHA-XXX，MDX Hash 计算：
```
${__digest(MD5,Apache JMeter 4.0 rocks !,,,)}
```
返回**0e16c3ce9b6c9971c69ad685fd875d2b**


新函数 [__dateTimeConvert](http://jmeter.apache.org/usermanual/functions.html#__dateTimeConvert) 提供两种时间格式的快速转换：
```
${__dateTimeConvert(01 Jan 2017,dd MMM yyyy,dd/MM/yyyy,)}
```
返回**01/01/2017**


新函数 [changeCase](http://jmeter.apache.org/usermanual/functions.html#__changeCase)提供字符在大写、小写、驼峰式之间的转换：
```
${__changeCase(Avaro omnia desunt\, inopi pauca\, sapienti nihil,UPPER,)}
```
返回**AVARO OMNIA DESUNT, INOPI PAUCA, SAPIENTI NIHIL**


新函数[__isVarDefined](http://jmeter.apache.org/usermanual/functions.html#__isVarDefined)和 [__isPropDefined](http://jmeter.apache.org/usermanual/functions.html#__isPropDefined) 用于测试属性和变量是否可用。
```
${__isPropDefined(START.HMS)}
```
返回 **true**
```
${__isVarDefined(JMeterThread.last_sample_ok)}
```
返回 **true**


### 编码和插件开发

如果你不想样例在测试结果中出现，可以调用**SampleResult#setIgnore()**。

**JavaSamplerContext** 替代在**AbstractJavaSamplerClient**，有新的方法用于快速的插件开发。

JMeter 现在发布 Maven 源和 JavaDoc在[Maven repository](https://repo1.maven.org/maven2/org/apache/jmeter/ApacheJMeter_core/4.0/)中。

插件可以注册监听事件，当收到 TestPlan 的开启/关闭状态通知时。

### 实时报告和 Web 报告

**InfluxDB backend listener**支持通过使用**TAG_**来定制化 tags，详见[Bug 61794](https://bz.apache.org/bugzilla/show_bug.cgi?id=61794).

在 Web 报告中 **responseTime**分布图更加精细。

一些 BUG 修复也被集成在报告模块中，详见[Bug 61900](https://bz.apache.org/bugzilla/show_bug.cgi?id=61900)，[Bug 61956](https://bz.apache.org/bugzilla/show_bug.cgi?id=61956)，[Bug 61899](https://bz.apache.org/bugzilla/show_bug.cgi?id=61899)。图表中 **Latency Vs Request** 和 **Response Time Vs Request** 不会超过1000RPS，详见[Bug 61962](https://bz.apache.org/bugzilla/show_bug.cgi?id=61962)。

### JMeter 环境配制

JMeter 的启动脚本用于 JVM设置的被放在了单独的文件中(Unix 中是**bin/setenv.sh**，Windows 中是**bin\setenv.bat**)，在启动时会被调用。这样，启动脚本再也不用编辑了。

### 优化调整

- 线程组的**Start time** 和 **End date**被移除，详见[Bug 61549](https://bz.apache.org/bugzilla/show_bug.cgi?id=61549)
- 分布式测试中，**Hold**模式被删除。使用其它替代和更有效的模式
- 针对第三方插件，方法**org.apache.jmeter.gui.tree.JMeterTreeNode**为合并至 Java9已被废弃([Bug 61529](https://bz.apache.org/bugzilla/show_bug.cgi?id=61529))

```
public Enumeration<JMeterTreeNode> children()
```

- **tearDown Thread Group** 在默认情况下，会停止并关闭测试。如果你不想这样做，去掉 **Test Plan**中的**Run tearDown Thread Groups after shutdown of main threads on Test Plan**勾选。详见[Bug 61656](https://bz.apache.org/bugzilla/show_bug.cgi?id=61656)
- **sampleresult.getbytes.headers_size**属性和**sampleresult.getbytes.body_real_size**属性被废弃。详见[Bug 61587](https://bz.apache.org/bugzilla/show_bug.cgi?id=61587)
- JMeter 现在会在每次运行时保存测试计划，这个行为可以通过**save_automatically_before_run**来设置。详见[Bug 61731](https://bz.apache.org/bugzilla/show_bug.cgi?id=61731)
- **Workbench**元素被废弃，你可以直接添加**Test Plan** 中 **Non Test Element**的子元素来直接添加。当加载一个包含这种元素的 **Test Plan**时，JMeter 会增加将**Mirror Server, Property Display ** 和 **HTTP(s) Test Script Recorder**添加为直接子元素。对于任何元素，它会创建一个 **Test Fragment**元素，调用 **Workbench Test Fragment 并将元素移入**。
- 下面的类被废弃(**org.apache.jmeter.functions.util.ArgumentEncoder, org.apache.jmeter.functions.util.ArgumentDecoder**)，详见[Pull request #335](https://github.com/apache/jmeter/pull/335)
- 在**JMS Point-to-Point**样例中，设置超时为0时，表示无穷大的时间。未设置时，表示超时为2000ms。详见[Bug 61829](https://bz.apache.org/bugzilla/show_bug.cgi?id=61829)
- 当断言用于不同的范围时，它们会被从最外围一个至最内部的一个。详见[Bug 61846](https://bz.apache.org/bugzilla/show_bug.cgi?id=61846)
- JMeter 现在默认启动语言为英语。这是因为缺少很多种类的语言翻译支持。可以通过修改 jmeter 和 jmeter.bat(或最好用 setenv.sh/setenv.bat)中的**JVM_ARGS**系统设置来调整。我们也很高兴，如果你能贡献支持语言的翻译工作。
- **Switch Controller**现在默认会 trim掉无用的空格，减少问题出现。详见[Bug 61771](https://bz.apache.org/bugzilla/show_bug.cgi?id=61771)
- JMeter JVM 堆设置从**-Xms512m -Xmx512m**调整为**-Xms1g -Xmx1g**。