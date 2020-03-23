---
title: 'Jenkins with Grunt'
tags:
 - Jenkins
 - SuperTest
 - Grunt
 - Node.js
categories:
 - Tool
date: 2016-03-03 20:45:38
---

# Jenkins

```
In a nutshell, Jenkins is the leading open source automation server.
Built with Java, it provides hundreds of plugins to support building,
testing, deploying and automation for virtually any project
```

```
Jenkins是一个开源软件项目，旨在提供一个开放易用的软件平台，使软件的持续集成变成可能。
```

<!--more-->


## 特性
* 容易安装，提供各种操作系统的安装包及独立的jar包进行安装
* 容易配制，完善的GUI提供快速的配制操作界面
* 强大的[插件系统](https://wiki.jenkins-ci.org/display/JENKINS/Plugins)，可以满足基本所有的项目需求
* 可扩展性，个性化定制Jenkins，自行开发插件
* 分布式构建，可让项目在不同的模块、系统中任意搭配。当然操作系统也可随意搭配

## 下载
### 安装包
官网首页提供了支持各种操作系统的安装包，可直接进行下载，[http://jenkins-ci.org/](http://jenkins-ci.org/)

### war包
直接下载[war](http://mirrors.jenkins-ci.org/war/latest/jenkins.war)包

## 安装&运行

### 安装包
直接使用对应平台的安装包，进行安装即可。没有啥可设置的

### war包
直接使用`java -jar jenkins.war`来运行war包，即可

```
➜  jenkins java -jar jenkins.war
Running from: /Users/yjshi/Downloads/All/Software/jenkins/jenkins.war
webroot: $user.home/.jenkins
Mar 03, 2016 9:21:54 PM winstone.Logger logInternal
INFO: Beginning extraction from war file
Mar 03, 2016 9:21:54 PM org.eclipse.jetty.util.log.JavaUtilLog info
INFO: jetty-winstone-2.9
Mar 03, 2016 9:21:56 PM org.eclipse.jetty.util.log.JavaUtilLog info
INFO: NO JSP Support for , did not find org.apache.jasper.servlet.JspServlet
Jenkins home directory: /Users/yjshi/.jenkins found at: $user.home/.jenkins
Mar 03, 2016 9:21:57 PM org.eclipse.jetty.util.log.JavaUtilLog info
INFO: Started SelectChannelConnector@0.0.0.0:8080
Mar 03, 2016 9:21:57 PM winstone.Logger logInternal
INFO: Winstone Servlet Engine v2.0 running: controlPort=disabled
Mar 03, 2016 9:21:57 PM jenkins.InitReactorRunner$1 onAttained
INFO: Started initialization
Mar 03, 2016 9:21:57 PM jenkins.InitReactorRunner$1 onAttained
INFO: Listed all plugins
Mar 03, 2016 9:21:57 PM jenkins.InitReactorRunner$1 onAttained
INFO: Prepared all plugins
Mar 03, 2016 9:21:57 PM jenkins.InitReactorRunner$1 onAttained
INFO: Started all plugins
Mar 03, 2016 9:21:57 PM jenkins.InitReactorRunner$1 onAttained
INFO: Augmented all extensions
Mar 03, 2016 9:21:58 PM jenkins.InitReactorRunner$1 onAttained
INFO: Loaded all jobs
Mar 03, 2016 9:21:59 PM hudson.model.AsyncPeriodicWork$1 run
INFO: Started Download metadata
Mar 03, 2016 9:21:59 PM org.jenkinsci.main.modules.sshd.SSHD start
INFO: Started SSHD at port 64899
Mar 03, 2016 9:21:59 PM jenkins.InitReactorRunner$1 onAttained
INFO: Completed initialization
Mar 03, 2016 9:21:59 PM hudson.UDPBroadcastThread run
INFO: Cannot listen to UDP port 33,848, skipping: java.net.SocketException: Can't assign requested address
Mar 03, 2016 9:21:59 PM jenkins.InitReactorRunner$1 onAttained
INFO: Started initialization
Mar 03, 2016 9:21:59 PM jenkins.InitReactorRunner$1 onAttained
INFO: Listed all plugins
Mar 03, 2016 9:21:59 PM jenkins.InitReactorRunner$1 onAttained
INFO: Prepared all plugins
Mar 03, 2016 9:21:59 PM jenkins.InitReactorRunner$1 onAttained
INFO: Started all plugins
Mar 03, 2016 9:21:59 PM jenkins.InitReactorRunner$1 onAttained
INFO: Augmented all extensions
Mar 03, 2016 9:21:59 PM jenkins.InitReactorRunner$1 onAttained
INFO: Loaded all jobs
Mar 03, 2016 9:21:59 PM jenkins.InitReactorRunner$1 onAttained
INFO: Completed initialization
Mar 03, 2016 9:21:59 PM hudson.WebAppMain$3 run
INFO: Jenkins is fully up and running
```
## 访问
直接访问[http://localhost:8080/](http://localhost:8080/)，即可打开jenkins的界面

![](/img/github.jenkins.init.png)



## 更多安装说明

* 其它安装说明(https://wiki.jenkins-ci.org/display/JENKINS/Installing+Jenkins)


# Grunt

```
The JavaScript Task Runner
```

## 安装npm
官网下载对应的操作系统版本-[NPM](https://nodejs.org/en/download/)，下载完成后，直接进行安装即可

## 安装Grunt


```
npm install -g grunt-cli
```

## 验证安装
正常显示版本号，则安装成功

```
➜  ~ grunt --version
grunt-cli v0.1.13
```
# Combine：Jenkins&Grunt

## 安装NodeJS插件
* 使用Jenkins安装NodeJS插件，选择[install without restart]
![](/img/github.NodeJS_Plugin.png)
* 等待安装成功
![](/img/github.NodeJs_Plugin_Install.png)

## Jenkins安装Grunt
为执行Grunt时，使用
![](/img/github.Jenkins_Install_NodeJS.png)

## 配制Job

- 在Jenkins中选择[New Item]，在[Item name]中输入(GruntJob)，并选择[Freestyle project]，点击[OK]
![](/img/github.jenkins%26grunt.FirstStep.png)
- 配制build，选择[Save]
![](/img/github.Job_Config.png)
- 在Job处选择[Build Now]，查看构建结果

```
var sys = require('sys');
sys.puts('NodeJS Test');
sys.puts('***************');
sys.puts('helloworld');
```
![](/img/github.Build_Result.png)

- 添加build step中`execute shell`

```
npm update
grunt
```
- 指定的grunt构建配制完成


# 参考

* Jenkins官网:[http://jenkins-ci.org/](http://jenkins-ci.org/)
* Jenkins百度百科：[http://baike.baidu.com/link?url=pVYPV6gky9E3fCPe1hAvofgKswHkO06S0B6oVYYCQpXWaBrRB5TcOvJEGaOmae6a6tOLo19xCdEW1ovacOcsoq](http://baike.baidu.com/link?url=pVYPV6gky9E3fCPe1hAvofgKswHkO06S0B6oVYYCQpXWaBrRB5TcOvJEGaOmae6a6tOLo19xCdEW1ovacOcsoq)
* Grunt官网：[http://gruntjs.com/](http://gruntjs.com/)
* npm:[NPM](https://nodejs.org/en/download/)
* jenkins-integration-with-grunt:[http://stackoverflow.com/questions/21765428/jenkins-integration-with-grunt](http://stackoverflow.com/questions/21765428/jenkins-integration-with-grunt)
