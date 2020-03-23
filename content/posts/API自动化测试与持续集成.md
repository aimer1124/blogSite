---
title: 'API自动化测试与持续集成'
tags:
  - API测试
  - SuperTest
  - Gulp
  - Grunt
  - Jenkins
  - Git
  - Testing
categories:
  - Testing
date: 2016-05-10 14:23:00
---
# 目的
* 如何使用`SuperTest`测试框架，进行API测试
* 如何将API测试与构建工具结合
* 如何将API测试、构建工具与持续集成结合

<!--more-->

# SuperTest
## 什么是SuperTest
*  `To provide a high-level abstraction for testing HTTP`，提供一个高级别的`HTTP`测试
* Github地址：[SuperTest](https://github.com/visionmedia/supertest)

## 如何安装
* 命令

```
npm install supertest --save-dev
```
* 样例

```
describe('Test Demo.', function() {

    it('Visit URL', function(done) {
        request.get('')
            .expect(200)
            .end(done);
    });
});
```
* 样例原理：通过获取请求的`结果`，对请求结果进行`验证`。`样例`中的验证条件为返回的状态码为`200`。

# 自动化API测试：Grunt & Gulp

## Grunt篇

### 什么是Grunt

* `The JavaScript Task Runner`，JavaScript的构建工具
* 官网：[Grunt](http://gruntjs.com/)

### 安装
* 命令

```
npm install -g grunt-cli
```

### 功能分析

#### 测试目的：请求[https://github.com/aimer1124/SuperTestWithGrunt](https://github.com/aimer1124/SuperTestWithGrunt)是否能返回状态码`200`


#### 使用Github来Clone`https://github.com/aimer1124/SuperTestWithGrunt.git`

```
.
├── Gruntfile.js
├── README.md
├── api-test.iml
├── package.json
├── results.txt
└── test
    ├── config
    │   └── endpoints.js
    └── module
        └── demo.js
```

* `/test/module/demo.js`:测试脚本

```
var config = require('../config/endpoints'),

request = require('supertest')(config.host[config.env]);

describe('Test Demo.', function() {

  this.timeout(10000);

  it('Visit ' + config.env, function(done) {

    request.get('')

                .expect(200)

                .end(done);

    });

});
```
* `/test/config/endpoints.js`:环境配制

```
module.exports = {

host : {

master: 'https://github.com/aimer1124/SuperTestWithGrunt',

branch: 'https://github.com/aimer1124/SuperTestWithGrunt/tree/differentENV'

},

env: process.env.NODE_ENV || 'master'

};
```

* `Gruntfile.js`:Grunt运行时的命令配制
* `package.json`:[npm](https://www.npmjs.com/) 安装时所需要的包
* `results.txt`:执行结果存放文件

#### 执行
* 命令:`grunt`
* 运行结果

```
➜  SuperTestWithGrunt git:(master) ✗ grunt
Running "mochaTest:test" (mochaTest) task


  Test Demo.
    ✓ Visit master (1640ms)


  1 passing (2s)


Done, without errors.
```
* 结果分析：`✓ Visit master (1640ms)`表示测试正常通过；`1 passing (2s)`表示整个测试所执行的时间和测试所执行的数量

## Gulp篇
### 什么是Gulp
* `Automate and enhance your workflow`，自动化并且增强你的工作流
* 官网：[http://gulpjs.com/](http://gulpjs.com/)
* 中文官网：[http://www.gulpjs.com.cn/](http://www.gulpjs.com.cn/)

### 安装
* 命令

```
npm install --global gulp-cli
```
### 功能分析
#### 测试目的：请求[http://aimer1124.github.io/](http://aimer1124.github.io/)是否能返回状态码`200`

#### 使用Github来Clone[https://github.com/aimer1124/SuperTestWithGulp](https://github.com/aimer1124/SuperTestWithGulp)

```
.
├── README.md
├── config
│   ├── branch.js
│   ├── endpoints.js
│   └── master.js
├── gulpfile.js
├── package.json
└── test
    └── test-demo.js
```

* `/test/config/endpoints.js`:环境配制

```
var host = {
    master: require('./master.js'),
    branch: require('./branch.js')
};

var ENV;

module.exports = function(env) {
    if (env) {
        ENV = host[env];
        return;
    }
    return ENV;
};

```
* `/test/config/master`的具体配制

```
module.exports = {
    url: 'http://aimer1124.github.io/',
    name: 'master'
};

```
* `/test/module/test-demo.js`:测试脚本

```

var data = require('../config/endpoints'),
    request = require('supertest')(data().url);

describe('Test Demo.', function() {

    this.timeout(10000);

    it('Visit ' + data().url, function(done) {
        request.get('')
            .expect(200)
            .end(done);
    });
    console.log('You are in ' + data().name);
});

```
* `gulpfile.js`:Grunt运行时的命令配制
* `package.json`:[npm](https://www.npmjs.com/) 安装时所需要的包
* `results.txt`:执行结果存放文件

#### 执行

* 命令

```
gulp master
```
* 结果

```
➜  SuperTestWithGulp git:(master) gulp master
[17:34:44] Using gulpfile ~/Downloads/SuperTestWithGulp/gulpfile.js
[17:34:44] Starting 'master'...
[17:34:44] Finished 'master' after 37 ms
You are in master


  Test Demo.
    ✓ Visit http://aimer1124.github.io/ (502ms)


  1 passing (506ms)
```
* 结果分析：`✓ Visit http://aimer1124.github.io/ (502ms)`表示测试正常通过；`1 passing (506ms)`表示整个测试所执行的时间和测试所执行的数量

# 自动化测试的持续集成
## 持续集成是什么
* `Continuous Integration (CI) is a development practice that requires developers to integrate code into a shared repository several times a day. Each check-in is then verified by an automated build, allowing teams to detect problems early.`

## Travis CI
* 在线CI工具
* 官网：[https://travis-ci.org/](https://travis-ci.org/)

### Travis与Gulp集成
* 使用Git项目[SuperTestWithGulp](https://github.com/aimer1124/SuperTestWithGulp)
* 在项目根目录中添加`.travis.yml`文件，`language`表示使用的语言为`node_js`，`0.12`表示使用`node_js`的版本，`before_script`表示运行脚本前执行的脚本命令，`script`表示启动时的执行脚本

```
language: node_js

node_js:

  - "0.12"

before_script:

  - npm install -g gulp

script: gulp master
```
* 在Travis中关联此Github项目[SuperTestWithGulp](https://github.com/aimer1124/SuperTestWithGulp)


* Travis会在Github代码有`变更`时，`自动`拉取项目的代码并进行`在线集成`

## Jenkins
* `Build great things at any scale`
* 官网：[https://jenkins.io/](https://jenkins.io/)

### Jenkins与Grunt集成
* 安装`NodeJS`、`Git`插件
* 配制`Job`的`build step`中`execute shell`：`npm install && grunt`

* 运行`Job`即可执行API测试


# 总结
* API自动化测试已经说完了，完全没有太复杂的代码和编写难度。
* 使用SuperTest可实现多场景、多环境的API场景测试，且执行速度较[UI自动化测试](http://www.jianshu.com/p/cb24e7fa8f56)快很多。
* SuperTest与Grunt/Gulp的集成很方便，即使在本地进行调试也很快捷。
* 持续集成工具Travis/Jenkins，与API测试集成后，更高效的提高测试效率。

# 参考
* SuperTest
[https://github.com/visionmedia/supertest](https://github.com/visionmedia/supertest)
* Grunt官网
[http://gruntjs.com/](http://gruntjs.com/)
* NPM官网
[https://www.npmjs.com/](https://www.npmjs.com/)
* Gulp官网
[http://gulpjs.com/](http://gulpjs.com/)
* Continuous Integration
[https://www.thoughtworks.com/continuous-integration](https://www.thoughtworks.com/continuous-integration)
* Travis CI
[https://travis-ci.org/](https://travis-ci.org/)
* Jenkins
[https://jenkins.io/](https://jenkins.io/)
* NodeJS
[https://nodejs.org/en/](https://nodejs.org/en/)
* UI自动化测试
[http://www.jianshu.com/p/cb24e7fa8f56](http://www.jianshu.com/p/cb24e7fa8f56)
* Jenkins with Grunt
[http://aimer1124.github.io/2016/03/03/Tool-Jenkins-with-SuperTest-and-Grunt/](http://aimer1124.github.io/2016/03/03/Tool-Jenkins-with-SuperTest-and-Grunt/)



`首发于简书`：[http://www.jianshu.com/p/a3e35928a0aa](http://www.jianshu.com/p/a3e35928a0aa)
