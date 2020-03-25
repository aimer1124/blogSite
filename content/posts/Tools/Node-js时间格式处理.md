---
title: 'Node.js时间格式处理'
tags:
  - Node.js
  - API测试
categories:
  - Tool
date: 2016-01-26 22:18:00
---

## moment库

* 专门用于Javascript的时间转化、验证、处理、展示
* 安装moment

```
npm install moment
```


## 使用moment
* 引用moment

```javascript
var moment = require('moment');
```

<!-- more -->

* 转化时间

```javascript
//将时间格式转化为：2016-01-22 21:21:26
moment(new Date()).format("YYYY-MM-DD HH:mm:ss");
moment().format('MMMM Do YYYY, h:mm:ss a'); // January 26th 2016, 10:25:00 pm
moment().format('dddd');                    // Tuesday
moment().format("MMM Do YY");               // Jan 26th 16
moment().format('YYYY [escaped] YYYY');     // 2016 escaped 2016
moment().format();                          // 2016-01-26T22:25:24+08:00
```
* 相对时间

```javascript
moment("20111031", "YYYYMMDD").fromNow(); // 4 years ago
moment("20120620", "YYYYMMDD").fromNow(); // 4 years ago
moment().startOf('day').fromNow();        // a day ago
moment().endOf('day').fromNow();          // in 2 hours
moment().startOf('hour').fromNow();      
```
* 日历时间

```javascript
moment().subtract(10, 'days').calendar(); // 01/16/2016
moment().subtract(6, 'days').calendar();  // Last Wednesday at 10:27 PM
moment().subtract(3, 'days').calendar();  // Last Saturday at 10:27 PM
moment().subtract(1, 'days').calendar();  // Yesterday at 10:27 PM
moment().calendar();                      // Today at 10:27 PM
moment().add(1, 'days').calendar();       // Tomorrow at 10:27 PM
moment().add(3, 'days').calendar();       // Friday at 10:27 PM
moment().add(10, 'days').calendar();     
```

* 其它应用

```javascript
moment().format('L');    // 01/26/2016
moment().format('l');    // 1/26/2016
moment().format('LL');   // January 26, 2016
moment().format('ll');   // Jan 26, 2016
moment().format('LLL');  // January 26, 2016 10:28 PM
moment().format('lll');  // Jan 26, 2016 10:28 PM
moment().format('LLLL'); // Tuesday, January 26, 2016 10:28 PM
moment().format('llll');
```
* 其它使用：[官方文档](http://momentjs.com/docs/)

## API测试应用：Node.js
* 日期判断、对比
* 日期格式转化
