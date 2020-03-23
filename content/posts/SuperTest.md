---
title: 'SuperTest-API测试'
tags:
  - API测试
  - SuperTest
  - Testing
  - Jenkins
  - Grunt
categories:
  - Tool
date: 2016-01-17 19:51:00
---
## 什么是SuperTest
* The motivation with this module is to provide a high-level abstraction for testing HTTP, while still allowing you to drop down to the lower-level API provided by super-agent.
* 简单说明：用来测试HTTP请求，提供简单的super-agent来实现API请求

## 安装SuperTest

* npm安装

 - 官网下载对应的操作系统版本-[NPM](https://nodejs.org/en/download/)，下载完成后，直接进行安装即可
 - cnpm,若翻墙网络比较慢或访问不了的话，可以尝试使用cnpm(国内的镜像)。[CNPM](https://github.com/cnpm/cnpm)

* SuperTest安装

 ```
 npm install supertest --save-dev
 ```
* grunt安装

```
npm install -g grunt-cli
```

<!-- more -->

## 使用Grunt来管理和运行SuperTest

* Git Clone [SuperTestDemo](https://github.com/aimer1124/SuperTestDemo)。此项目针对访问的URL的返回状态进行验证。

* 进入目录，执行grunt命令。查看执行结果

## 组装SuperTest测试API

* 多个API测试：添加多个it，进行多个API测试

```javascript
	describe('司机信息.', function() {
	    it('能够获取通过司机的列表.', function(done) {
	        request.get('/driver?status=PASSED&page_size=10&page_index=0')
	            .expect(200)
	            .expect('Content-Type', 'application/json;charset=utf-8')
	            .end(done);
	    });

	    it('能够获取接单司机的信息.', function(done) {
	        request.get('/driver/driver-info?order_id=ce0a5279-6a7a-42d1-87d5-d396eb60c4bc')
	             .expect(200, {
	                "uuid": "222222"
	                }, done);
	    })

	});
```

* 测试场景：利用上面的多个API测试，达到测试场景的组装

```javascript
    describe('司机信息.', function() {
	    it('能够获取通过司机的列表.', function(done) {
	        request.get('/driver?status=PASSED&page_size=10&page_index=0')
	            .expect(200)
	            .expect('Content-Type', 'application/json;charset=utf-8')
	            .end(done);
	    });

	    it('能够获取接单司机的信息.', function(done) {
	        request.get('/driver/driver-info?order_id=ce0a5279-6a7a-42d1-87d5-d396eb60c4bc')
	             .expect(200, {
	                "uuid": "222222"
	                }, done);
	    })

	});
```

* 获取API的返回数据：定义一个变量(var)，在其它it中使用

```javascript
  describe('司机信息.', function() {
  		var id;
	    it('能够获取通过司机的列表.', function(done) {
	        request.get('/driver?status=PASSED&page_size=10&page_index=0')
	            .expect(200)
	            .expect('Content-Type', 'application/json;charset=utf-8')
	            .end(done);
	    });

	    it('能够获取接单司机的信息.', function(done) {
	        request.get('/driver/driver-info?order_id=ce0a5279-6a7a-42d1-87d5-d396eb60c4bc')
	             .expect(function(res){
                 	id=res.body.uuid;
                 })
                 .expect(200, {
	                "uuid": "222222"
	                }, done);
	    })

	});
```

## Jenkins集成

* 配制command line调用grunt即可
* 参考[Tool]Jenkins with Grunt](http://aimer1124.github.io/2016/03/03/Tool-Jenkins-with-SuperTest-and-Grunt/)
