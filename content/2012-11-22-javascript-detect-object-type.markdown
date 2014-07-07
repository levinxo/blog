Author: levin
Date: 2012-11-22 14:37
disqus_identifier: 201211221437
Slug: javascript-detect-object-type
Title: javascript验证对象类型
Category: Program language
Tags: javascript

在书上看到一个js验证对象类型的自定义函数，能准确的判断各种对象类型，摘录如下。<!-- more -->

    //为对象增加自定义方法
    Object.prototype.InstanceOf = function (type) {
    	try {	//只要其中一个判断能对上，即返回true
    		return typeof(this) == type ||
    		this.constructor == type ||
    		this instanceof type;
    	} catch (ex) {
    		return false;
    	}
    }
    var a = new Array();
    alert(a.InstanceOf(Array));
    //返回true
