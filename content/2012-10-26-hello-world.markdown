Author: Levin
Date: 2012-10-26 16:13
Modified: 2019-05-26 03:05
disqus_identifier: 201210261613
Slug: hello-world
Title: Hello world!
Category: 随笔

折腾了很久，找了很多的云服务，终于打算在openshift安家了。

之前试过了很多的云服务器，PaaS(平台即服务)理念在国外云服务商贯彻的很透彻，国内目前就新浪的sae能看看吧。

最初接触的是sae，国内访问速度很快。随着用户的增多，sae再也不喊免费的口号了，打算每天都收费。于是着手开始寻找新的云平台。<!-- more -->

首先是dotcloud，dotcloud新手的话上手难度比较大，不过也就如此。它的速度还不错，可以架设多种语言的应用，其收费和免费其实差不多，只是免费的不能绑定域名而已。

然后找到了appfog，原本的名字是php fog，速度很不错，比dotcloud还快，上手程度也简单多了，而且支持免费绑定域名，每个开发者都有2g的ram提供，应用上限为10个，ram可给每个应用灵活调整。

再次是zend的phpcloud，此云在国内访问速度一般，感觉不是很稳定，上手程度也挺快的。

最后试了redhat的openshift，速度比appfog稍慢，和dotcloud差不多，可以免费绑定域名。这个平台需要自己制作openssh或者ppk密钥。

折腾了一个星期将近，决定了openshift，毕竟是redhat的，可靠性应该不错。做了选择，就开始动手，安装php应用，mysql数据库，架设wordpress，制作密钥，绑定域名，重定向域名，终于搞定。

谨以此文纪念我折腾云服务的小插曲。

---

更新于2013-10-20：

用了小红帽家的openshift大概4个月吧，到了今年3月的时候，openshift很难连接上了，
查看[openshift服务器状态](/url.html#https://openshift.redhat.com/app/status)却是`No open issues`。
所以被迫将[博客转移到了sae](/blog/archive/my-blog-moved-to-sae-from-rhcloud/)上，挥泪告别可爱的小红帽。

在7月份的时候，觉得wordpress写博客不够有趣，而且sae又无法在不备案的情况下真正地绑定域名，
所以就将[博客转移到了github](/blog/archive/my-pagination-on-homepage-base-on-jekyll-pagination-plugin/)，
目前为止运行状态良好。

---

更新于2014-08-08：

到2014年7月，正好使用jekyll一年，想尝试python写的静态站点生成软件，找到了[pelican](/url.html#https://github.com/getpelican/pelican)。花了几天时间迁移之前的文章，为站点加入主题和各种插件。目前博客源码在[这里](/url.html#https://github.com/levinxo/blog)，欢迎查看，其中的webroot文件夹为submodule（子模块），用于存放站点生成的静态文件。

---

更新于2015-02-19：

2015年2月，整个blog通过pelican生成的静态文件已从github page迁移至linode服务器上，同时支持http和[https](https://www.bicky.me/)访问，站点生成器依旧是pelican。

---

更新于2019-05-26：

2019年4月，用GO写了个静态博客生成器，并把原先用pelican生成的内容无缝迁移了过来。

