---
title: 'Http-Header'
tags:
  - API测试
  - SuperTest
categories:
  - Tool
date: 2016-02-29 20:14:00
---
# Header

## 定义

提供HTTP所需要的信息或发送的信息

`
HTTP header fields provide required information about the request or response, or about the object sent in the message body.
`

<!--more-->


## 分类

* General-header：常用的http请求或响应的header信息

 * Cache-Control：缓存控制
 * Connection：请求后的链接状态，Connection/keep-alive/close
 * Date：时间戳，支持这三种格式

  ```
Sun, 06 Nov 1994 08:49:37 GMT  ; RFC 822, updated by RFC 1123
Sunday, 06-Nov-94 08:49:37 GMT ; RFC 850, obsoleted by RFC 1036
Sun Nov  6 08:49:37 1994       ; ANSI C's asctime() format
  ```

 * Pragma：未来将不会使用
 * Trailer：指定内容将采用何种格式

  ```
Transfer-Encoding
Content-Length
Trailer
  ```

  * Transfer-Encoding：传输的编码，与`content-encoding`不一样
  * Upgrade：支持其它的协议`HTTP/2.0, SHTTP/1.3, IRC/6.9, RTA/x11`
  * Via：定义协议和接收者
  * Warning：存储额外的信息，如状态或消息

* Client Request-header：仅包括请求部分的header信息
 * Accept：接收的内容类型
 * Accept-Charset：接收的字符集
 * Accept-Encoding：字符编码
 * Accept-Language：语言
 * Authorization：权限请求内容，参考[SuperTest-header:Auth设置](http://aimer1124.github.io/2016/02/28/title-Tool-SuperTest-header-Auth%E8%AE%BE%E7%BD%AE/)
 * Cookie：Cookie设置
 * Expect：期望的服务器行为
 * From：请求来源，指定的邮件地址
 * If-Match：请求服务器的执行Match的tag，如果match上，则执行；否则返回412状态
 * If-Modified-Since：与`If-Match`类似，对比内容为时间
 * If-Range：可定义`If-Match`与`If-Modified-Since`两个维度的内容，或一个维度的内容
 * If-Unmodified-Since：如果没有修改，与`If-Modified-Since`类似
 * Max-Forwards：最大代理和网关的跳转次数，防止出现无限循环
 * Proxy-Authorization：代理的权限
 * Range：请求内容的部分次序
 * Referer：指定相关的地址
 * TE：`Transfer-Encoding`
的扩展
 * User-Agent：使用的客户端及版本

* Server Response-header：仅包括响应的header信息

 * Accept-Ranges：指定接收资源的次序
 * Age： 生成response的时间
 * ETag： 值标签
 * Location： 重定向的URI地址，绝对地址
 * Proxy-Authenticate： 代理权限
 * Retry-After： 状态码503出现后，多久重试
 * Server： 说明使用的服务器及一些comments
 * Set-Cookie： 设置返回的cookie值
 * Vary： 定义header中的多个资源
 * WWW-Authenticate： 必须在401返回状态中，权限内容

* Entity-header：请求数据body或资源部分
 * Allow： 具体的请求方法，Get/POST等
 * Content-Encoding： 定义整个资源的媒介类型
 * Content-Language
 * Content-Length
 * Content-Location
 * Content-MD5
 * Content-Range
 * Content-Type
 * Expires： 失效时间
 * Last-Modified： 最后修改时间


# 参考资料

* Heder分类：[http://www.tutorialspoint.com/http/http_header_fields.htm](http://www.tutorialspoint.com/http/http_header_fields.htm)
