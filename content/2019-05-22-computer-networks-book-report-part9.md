Author: Levin
Date: 2019-05-22 16:34
disqus_identifier: 201905221634
Slug: computer-networks-book-report-part9
Title: 《计算机网络》读书笔记整理（9）-- 无线网络和移动网络
Category: Network
Tags: network, book report

### 无线局域网WLAN

#### 无线局域网分类

* 有固定基础设施的
    * 802.11是一个无线局域网的协议标准，使用星形拓扑，中心接入点叫AP（Access Point），在MAC层使用CSMA/CA协议。802.11里无线互联网的最小构件是基本服务集BSS（Basic Service Set），包含一个基站（base station）和多个移动站。
* 无固定基础设施的
    * 自组网络（ad hoc network）没有接入点AP，而是由移动站相互通信组成的临时网络。

#### CSMA/CA协议

CSMA/CA协议即载波监听多点接入/碰撞避免，类似CSMA/CD协议，只是从碰撞检测变为了碰撞避免，CA表示Collision Avoidance，协议的设计目标是尽量减少碰撞发生的概率。

CSMA/CA还使用了停止等待协议，发送方必须等待对方的确认帧。通过帧间间隔IFS（InterFrame Space）和二进制指数退避算法来尽量避免碰撞，另外允许对信道进行预约。

### 无线个人区域网WPAN

无线个人区域网WPAN有蓝牙系统、低速WPAN（有ZigBee实现）、高速WPAN等

### 蜂窝移动通信网

#### 蜂窝移动通信

移动通信使用最多的是蜂窝移动通信，又称为小区制移动通信。把整个的网络服务区划分成许多小区（cell），每个小区设置一个基站负责移动站的通信和控制，基站再和无线网络控制器RNC（Radio Network Controller）进行通信，通过RNC再和各子系统配合可以进行语音通话和数字通信。

#### 移动IP

移动IP，也称为移动IP协议，允许计算机移动到外地时，仍然保留原先的IP地址。

移动站拥有一个原始地址，即归属地址（home address），属于归属网络（home network），归属代理（home agent）是在归属网络上的路由器。

当移动站到另外一个网络时，称为外地网络（foreign network），被访网络使用的代理叫外地代理（foreign agent）。此时外地代理为移动站创建一个转交地址（care-of address），并把该地址通知给归属代理。

此后发送给移动站的数据报将通过归属代理和外地代理来转发给移动站。

这种间接的路由选择，可能会导致数据转发低效，称为三角形路由选择问题（triangle routing problem）。可用直接路由选择来解决。

---

参考文献：  
[1] 谢希仁. [计算机网络（第7版）](https://www.bicky.me/url.html#https://book.douban.com/subject/26960678/)[M]. 北京：电子工业出版社，2017.

