Author: Levin
Date: 2019-05-22 16:31
disqus_identifier: 201905221631
Slug: computer-networks-book-report-part6
Title: 《计算机网络》读书笔记整理（6）-- 应用层
Category: Network
Tags: network, book report

不同的网络应用之间，需要有不同的通信规则，因此产生了应用层协议。

### 域名系统DNS

域名系统DNS（Domain Name System）是互联网使用的命名系统，将域名转换为IP地址。使用UDP运输层协议。

DNS服务器按照层次安排，根据域名服务器的作用，分类如下：

1. 根域名服务器。当本地域名服务器无法解析时，会向根域名服务器发起请求，得知应该去哪个顶级域名服务器进行查询。采用anycast（任播，不同地点主机，IP地址相同，网络分组交付最近一台主机）技术。
2. 顶级域名服务器。管理某个顶级域名下的所有二级域名。
3. 权限域名服务器。负责一个区的域名服务器，区不会大于域。
4. 本地域名服务器。接收主机发送过来的DNS查询请求。

域名的解析过程：

1. 一般情况下主机向本地域名服务器发起递归查询请求。
2. 本地域名服务器向根服务器发起迭代查询请求或递归查询请求。

域名服务器中广泛使用了高速缓存对DNS记录进行保存，提升整体查询效率。

### 文件传送协议FTP

文件传送协议（File Transfer Protocol）提供文件传送的基本服务，主要是为了消除不同操作系统下处理文件的不兼容性，使用TCP进行可靠传输。

FTP服务器进程由两大部分组成，一个主进程，负责接收新请求；若干个从属进程，负责处理单个请求。从属进程又分为控制进程和数据传送进程。

### 远程终端协议TELNET

远程终端协议TELNET通过TCP连接登录到远程机器的应用进程上进行交互和数据传输。

### 万维网WWW

万维网WWW（World Wide Web）是一个大规模的、联机式的信息储藏所，简称Web。

万维网的组成：

* 万维网使用统一资源定位符URL（Uniform Resource Locator）标识各种文档。
* 万维网的客户端和服务器程序之间交互遵守超文本传送协议HTTP（HyperText Transfer Protocol），使用TCP进行可靠传输。
* 万维网使用超文本标记语言HTML（HyperText Markup Language）将Web页面显示出来，同时用户可以使用搜索引擎查找所需信息。

HTTP协议是无连接的，即交换HTTP报文前不需要先建立HTTP连接。同时HTTP也是无状态（stateless）的和面向文本（text-oriented）的，一般使用Cookie在服务器和客户端之间传递状态信息。

HTTP1.1协议的持续连接有两种工作方式：非流水线方式（without pipelining）和流水线方式（with pipelining）

通用网关接口CGI（Common Gateway Interface）是一种标准，定义了动态文档如何创建，输入数据如何提供给CGI应用程序，输出结果如何使用。服务器与CGI的通信遵循CGI标准，『通用』是因为该标准的规则对任何编程语言都是通用的，『网关』是因为CGI程序还可能访问其它的服务器资源。Web服务器使用fork+execute方式来调用CGI应用程序。

### 电子邮件系统

电子邮件系统由用户代理、邮件服务器组成。发送协议有简单邮件传送协议SMTP（Simple Mail Transfer Protocol），读取协议有邮局协议POP3（Post Office Protocol 3）和网际报文存取协议IMAP（Internet Message Access Protocol）

由于SMTP只能传送7位的ASCII码，不能传送多媒体文件，于是产生了通用互联网邮件扩充MIME（Multipurpose Internet Mail Extensions）。MIME增加了邮件主体的结构，定义了传送非ASCII码的编码规则。

### 动态主机配置协议DHCP

动态主机配置协议DHCP（Dynamic Host Configuration Protocol）提供了一种即插即用连网的机制，允许计算机加入新的网络和获取IP地址而不用人工参与，使用UDP协议实现。

### 网络的系统调用

大多数操作系统使用系统调用（system call）的机制在应用程序和操作系统之间传递控制权。系统调用接口是应用进程的控制权和操作系统的控制权进行转换的一个接口，也叫应用编程接口（Application Programming Interface）。

可供应用程序使用TCP/IP的应用编程接口其中一种实现方式叫套接字接口（socket interface）。应用进程需要使用TCP/IP进行通信时，通过套接字接口进行系统调用即可。

---

参考文献：  
[1] 谢希仁. [计算机网络（第7版）](https://www.bicky.me/url.html#https://book.douban.com/subject/26960678/)[M]. 北京：电子工业出版社，2017.

