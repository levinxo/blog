Author: Levin
Date: 2019-05-22 16:29
disqus_identifier: 201905221629
Slug: computer-networks-book-report-part4
Title: 《计算机网络》读书笔记整理（4）-- 网络层
Category: Network
Tags: network, book report

### 概述

网络层向上提供简单灵活的、无连接的、尽最大努力交付的数据报服务，不提供服务质量的承诺。发送分组时不需要先建立连接，分组不进行编号，独立发送。

网际协议IP是网络层协议，是TCP/IP体系中最重要的协议之一。

与IP协议配套使用的协议有三个：

* 地址解析协议ARP（Address Resolution Protocol）
* 网际控制报文协议ICMP（Internet Control Message Protocol）
* 网际组管理协议IGMP（Internet Group Management Protocol）

将各个单独的网络互连起来需要使用中间设备，其中网络层使用的中间设备叫做路由器（router）。路由器是一台专用计算机，用来在互联网中进行路由选择。路由器由路由选择和分组转发部分组成。

物理地址是数据链路层和物理层使用的地址，而IP层是网络层和以上各层使用的地址，是一种逻辑地址。

在路由表里每行记录的主要信息有三个，目的网络地址+子网掩码+下一跳地址。

目前通常使用的路由表查找算法是使用二叉线索（binary trie），并在此基础上使用了压缩技术，以提高路由查找效率。

### ARP和ICMP

在多个网络间分组转发的时候，经常需要使用ARP协议通过IP地址获得MAC地址。每台主机都设有一个ARP高速缓存，里面有各主机和路由器IP地址到MAC地址的映射表。ARP协议通过广播ARP请求分组并接收ARP响应分组来获得IP地址到MAC地址的映射。

ICMP协议允许主机或路由器报告差错情况和提供有关异常情况的报告。分为差错报告报文和询问报文两种。

### IP地址编址方法

IP地址长度为32位，一般用点分十进制法表示。IP地址编址方法共经历过了三个历史阶段。

* 分类的IP地址
* 子网的划分
* 构成超网

第一个历史阶段分类的IP地址利用率很低且不够灵活，第二个历史阶段给IP地址中增加了一个『子网号字段』，两级IP地址变成了三级，这种方法就是划分子网。

划分子网的具体方法是从网络的主机号借用若干位作为子网号（subnet-id），这时主机号也减少了相应的位数。于是两级IP地址在本单位内部就变为了三级IP地址。

当一个网络包到达本单位时，单从IP地址和IP包头部信息无法得知子网划分的信息。这时需要通过子网掩码来获得目标主机的网络号，子网掩码和IP地址进行逐位相与后就可得到网络地址。

由于IP地址消耗很快，且路由表中的数目急剧增长，第三个历史阶段使用了无分类域间路由选择CIDR（Classless Inter-Domain Routing）。取消了传统的ABC类地址和划分子网的概念，使用无分类的两级编址。

CIDR使用斜线记法，在IP地址后加上斜线，并写上网络前缀所占的位数。这样一个CIDR地址块有多个地址，路由表就可以利用CIDR地址块来查找目的网络。使得路由表中一个项目可以表示原来传统分类地址的很多个路由，这种地址聚合叫路由聚合，也叫构成超网。

### 路由协议

互联网采用分层次的路由协议，分为内部网关协议IGP和外部网关协议EGP。内部网关协议有RIP和OSPF等，外部网关协议有BGP。

内部网关协议RIP（Routing Information Protocol）是最先得到广泛使用的内部网关协议。是分布式的基于距离向量的路由选择协议，实现简单，开销小。   
开放最短路径优先OSPF（open shortest path first）是为了克服RIP的缺点开发出来的。OSPF最主要的特征就是使用分布式的链路状态协议（link state protocol）。

RIP和OSPF的异同：

* RIP：
    * RIP分组使用UDP报文传送。
    * 定期向相邻的路由发送自己所知的全部网络距离（网络距离用跳数来衡量）和下一跳路由器，此信息即路由表。
    * 使用距离向量算法。
    * 在自治系统内传播，没有全部网络的拓扑信息，所以只能找出到某个网络的一条路径。
    * 发现拓扑有变化时，向相邻路由发送更新后的路由表，全网全部更新完成耗时较多。坏消息传得慢。

* OSPF：
    * OSPF分组使用IP数据报传送。
    * 初始化时通过分组类型里的问候、数据库描述、链路状态请求分组来进行路由器自身的路由数据库构建。
    * 使用最短路径算法（SPF），通过链路度量（距离、时延、带宽等）来判断到达其它路由器的代价，将自治系统划分为更小的区域以及使用层次划分的结构。
    * 有全部的网络拓扑，所以能同时使用多条代价相同的路径，达到负载平衡的目的。
    * 发现拓扑有变化时，使用可靠的洪泛法向当前区域发送链路状态更新分组，全网全部更新完成耗时非常少。坏消息传得快。

EGP目前主要使用边界网关协议BGP，BGP力求寻找一条能到达目的网络且比较好的路由，并不是要寻找最佳路由。

BGP采用路径向量（path vector）路由选择协议，每个自治区域至少有一个BGP发言人。BGP发言人互相之间通过TCP建立BGP会话，并通过BGP报文交换路由信息。交换的网络可达性信息就是要到达某个网络所需要经过的一系列自治系统。

### IPv6

IPv6和IPv4的一些区别：

* IPv6地址位数为128位，比IPv4大了4倍。
* IPv6的首部和IPv4并不兼容，路由器对IPv6的扩展首部不处理。
* IPv6的首部长度固定，选项和数据部分放在有效载荷中，路由器只处理头部，提高了转发效率。
* IPv6即插即用，不需要DHCP。
* 支持通过流标号对资源的预分配，让带宽和时延对多媒体资源更友好。
* 取消了检验和字段，加快了路由器处理速度。
* IPv6使用冒号十六进制记法，可以使用零压缩进行简化。

从IPv4切换到IPv6采用逐步演进的办法：双协议栈和隧道技术。

### VPN和NAT

虚拟专用网VPN（Virtual Private Network）主要使用隧道技术实现，满足多地部门交换信息的需求。

网络地址转换NAT（Network Address Translation）是指只有本地地址的主机在和外界通信时，NAT路由器将分组里的本地地址转换为全球IP地址；当NAT路由器收到分组时，通过NAT地址转换表，把目的地址转换为本地主机的地址再转发到对应主机。

把运输层的端口也利用上，就可以更加有效利用NAT路由器的全球IP地址。使用端口号的NAT叫做网络地址与端口号转换NAPT。

---

参考文献：  
[1] 谢希仁. [计算机网络（第7版）](https://www.bicky.me/url.html#https://book.douban.com/subject/26960678/)[M]. 北京：电子工业出版社，2017.

