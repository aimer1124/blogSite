---
title: '七牛床图迁移至Github'
tags:
  - Github
  - 七牛
categories:
  - Mark
date: 2018-10-18 15:10:00
---


问题由于网站的大部分床图一直使用的是七牛的，近期[官网更新](https://developer.qiniu.com/fusion/kb/1319/test-domain-access-restriction-rules)，导致原测试域名已失效，之前在测试域名存储的图片无法`访问、查看、下载`，网站文章关联的图片无法正常查看。所以决定**把图片从七牛迁移至Github来存储，弃用七牛云**。

```
七牛融合 CDN 测试域名（以 clouddn.com/qiniucdn.com/qiniudn.com/qnssl.com/qbox.me 结尾），每个域名每日限总流量 10GB，
每个测试域名自创建起 30 个自然日后系统会自动回收，仅供测试使用，详情查看 七牛测试域名使用规范 。
```

<!--more-->

---

## 具体操作分三步

```
- Step1:从废弃测试域名空间至可用测试域名空间迁移
- Step2:从测试域名的空间下载至本机
- Step3:从本机上传至Github中
```

### Step1:从废弃测试域名空间至可用测试域名空间迁移
`废弃测试域名空间：bucketA，可用测试域名空间：bucketB`

- 下载[qshell](https://github.com/qiniu/qshell)包到本机，解压，查看是否可以正常运行
```
➜  qshell-v2.2.0 ./qshell-darwin-x64 -v
QShell/v2.2.0 (darwin; amd64; go1.9)
```
- 执行`./qshell-darwin-x64 account AK SK`配制自己的账号信息，AK/SK查看方法[https://portal.qiniu.com/user/key](https://portal.qiniu.com/user/key)，检验是否配制成功
```
➜  qshell-v2.2.0 ./qshell-darwin-x64 account
AccessKey: Your AK
SecretKey: Your SK
```

- 使用导出文件列表命令，导出需要迁移的bucketA文件列表

```
➜  qshell-v2.2.0 ./qshell-darwin-x64 listbucket bucketA tocopy.txt
```

- 需要手动把`tocopy.txt`中的的每行内容修改为**仅有文件名**

- 执行平移(batchcopy)命令
```
➜  qshell-v2.2.0 ./qshell-darwin-x64 batchcopy --force --overwrite bucketA bucketB tocopy.txt
```

至些，已完成失败图片的`救援工作`。

### Step2:从测试域名的空间下载至本机

- 新增一个qdownload配制文件，具体使用[参考](https://github.com/qiniu/qshell/blob/master/docs/qdownload.md)，精简版本如下：
```
{
    "dest_dir"   :   "YourDownloadPath",
    "bucket"     :   "bucketB",
    "cdn_domain" :   "ConfigYourTestCDNDomain"
}
```
如果不配制`cdn_domain`的话，需支付源站流量费用，无法减免。**官方说法，官方说法，官方说法**
- 执行下载命令，便会开始进入图片下载
```
./qshell-darwin-x64 qdownload 10 download.conf
```

下载结束后，会生成一个下载日志文件，用于查看下载过程。至此，所有图片已下载至本机

### Step3:从本机上传至Github中

- 将本机图片上传至Github中(依据自己的喜好，随便存)
- 修改原来文章中的链接地址指向七牛的地址，全部重新指向Github地址。

经测试，所有图片均可正常打开，网站的图片均可正常打开及查看。


