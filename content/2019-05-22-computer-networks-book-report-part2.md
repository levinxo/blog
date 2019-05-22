Author: Levin
Date: 2019-05-22 16:27
disqus_identifier: 201905221627
Slug: computer-networks-book-report-part2
Title: 《计算机网络》读书笔记整理（2）-- 物理层
Category: Network
Tags: network, book report

通信的目的是传输消息（message），数据（data）是运送消息的实体。信号（signal）是数据的电气或电磁表现

根据信号取值方式不同，信号可分为两类：

* 模拟信号，或连续信号。信号参数的取值是连续的。
* 数字信号，或离散信号。信号参数的取值是离散的。代表不同离散数值的基本波形称为码元。使用二进制时只有0、1两种码元。

信道（channel）表示向某个方向传送信息的媒体。交互有几种基本方式：

* 单向通信，或单工通信。
* 双向交替通信，或半双工通信。通信双方都可以发送消息，但不可同时发送。
* 双向同时通信，或全双工通信。

来自信源（source）的信号称为基带信号，此信号有较多低频和直流成分，为达到传输目的，需要对基带信号进行调制（modulation）。调制分为基带调制和带通调制。

物理层下面的传输媒体分为引导型和非引导型

* 引导型：双绞线、同轴电缆、光缆（多模、单模）
* 非引导型：微波通信（地面微波接力通信、卫星通信）、红外通信、激光通信等

信道复用技术分为：

* 频分复用（FDM，Frequency Division Multiplexing），每个用户在通信时占用某个固定的带宽（频带宽度）
* 时分复用（TDM，Time Division Multiplexing），用户在不同的时间占用同样的带宽。
* 统计时分复用（STDM，Statistic TDM），是一种改进的时分复用，可提高信道利用率。按需动态分配时隙。
* 波分复用（WDM，Wavelength DM），是光的频分复用。
* 码分复用（CDM，Code DM，也叫码分多址CDMA），各用户使用不同码型。

非对称数字用户线ASDL（Asymmetric Digital Subscriber Line），是使用数字技术对现有模拟电话线进行改造，使之能承载带宽数字业务。

---

参考文献：  
[1] 谢希仁. [计算机网络（第7版）](https://www.bicky.me/url.html#https://book.douban.com/subject/26960678/)[M]. 北京：电子工业出版社，2017.

