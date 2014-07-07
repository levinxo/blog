Author: levin
Date: 2012-11-29 14:21
disqus_identifier: 201211291421
Slug: php-getallheaders-didnt-work-in-nginx
Title: php的getallheaders函数在nginx下失效的解决办法
Category: Web
Tags: apache,nginx,PHP

今天将apache下的php应用部署到了nginx上，却发现报错：找不到getallheaders()这个函数。

很惊奇，这不是php的默认函数么，怎么给我找不到了。但问题就是出现了，只能去找解决方法。

原来此函数是apache\_request\_headers()函数的别名，看到了吧，带有apache的血统，因此nginx不能用很正常了。<!-- more -->

找到原因了，还是需要解决方案的，在php手册里找到了此函数的写法，于是摘抄下来，方便以后查看：

    <?php
    if (!function_exists('getallheaders')) {
    	function getallheaders() {
    		foreach ($_SERVER as $name => $value) {
    			if (substr($name, 0, 5) == 'HTTP_') {
    				$headers[str_replace(' ', '-', ucwords(strtolower(str_replace('_', ' ', substr($name, 5)))))] = $value;
    			}
    		}
    		return $headers;
    	}
    }
    //over
