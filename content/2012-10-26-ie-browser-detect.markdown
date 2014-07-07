Author: levin
Date: 2012-10-26 18:13
disqus_identifier: 201210261813
Slug: ie-browser-detect
Title: IE系列浏览器判断，包含IE9
Category: Web
Tags: javascript

<!-- more -->

    var ie = ! ','.split(/,/).length;

之前使用的：

    var ie = ! + [1, ];

不能用于判断IE9

摘自：http://blog.csdn.net/satans18/article/details/5502129
