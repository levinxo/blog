Author: levin
Date: 2015-02-21 15:00
disqus_identifier: 201502211500
Slug: nginx-proxy-directory-slash-redirect
Title: Nginx反向代理的文件目录重定向
Category: Web
Tags: nginx

目前将托管在[Github](/url.html#https://pages.github.com/)的静态博客迁移到了Linode上的Nginx服务器，在接入层使用Nginx proxy进行分流，接入http和https请求，然后转发至下层的Nginx服务器。<!-- more -->

当访问80端口时，由[firewalld](/url.html#https://fedoraproject.org/wiki/FirewallD)将请求转发至8080端口给Nginx proxy，Nginx proxy再将请求转发到8000端口给下游Nginx处理。

###问题：

* 访问`http://server_name/folder/`时表现正常。

* 访问`http://server_name/folder`时下游Nginx将请求重定向到了`http://server_name:8000/folder/`。

原因是请求到达下游的Nginx时服务器认为hostname是server_name:8000，从而无法正确重定向。

###解决方案：

在Nginx proxy的配置文件里加入`proxy_redirect`项将下游Nginx响应header里对应的Location值改为正确的URL。

	location / {
        proxy_pass http://127.0.0.1:8000;
        #将重定向中的端口号去除
        proxy_redirect http://$server_name:8000/ http://$server_name/;

        proxy_set_header   Host            $host;
        proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
    }

这下问题解决。

Reference:

1. [Module ngx_http_proxy_module proxy_redirect](/url.html#http://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_redirect)
2. [Nginx + Apache trailing slash redirect - Server Fault](/url.html#http://serverfault.com/questions/174297/nginx-apache-trailing-slash-redirect)

