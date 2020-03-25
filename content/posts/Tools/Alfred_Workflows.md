---
title: 'Alfred中的Workflow配制'
date: 2020-01-11 12:00:00
tags:
  - Alfred
  - Workflow
categories:
  - Tool
---

## 是什么

### Alfred

[https://www.alfredapp.com/](https://www.alfredapp.com/)

- 官方定义：
```markdown
Alfred is an award-winning app for macOS which boosts your efficiency with hotkeys, keywords, text expansion and more. Search your Mac and the web, and be more productive with custom actions to control your Mac.
```

- 自己理解

通过`定制化`的方法，`提高`使用`macOS` `效率`的工具。

补充：
Alfred提供了Powerpack的`收费`功能，用于`深度`定制。
建议购买`Powerpack`。

### Workflows

Workflows是用于定制Alfred与操作系统交互，可将一个或多个`流程性`/`重复性`的操作定制为Workflow。如每天上班后，打开IDEA、邮件等。

## 第一个Workflow

**需求：一个命令打开IntelliJ和GMail邮件**

### 初版

- 定义从热键启动Workflow

![OpenIntelliJ](/img/Alfred/OpenIntelliJ.png)
![Workflow](/img/Alfred/Workflow.png)
![Keyword](/img/Alfred/Keyword.png)

- 启动IntelliJ

![OpenAPP](/img/Alfred/OpenAPP.png)
![AddIntelliJ](/img/Alfred/AddIntelliJ.png)
![IntelliJDone](/img/Alfred/IntelliJDone.png)

- 使用默认浏览器打开GMail

![OpenURL](/img/Alfred/OpenURL.png)
![SetGMailURL](/img/Alfred/SetGMailURL.png)


以上步骤，已完成一个基础功能的Workflow配制。
![WorkflowDone](/img/Alfred/WorkflowDone.png)

- 测试

![TestWorkflow](/img/Alfred/TestWorkflow.png)

输入`morning`回车后，会先打开`IntelliJ`再使用默认浏览器打开GMail。

### 进阶版

回顾`初版`的功能，发现还有一些不足之处。

- 能否打开IntelliJ的同时也打开GMail，`减少`等待时间
- 能否打开IntelliJ的时候，打开`指定`的项目

#### 解决第一个问题：能否打开IntelliJ的同时也打开GMail，`减少`等待时间

- 取消打开IntelliJ后再打开GMail的关联性，选择IntelliJ和GMail中间的连接线(选取-->删除，即可)
- 设置输入Keyword和GMail的关联性，鼠标悬浮在Keyword后的连接线处，拖动后会出现连接线，选择GMail即可

![OpenIntelliJAndGMail](/img/Alfred/OpenIntelliJAndGMail.png)


#### 解决第一个问题：能否打开IntelliJ的时候，打开`指定`的项目

- 设置IntelliJ为支持命令行启动,`/usr/local/bin/idea`

![CreateCommandLineLauncher](/img/Alfred/CreateCommandLineLauncher.png)

- 替换Workflow中IntelliJ的启动为命令行启动

![ReplaceWithRunScript](/img/Alfred/ReplaceWithRunScript.png)

```shell script
projectPath=/Users/yuanjie/Downloads/aimer1124.github.io

/usr/local/bin/idea  $projectPath
```

`projectPath`为`指定`项目地址

---

至此，两个问题都已解决

![FixTwoUpgrade](/img/Alfred/FixTwoUpgrade.png)

导出的Workflow地址：[https://github.com/aimer1124/workflow_alfred](https://github.com/aimer1124/workflow_alfred)

我创建的Workflow: [https://github.com/aimer1124/workflow_alfred](https://github.com/aimer1124/workflow_alfred)

## 参考

- [https://www.alfredapp.com/](https://www.alfredapp.com/)
- [https://www.alfredapp.com/help/workflows/](https://www.alfredapp.com/help/workflows/)
- [https://github.com/bchatard/jetbrains-alfred-workflow](https://github.com/bchatard/jetbrains-alfred-workflow)