---
title: 'Node入门'
tags:
 - Node.js
categories:
 - Book
date: 2016-09-20 20:44:00
---

## 书

- 在线版本: [Node入门](http://www.nodebeginner.org/index-zh-cn.html)，可在线`阅读全文`

## 读后感

- Node.js的入门，没有讲任何的框架。但从最基础的知识点把Node如何使用讲的比较清晰

- 书中的例子做完后(只有**42**页)，可以实现一个`文件上传`的完整功能，不需要其它复杂的框架

<!--more-->

## 代码分析

- 功能说明
  - 选择文件，并上传至`/tmp/test.png`
  - 回显上传的文件至页面中

```
.
├── index.js  #入口文件
├── requestHandlers.js  #请求处理
├── router.js #路由跳转
└── server.js #服务控制
```

- `index.js`

```
var server = require('./server');
var router = require('./router');
var requestHandlers = require('./requestHandlers');

var handle = {};
handle["/"] = requestHandlers.start;
handle["/start"] = requestHandlers.start;
handle["/upload"] = requestHandlers.upload;
handle["/show"] = requestHandlers.show;

server.start(router.route,handle);
```

- `requestHandlers.js`

```
var querystring = require("querystring"),
    fs = require("fs"),
    formidable = require("formidable");

function start(response) {
    console.log("Request handler 'start' was called.");

    var body = '<html>'+
        '<head>'+
        '<meta http-equiv="Content-Type" content="text/html; '+
        'charset=UTF-8" />'+
        '</head>'+
        '<body>'+
        '<form action="/upload" enctype="multipart/form-data" '+
        'method="post">'+
        '<input type="file" name="upload" multiple="multiple">'+
        '<input type="submit" value="Upload file" />'+
        '</form>'+
        '</body>'+
        '</html>';

    response.writeHead(200, {"Content-Type": "text/html"});
    response.write(body);
    response.end();
}

function upload(response, request) {
    console.log("Request handler 'upload' was called.");

    var form = new formidable.IncomingForm();
    console.log("about to parse");
    form.parse(request, function(error, fields, files) {
        console.log("parsing done");
        fs.renameSync(files.upload.path, "/tmp/test.png");
        response.writeHead(200, {"Content-Type": "text/html"});
        response.write("received image:<br/>");
        response.write("<img src='/show' />");
        response.end();
    });
}

function show(response) {
    console.log("Request handler 'show' was called.");
    fs.readFile("/tmp/test.png", "binary", function(error, file) {
        if(error) {
            response.writeHead(500, {"Content-Type": "text/plain"});
            response.write(error + "\n");
            response.end();
        } else {
            response.writeHead(200, {"Content-Type": "image/png"});
            response.write(file, "binary");
            response.end();
        }
    });
}

exports.start = start;
exports.upload = upload;
exports.show = show;
```

- `router.js`

```
function route(handle, pathname, response, request) {
    console.log('About to route a request for ' + pathname);
    if (typeof  handle[pathname] === 'function') {
        handle[pathname](response, request);
    } else {
        console.log("No request handler found for " + pathname);
        response.writeHead(404, {"Content-Type": "text/html"});
        response.write("404 Not found");
        response.end();
    }
}

exports.route = route;
```

- `server.js`

```
var http = require("http");
var url = require('url');

function start(route,handle) {
    function onRequest(request,response) {
        var pathname = url.parse(request.url).pathname;
        var postData = "";

        console.log('Request for ' + pathname + ' received.');

        route(handle, pathname, response, request);
    }
    http.createServer(onRequest).listen(8889);
    console.log('Server starting on 8889.');
}

exports.start = start;
```
