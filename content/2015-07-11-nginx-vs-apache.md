Author: levin
Date: 2015-07-11 22:40
disqus_identifier: 201507112240
Slug: nginx-vs-apache
Title: Nginx和Apache的区别
Category: Web
Tags: nginx,apache

###Nginx

Nginx使用epoll或kqueue网络模型，异步非阻塞。Nginx把每次请求都划分成了事件。例如accept、recv、磁盘io、send等，每部分都有对应模块响应。<!-- more -->

处理的核心在于事件收集和分发到模块，只有在对对应模块调度时才让该模块占用CPU资源。在Nginx进程里，一个请求被分成很多阶段，每个阶段都到对应模块注册，处理，完毕再通知进程事件已经完成。

Nginx不会为每个请求新建进程，我们可以设置Nginx开启的进程数，一般设置每个核绑定一个进程，每个进程都是单线程，可以异步处理数千个并发请求。

###Apache

Apache使用select网络模型，依赖于进程和线程，同步阻塞，多进程（prefork）或多线程（worker）工作。
Apache的MPM可以设置使用prefork或者worker模式，当请求到来时，两种方式都会创建新进程，区别在于prefork的每个进程只处理一个请求，而worker在进程下开启多个线程处理请求，一个线程对应一个请求。

同等请求条件下，worker会比prefork使用更少的内存，因为线程比进程消耗的内存更少。

在prefork模式下，进程数会随着请求数的增加而增加。一个请求会阻塞在一个进程里，请求数增多时Apache要生成更多的进程响应，CPU对于进程的切换就会比较频繁，且过多的进程会耗尽内存从而使系统使用磁盘的交换内存，导致性能下降。

###各自适合的业务场景

Nginx适合作为反向代理服务器，阻塞的事情丢给后端，Nginx负责转发请求和回传响应即可，因为基于事件驱动，进程只处理有响应的io事件，CPU和内存消耗的比较少。

Apache适合作为应用服务器，处理后端业务更擅长。Apache基于进程和线程的模型应该让它静静地去处理业务。
不过如果是运行php的话，更建议直接使用php-fpm和Nginx进行交互，而不是Apache的mod_php。


