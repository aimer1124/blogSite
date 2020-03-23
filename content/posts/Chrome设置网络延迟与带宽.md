---
title: 'Chrome设置网络延迟与带宽'
tags:
 - Chrome
categories:
 - Tool
date: 2016-03-09 20:20:00
---

# Developer Tools`开发者工具`查看网络请求
* Windows: F12键
* Mac OS: option+command+i键
<img src="/img/github.Chrome.DeveoperTools.png" />
* 打开网络请求`Network`
* 请求网址[http://aimer1124.github.io/](http://aimer1124.github.io/)后，`Network`中便会有本次的网络请求内容
![NetWorks](/img/github.Chrome.Networks.png)
* 点击第一条请求`http://aimer1124.github.io/`，可查看到此网络请求的详细信息Request/Response
 * 切换到`Timing`栏中，显示具体的请求时间消耗
![Timing](/img/github.Chrome.Timing.png)
 * 切换`Headers`、`Preview`、`Response`、`Cookies`，也可直接查看对应的信息

<!-- more -->
# 设置网络延迟和带宽
* 点击`No throttling`会显示出`Chrome`已提前设置好常用的网络延迟和带宽，供直接选择

| 网络类型  | 带宽  | 延迟 |
|:-------------: |:---------------:|:-------------:|
| Offline| 0kb/s | 0ms |
| GPRS| 50kb/s | 500ms |
| Regular 2G| 250kb/s | 300ms |
| Good 2G| 450kb/s | 150ms |
| Regular 3G| 750kb/s | 100ms |
| Good 3G| 1Mb/s | 40ms |
| Regular 4G| 4Mb/s | 20ms |
| DSL| 2Mb/s | 5ms |
| WiFi| 30Mb/s | 2ms |
* 选择`GRPS`，clear网络请求，再次刷新页面，查看请求`http://aimer1124.github.io/`的`Timing`
![Latency](/img/github.Chrome.Latancy.png)
* 此时，可查看到对应的网络延迟已经`生效`

# 自定义网络延迟和带宽
* 点击`No throttling`-`Custom`-`add`进入`Network Throttling Profiles`设置页面
* 设置`Profile Name`：slow1S，`Throughput`：10，`Latency`为：1000
![setNetwork](/img/github.Chrome.setNetwork.png)
* 关闭设置框，切换`No throttling`为`slow1S`，自定义网络延迟与带宽设置完成
![setCustomNetwork](/img/github.Chrome.setCustomNetwork.png)

# 参考
* Measure Resource Loading Times:[https://developers.google.com/web/tools/chrome-devtools/profile/network-performance/resource-loading#network-panel-overview](https://developers.google.com/web/tools/chrome-devtools/profile/network-performance/resource-loading#network-panel-overview)
* Device Mode & Mobile Emulation:[https://developer.chrome.com/devtools/docs/device-mode](https://developer.chrome.com/devtools/docs/device-mode)
