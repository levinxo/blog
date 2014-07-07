Author: levin
Date: 2013-06-01 16:48
disqus_identifier: 201306011648
Slug: configure-apache-and-php-in-osx-mountain-lion
Title: mac10.8.3配置apache+php5
Category: Web
Tags: apache,mac,PHP

首先查看apache是否已经默认安装，一般都默认装好了：<!-- more -->

    sudo apachectl start

打开浏览器，查看localhost，若显示it works!则已经安装好了apache且已正常工作。

然后编辑apache配置文件：

    sudo vim /etc/apache2/httpd.conf

找到#LoadModule php5\_module libexec/apache2/libphp5.so然后去掉之前的注释

配置php文件夹路径(默认的路径为/Library/WebServer/Documents)：

找到DocumentRoot "/Library/WebServer/Documents"和&lt;Directory "/Library/WebServer/Documents"&gt;，将其默认路径改为你以后想放置php脚本的文件夹路径。

然后打开php脚本文件夹，编辑index.php加入

    <?php
    phpinfo();

最后打开localhost/index.php，完成。
