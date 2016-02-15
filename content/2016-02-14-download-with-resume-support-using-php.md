Author: levin
Date: 2016-02-14 20:25
disqus_identifier: 201602142025
Slug: download-with-resume-support-using-php
Title: 下载断点续传原理和PHP实现
Category: Web
Tags: PHP

今天研究下载的断点续传。<!-- more -->

## 1 断点续传的原理
下载时的断点续传是指在下载的时候，将一个下载资源分为几部分依次下载，碰到网络问题时用户不必重新下载完整的资源，只要把未完成的部分重新下载即可。当然也可以同时下载不同的部分以节省时间。

当客户端发起定向到资源某部分的请求时，服务器声明支持断点续传，并告诉客户端返回了资源的哪部分以及对应部分的资源实体。

## 2 实现步骤

### 2.1 客户端发起请求
首先，下载的请求由客户端发起，如果请求的头部中带了range字段，说明是请求资源的某一部分。range字段可能有几种情况，下面分别列出：

```
Range: bytes=0-499
Range: bytes=-500
Range: bytes=9500-
Range: bytes=0-0,-1
Range: bytes=500-700,601-999
```

1. 第一种情况表示取0-499这500个字节
2. 第二种情况表示取最后500个字节
3. 第三种情况表示取offset为9500到最末的所有字节
4. 第四种情况表示取第一个和最后一个字节的集合
5. 第五种情况表示取500-999这500个字节

其中第4、5种情况稍微复杂，请求了多个部分或是重叠请求。我们要从这几种情况获得客户端最终需要资源range的start和end。

### 2.2 服务器返回内容
接着，服务器知道客户端需要的range之后，如果range合法（start不小于0，start不大于end，range大小不大于资源大小），则返回206的http状态码并声明range，同时将资源按照range截取出来放入body中一起返回。

```
HTTP/1.1 206 Partial content
Accept-Ranges: bytes
Content-Range: bytes 21010-47021/47022
```

否则返回416http状态码并告诉客户端正确的offset范围：

```
HTTP/1.1 416 Requested range not satisfiable
Content-Range: bytes */47022
```

实现断点续传的逻辑之后可以使用wget命令进行测试（-c即--continue，意思是支持断点续传）。

`wget -c -o "test.zip" "http://example.com/abc.zip"`

### 2.3 代码实现
目前使用php实现了这个逻辑，供参考：[代码](/url.html#https://github.com/levinxo/serendipity/blob/master/php_resume_download_func.php)

--EOF--

Reference:

1. [Range](/url.html#https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35)
2. [Accept-Ranges](/url.html#https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.5)
3. [Content-Range](/url.html#https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16)


