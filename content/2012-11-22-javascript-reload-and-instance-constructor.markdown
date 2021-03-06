Author: levin
Date: 2012-11-22 07:17
disqus_identifier: 201211220717
Slug: javascript-reload-and-instance-constructor
Title: javascript中函数返回函数，重载以及对象实例化相关
Category: Program language
Tags: javascript

第一个是最常见的，普通的函数，函数返回的是number类型的值

<!-- more -->

![第一个例子变量test获取到的是函数的返回值，类型是number](http://ww3.sinaimg.cn/large/0069yvRGgw1etc586qqynj30em05ut8u.jpg)

第二个是函数中返回函数的函数，并且此函数的toString方法被重载了，因此在直接输出test值的时候其返回的就是重载以后的toString函数给的返回值

![第二个例子变量test获取到的是函数的返回值，类型是function，并且此函数的toString方法被重载了](http://ww3.sinaimg.cn/large/0069yvRGgw1etc58518m1j30f80biaam.jpg)

第三个函数无返回值，因此试图直接获取此函数的返回值时只会获取到undefined，所以只有实例化此函数，将之变为对象，就能调用其函数体内各种属性和方法了，其toString方法也被重载了

![第三个例子函数无返回值，或者说其返回值为undefined，因此必须使用new实例化此函数](http://ww3.sinaimg.cn/large/0069yvRGgw1etc585wnhpj30jh0980t5.jpg)
