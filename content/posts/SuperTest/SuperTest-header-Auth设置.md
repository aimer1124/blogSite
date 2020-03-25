---
title: 'SuperTest-header:Auth设置'
tags:
  - API测试
  - SuperTest
categories:
  - Tool
date: 2016-02-28 21:36:00
---
# SuperTest

* [SuperTest-API测试](http://aimer1124.github.io/2016/01/17/SuperTest/)

# Auth分类

## [Basic](https://en.wikipedia.org/wiki/Basic_access_authentication):基本身份认证，直接采用：用户名密码

* 基本用法
```javascript
it('should receive a status code of 200 with login', function(done) {
    request(url)
        .get('/staging')
        .auth('the-username', 'the-password')
        .expect(200, done);
});
```
* Base64加密

```javascript
.set("Authorization", "basic " + new Buffer("username:password").toString("base64"))
```

<!-- more -->

## [Digest](https://en.wikipedia.org/wiki/Digest_access_authentication):摘要式身份认证

```javascript
request.get('http://some.server.com/').auth('username', 'password', false);
// or
request.get('http://some.server.com/', {
  'auth': {
    'user': 'username',
    'pass': 'password',
    'sendImmediately': false
  }
});
// or
request.get('http://some.server.com/').auth(null, null, true, 'bearerToken');
// or
request.get('http://some.server.com/', {
  'auth': {
    'bearer': 'bearerToken'
  }
});
```

## [OAuth Authentication](http://oauth.net/core/1.0/)

* 例子

```javascript
var OAuth = require('openauth');
var request = require('superagent');

require('superagent-openauth')(request);

var oauth = new OAuth(consumerKey, consumerSecret, {...});

request.post('https://api.twitter.com/1.1/statuses/update.json')
  .sign(oauth, token, tokenSecret)
  .type('urlencoded')
  .send({status: 'hello world'})
  .end(function(res) {
    console.log(res.status, res.body);
  });
```

* OAuth 1

```javascript
request.sign(oauth, token, secret);
```

`
oauth: OAuth instance
token: string access token
secret: string access token secret
`

* OAuth 2

```javascript
request.sign(oauth, token);
```

`
oauth: OAuth2 instance
token: string access token
`

## [Kerberos](http://searchsecurity.techtarget.com/definition/Kerberos)

* 完成二次认证交互，第三次再进行业务交互。传输过程中没有密码
* [示意图](https://www.google.com.hk/search?q=kerberos&tbm=isch&imgil=g3XTdJDBk9BSEM%253A%253BgqDVyMEXFduCpM%253Bhttps%25253A%25252F%25252Fmsdn.microsoft.com%25252Fen-us%25252Flibrary%25252Fbb742516.aspx&source=iu&pf=m&fir=g3XTdJDBk9BSEM%253A%252CgqDVyMEXFduCpM%252C_&usg=__gboKjk2d4nP_O26E2iFaegFIK5g%3D&biw=1393&bih=782&ved=0ahUKEwisyL2D4JbLAhXDbSYKHWnICBEQyjcIVQ&ei=LvbQVqz5H8PbmQHpkKOIAQ#imgrc=g3XTdJDBk9BSEM%3A)

# 参考资料

* Authentication分类介绍: [http://docs.python-requests.org/en/master/user/authentication/](http://docs.python-requests.org/en/master/user/authentication/)
* Basic Authentication: https://en.wikipedia.org/wiki/Basic_access_authentication(https://en.wikipedia.org/wiki/Basic_access_authentication)
* Digest Authentication: [https://en.wikipedia.org/wiki/Digest_access_authentication](https://en.wikipedia.org/wiki/Digest_access_authentication)
* Kerberos：[http://searchsecurity.techtarget.com/definition/Kerberos](http://searchsecurity.techtarget.com/definition/Kerberos)
* Kerberos Explained:[https://msdn.microsoft.com/en-us/library/bb742516.aspx](https://msdn.microsoft.com/en-us/library/bb742516.aspx)
* Superagent-openauth:[https://www.npmjs.com/package/superagent-openauth](https://www.npmjs.com/package/superagent-openauth)
