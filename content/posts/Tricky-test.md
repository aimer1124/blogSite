---
title: 'Tricky test scenario'
tags:
  - Test scenario
  - Testing
categories:
  - Testing
date: 2016-01-30 18:47:00
---
## 测试`验证码`，收到客户投诉
* Scenario
 - 作为普通用户,在用户注册时，可通过获取短信码使用手机号进行注册
* 功能
 - 用户注册时，需要测试手机号码与获取的短信码是否能正常收到且匹配。
 - 短信验证码由本项目生成,但由第三方来发送
 - 验证码发送是由第三方提供的，无法完全Mock
 - 数据库中会记录收到的短信验证码.
* 测试策略
 - 测试验证码能否匹配时,用了自己的手机号码来测试.
 - 后面再测试是否匹配时,发现没有手机号码可用,就 **随机** 输入了手机号码进行测试,通过查询数据库来获取验证码
* Tricky
 - 如上进行了一阵子测试,由于是国内某银行项目,后面就收到了客户投诉: **没有进行任何的操作,便收到了短信验证码**
* 分析
 - 是否每次测试时,都需要通过第三方来发送短信验证码.
 - 仅Mock第三方收到请求,不需要每次都真实的发送短信功能
* TIPS
 - 测试中,一定要确保 **普通用户** 不会收到短信验证码

<!-- more -->

## 同样`返回内容`,在不同的浏览器中显示不同
* Scenario
 - 作为普通用户,在浏览页面时,可查看到Title显示的内容
* 功能
 - 需要从第三方系统中获取指定的内容,返回给浏览器,并显示到Title
* 测试策略
 - 为确保兼容性,使用不同的浏览器进行查看
 - 涉及浏览器: **Chrome,FireFox,IE**
* Tricky
 - 仅Chrome查看正常显示,FireFox/IE查看均会显示 **部分** 乱码
* 分析
 - 返回的内容中有 **Unicode** 值为15的内容,这个返回值引起的显示乱码
* TIPS
 - 在对第三方集成时,一定要先针对所有输入/输出内容均进行字符集处理.确保所用的字符集均一致

## 同样的`样式`，在同一类浏览器中显示不同
* Scenario
 - 作为普通用户，在浏览页面时，可查看到正确的页面显示与布局
* 功能
 - 在页面布局测试时，需要查看页面的显示与布局的正确性
* 测试策略
 - 使用浏览器查看页面的显示与布局
* Tricky
 - 在测试电脑中，发现页面的布局中的样式有问题（按钮被换行）
 - 在DEV的电脑中完全是好的（使用的同一发布版本进行测试）
* 分析
 - 浏览器的版本是完全一致
 - 浏览器的 **缩放比例** 不同，测试电脑的页面被设置为 **缩放90%**
* TIPS
 - 在测试页面的显示和样式时，一定要确保页面 **浏览器版本、页面缩放** 完全一致

## PaaS平台部署后，时间出现`偏差`
* Scenario
 - 作为普通用户，在注册新用户时，需要使用获取的验证码在5分钟内进行验证，否则验证码失效
* 功能
 - 页面前端点击 **获取验证码** 后，需要在生成验证码5分钟内，进行注册
 - 生成的验证码会存储在 **数据库** 中
 - 生成验证码是由程序代码生成，有效期的验证是由生成验证码时生成的**Createtime**和**当前时间**比较
* 测试策略
 - 在点击 **获取验证码** 后，从数据库中查询生成的 **验证码**
 - 通过查询的验证码，进行用户注册
* Tricky
 - 在点击 **获取验证码** 后，直接去数据库中查询**验证码**
 - 使用查询获取的**验证码**，在进行用户注册时，提示验证码已过期(查询与注册的时间操作差，**绝对**在5分钟内)
* 分析
 - 此功能在非[PaaS](https://en.wikipedia.org/wiki/Platform_as_a_service)平台时完全正常的
 - 部署到Paas平台后，在[PaaS](https://en.wikipedia.org/wiki/Platform_as_a_service)平台时，程序代码是部署到一台机器、数据库部署在**另外**一台机器
 - 验证码的生成时间是由数据库脚本生成，获取的数据库的当前插入时间
 - 验证码有效期验证时，**当前时间**为从**程序代码**部署的机器获取**当前系统时间**
 - 两台部署机器时区设置不一致(程序代码：**Asia/Shanghai**，数据库:**Etc/Zulu**)，两个时区相差8小时
* TIPS
 - 部署环境时，一定要先确保时间的设置是否会对功能有影响
 - 涉及到时间处理时，一定确保使用的是**统一**的参考时间

## Mock的模块在集成后，Mock相关的`功能出错`
* Scenario
 - 作为普通用户，在查看个人账户时，可查看到账户余额
* 功能
 - 普通用户在查看个人账户时，需要通过系统去查询第三方系统数据
 - 在开发环境中第三方系统无法直接连接进行调试开发，因此提前做了Mock进行开发
* 测试策略
 - 测试时，正常使用个人账户查询结果
* Tricky
 - 在到**ST测试**环境时，无法正常查询账户余额。数据解析报错
* 分析
 - 使用Mock返回的数据时，在ST环境可正常查询
 - 但使用第三方**真实**返回的数据查询时，在ST便会报错
 - 对**真实**数据进行分析，发现**数据结构**已与之前Mock的不同
* TIPS
 - 针对Mock系统，一定要有对应的测试，确保接口的正确性及数据正确性
 - 针对需要Mock的功能，一定要定期与集成方沟通，确保开发功能、接口变同的同步

## 特定文件内容无法上传到`生产环境`，其它环境均正常
* Scenario
 - 作为注册用户，在个人信息中，可上传文档
* 功能
 - 注册用户，可使用**上传文档**功能，上传个人文档
 - 针对上传的文件内容及类型均无限制（由于系统是**特定**人群使用，所以对文件**类型**均没有限制），**文件大小**此处不考虑
*  测试策略
 - 针对上传文件类型进行测试：txt/exe/pdf/doc等
* Tricky
 - 上传txt/html时，若文件以**<**开头时，上传功能在其它环境均可正常使用，但在生产环境则上传会失败
* 分析
 - 生产环配制有网关，会对文件内容进行过滤
 - 若文件html/js/txt文件中以**<**开头时，则会被判断为**注入**文件
* TIPS
 - 作为测试人员，也要对**安全测试**常出现的问题进行考虑

## 参考资料

* PAAS：[https://en.wikipedia.org/wiki/Platform_as_a_service](https://en.wikipedia.org/wiki/Platform_as_a_service)
* 时区差：[https://en.wikipedia.org/wiki/List_of_tz_database_time_zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
* Asia/Shanghai:[https://en.wikipedia.org/wiki/Asia/Shanghai](https://en.wikipedia.org/wiki/Asia/Shanghai)
* Etc/Zulu:[http://www.prokerala.com/travel/timezones/Etc/Zulu](http://www.prokerala.com/travel/timezones/Etc/Zulu)
* Mock：[https://en.wikipedia.org/wiki/MockServer](https://en.wikipedia.org/wiki/MockServer)
* ST测试：[https://en.wikipedia.org/wiki/System_testing](https://en.wikipedia.org/wiki/System_testing)
* 安全测试：[http://www.ltesting.net/ceshi/ceshijishu/aqcs/2015/0104/207771.html](http://www.ltesting.net/ceshi/ceshijishu/aqcs/2015/0104/207771.html)
