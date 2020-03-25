---
title: 'Android UI自动化测试神器-Espresso录制'
tags:
  - Espresso
  - E2E
  - Android
categories:
  - Tool
date: 2016-11-25 13:46:00
---

Espresso Test Recorder的好处
- 直接录制与APP的所有交互操作
- 支持在录制过程中添加断言
- 可直接生成`可回放`的测试脚本，基本不需要做任何修改


原文地址: [Create UI Tests with Espresso Test Recorder](https://developer.android.com/studio/test/espresso-test-recorder.html)，以下为正文

---

 > 注意: Espresso Test Recorder在AndroidStudio 2.2 Beta版本之后才有。

 Espresso Test Recorder可以在不写一行代码的情况下创建UI测试。通过录制一个测试场景，你可以记录设备的交互并在APP的部分快照中添加断言来验证元素。Espresso Test Recorder会保存录制并自动生成对应的UI测试，并可直接运行来测试你的APP。

 Espresso Test Recorder编写的测试基于[Espresso Testing framework](https://google.github.io/android-testing-support-library/docs/espresso/)，API在[Android Testing Support Library](https://developer.android.com/topic/libraries/testing-support-library/index.html)。Espresso API鼓励你创建基于用户操作的简洁且可信赖的UI测试。通过使用expectations、interactions和assertions而不是底层APP的Activity和Views，这样的结构防止了测试的脆弱性并优化测试运行速度。

<!--more-->

 查看下面的视频可对Espresso Test Recorder有一个快速的了解，一个新的特性在AndroidStudio2.2:

 <iframe
	height=498 width=510
	src="https://storage.googleapis.com/androiddevelopers/videos/studio/espresso-test-recorder-overview_v2.mp4"
	frameborder=0 allowfullscreen>
</iframe>


## 关闭你设备中的动画
在使用Espresso Test Recorder之前，确保你关闭你设备中的动画以防止出现非预期的结果。依据"安装Espresso"说中在[测试UI在单个APP中](https://developer.android.com/training/testing/ui-testing/espresso-testing.html#setup)中，但是记得你不需要手工设置依赖相关配制到Espresso库中，因为Test Recorder会自动帮你做，当你录制的时候。这些步骤只需要在一个已有的项目中做一次。

## 录制一个Espresso测试
Espresso测试由两个主要部分组成: 在View元素中的UI交互和断言。UI交互包括一个人可以用来与你APP交互的点击和输入动作。断言验证在屏幕中的可见元素的存在或内容。比如，针对[Notes testing app](https://github.com/googlecodelabs/android-testing)的一个Espresso测试，包括UI交互针对点击一个按钮和写一个新的笔记，但使用断言来验证按钮的存在和笔记内容。

## 录制UI交互
为了开始录制一个Espresso Test Recorder，参考下面的步骤

1. 点击 __Run > Record Espresso Test__。
2. 在 __Select Deployment Target__ 窗口中，选择你想要录制的测试的设备。如果有必要，[创建一个新安卓虚拟设备](https://developer.android.com/studio/run/managing-avds.html)。点击 __OK__。
3. Espresso Test Recorder会激活构建你的项目，APP一定要在Espresso Test Recorder允许你交互之前，安装且启动。在APP启动之后，__Record Your Test__ 窗口会显示，如果你还没有跟设备交互，主面板会显示"No event recorded yet." 与你的设备开始交互来启动记录事件，比如"点击"和"输入"动作。

>注意:在你开始记录交互操作之前，在设备中你也许会看到一个对话框显示"Waiting for Debugger"或"Attaching Debugger"。Espresso Test Recorder使用debugger来记录UI事件。当debugger被attach，对话框将会自动关闭，不要点击 __Force Close__.

录制的交互将会显示在主面板中的 __Record Your Test__ ，像下图1显示。当你开始运行测试，Espresso测试执行这些测试按相同的次序。

![图1](https://developer.android.com/studio/images/test/espresso-test-recorder-window_2-2_2x.png)

## 添加断言来验证UI元素
断言通过三种主要的方式验证一个[View](https://developer.android.com/reference/android/view/View.html)元素的存在或内容:
- __text is__ : 校验选择元素的文件内容
- __exists__ : 屏幕中当前的View内，校验元素是存在的
- __does not exist__ : 当前的View内，校验元素是不存在的

给测试中添加断言，参考下面的步骤:
1. 点击 __Add Assertion__ 。一个 "屏幕截图"对话会显示出来，当Espresso获取到关于当前APP状态的UI结构或其它信息。一旦Espresso获取到屏幕截图，对话框将会关闭。
2. 在当前面板 __Record Your Test__ 窗口的右侧会显示当前屏幕显示的布局样式。选择一个需要创建断言的可见元素，在截图中点击元素或点击在窗口底部的 __Edit assertion__ 对话框的第一个下拉菜单。被选择的View对象会在红框中高亮。
3. 在__Edit assertion__ 对话框的第二个下拉菜单中选择你想使用的断言。Espresso交会弹出针对选择元素的断言
  - 如果你选择"text is"断言，Espresso会自动插入当前选择元素中的值。你可以在 __Edit assertion__ 编辑文本来匹配你想得到的断言结果。
4. 点击 __Save and Add Another__ 来创建另外一个断言或点击 __Save Assertion__ 来关闭断言面板。

在图2中，显示了"text is"断言被创建用于验证笔记的标题是"Happy Testing!":
![图2](https://developer.android.com/studio/images/test/espresso-test-recorder-assertion_2-2_2x.png)

当创建一个断言时，你可以继续与你的APP交互，只要断言面板 __Record Your Test__ 窗口仍然打开。Espresso Test Recorder将持续录制你的动作，一旦你正在编辑的断言保存后，新的交互会显示在后面。针对断方的截屏会保存当你在设备或模拟器中点击"Add Assertion"时的APP布局。

> 注意：Espresso Test Recorder还是一个实验性的特性，工具当前仅支持可见层断言。你可以通过添加断言来确定屏幕中的元素，屏幕截取仍显示可见模式，并且选择的元素的红色边框和无素在屏幕中的实际位置是不匹配的。

## 保存录制
一旦，你完成与你APP的交互并添加了断言，使用下面的步骤来保存你的记录并生成Espresso测试脚本：
1. 点击 __Complete Recording__ 。__Pick a test class name for your test__ 窗口将会显示。
2. Espresso Test Recorder将会对测试一个基于启动的Activity的唯一名字。如果你想改变测试名的话，使用 __Test class name__ 。点击 __Save__ 。
> 如果你没有给项目添加Espresso依赖， __Missing Espresso dependencies__ 对话框会在你保存的时候显示。 点击 __Yes__ 将会自动添加依赖至你的 build.gradle 文件中。

3. 在Espresso Test Recorder生在文件之后，会自动打开。并且 Android Studio将会在IDE的 __Project__ 窗口中找开测试类。
> 测试被保存的位置依据你的[instrumentation test](https://developer.android.com/training/testing/unit-testing/instrumented-unit-tests.html)，也与启动的Activity包名有关。比如，测试[Notes testing app](https://github.com/googlecodelabs/android-testing)保存在 __src > androidTest > java > com.example.username.appname__ 录制测试的APP模块下。


## 本地运行Espresso测试

为了运行Espresso测试，使用在IDE左侧的 __Project__ 窗口：
1. 打开APP模块文件夹，找到你想运行的测试。测试的位置依据你的[instrumentation test](https://developer.android.com/training/testing/unit-testing/instrumented-unit-tests.html)位置和启动Activity包名。下面的例子说明[Notes testing app](https://github.com/googlecodelabs/android-testing)的测试应该保存在哪：
- 如果你在窗口中使用[Android视图](https://developer.android.com/studio/projects/index.html#ProjectFiles)，进入 __java > com.example.username.appname(androidTest)__ .
- 如果你在窗口中使用 __Project视图__， 进入 __src > androidTest > java > com.example.username.appname__ 模板文件夹。

2. 在测试代码上点击右键，选择 __Run 'testName'__ .
- 同样，你可以打开测试文件，在生成的测试类或方法中右键点击来运行测试。了解更多关于如何运行测试在[测试你的APP](https://developer.android.com/studio/test/index.html#run_a_test)。

3. 在 __Select Deployment Target__ 窗口，选择你想要运行测试的测试设备。如果有需要，[创建一个新安卓虚拟设备](https://developer.android.com/studio/run/managing-avds.html)。点击 __OK__ 。

在IDE的底部 __Run__ 窗口中，会显示测试的运行过程。Android Studio运行项目的完整构建并在 __Run__ 窗口中打开一个测试名称的页签，如图3展示。你可以在页签中检查是否你的测试通过或失败，以及你的测试运行的多久。当测试结束后，页签将会显示 "Tests ran to completion."
![图3](https://developer.android.com/studio/images/test/run-window-espresso-test_2-2-preview-7_2x.png)

了解更多的编写测试的运行配制，可以去[创建并编辑 运行、调试 配制](https://developer.android.com/studio/run/rundebugconfig.html#creating)看"Defining a test configuration for a class or method"部分

## 运行Android的Espresso测试在 Firebase Test Lab

你可以在[Firebase Test Lab](https://firebase.google.com/docs/test-lab/)运行的Espresso测试在数以百计设备配制中。在Test Lab中可以使用[free daily quota on the Spark plan](https://firebase.google.com/docs/test-lab/overview#quota_for_spark_and_flame_plans)来免费运行测试。为了在[Firebase Test Lab](https://firebase.google.com/docs/test-lab/)中运行测试，为你的APP[创建一个Firebase项目](https://firebase.google.com/docs/test-lab/web-ui#create_a_firebase_project)，并按Android Studio的操作说明来[运行你的测试使用Firebase Test Lab](https://developer.android.com/training/testing/unit-testing/instrumented-unit-tests.html#run-ctl).
![图4 在Run窗口的使用Firebase Test Lab测试多个设备的结果展示](https://developer.android.com/images/training/ctl-test-results.png)
