---
title: "一行命令连接ECS"
date: 2020-03-25T16:40:04+08:00
tags:
  - ECS
  - SSH
categories:
  - Tool
---


**目标：一行命令，直接连接至阿里云的ECS。不需要手动输入IP/Port/User/Pwd。**

## ECS

### 创建密钥对

- 打开ECS的"网络与安全"..>"密钥对"
- 左上角“创建密钥对”，完成密钥`创建`
- 保存生成的`密钥对`至`本机`

### 绑定密钥对

- 在生成的密钥中，点击`绑定密钥对`
- 完成密钥与实例的绑定

## SSH

### 配制Config

- 修改`*.pem`文件的属性，支持可执行
```
chmod 400 *.pem
``` 
- 找到本机的ssh config文件，没有可直接创建，路径参考`~/.ssh/config`
- 完成config文件的配制，内容参考如下：
```
Host aliyun
  HostName ECS公网IP
  User root
  Port 22
  IdentityFile ~/.ssh/*.pem
```

### 连通测试 

命令行打开，输入`ssh aliyun`，可直接连接至阿里云的ECS

## 参考

- [使用SSH密钥对连接Linux实例](https://help.aliyun.com/document_detail/51798.html#title-7je-5ba-sm2)
- [绑定SSH密钥对](https://help.aliyun.com/document_detail/51796.html?spm=a2c4g.11186623.2.11.db7b4737ruorLv#concept-zzt-nl1-ydb)