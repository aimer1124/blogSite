---
title: 'Node.js调用数据库:Mysql'
tags:
  - API测试
  - Node.js
  - SuperTest
categories:
  - Tool
date: 2016-01-26 22:01:00
---
## 安装Mysql包

```
npm install mysql
```

## 调用 Mysql包

```javascript
var mysql = require('mysql');
```

## 数据库查询

<!-- more -->

```javascript
var mysql = require('mysql');
var connection = mysql.createConnection({
    host : '10.29.10.29',
    port : 3307,
    user : 'root',
    password : '',
    database : 'emall',
    //charset : 'UTF8_GENERAL_CI',
    debug : false
});
connection.connect();
connection.query("use emall");
connection.query('select id from users', function(err,results) {
		if (err) {
          throw err;
        }
        });
connection.end();

```

## 数据库插入

```javascript
var mysql = require('mysql');
var connection = mysql.createConnection({
    host : '10.29.10.29',
    port : 3307,
    user : 'root',
    password : '',
    database : 'emall',
    //charset : 'UTF8_GENERAL_CI',
    debug : false
});
connection.connect();
connection.query("use emall");
var insertUser2 = "INSERT INTO `sms_verification_code` (`phone_number`, `code`) VALUES ('18392520000', '018227');";
connection.query(insertUser2,function(err,results,field){
    if (err) {
        throw err;
    }
});
connection.end();					
```

## API测试应用：Node.js

* 初始化数据
* 数据CRUD
* 获取部分无返回值的Post结果，如：查询创建用户后，获取用户的ID
