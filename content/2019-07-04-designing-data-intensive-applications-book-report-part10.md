Author: Levin
Date: 2019-07-04 15:52
disqus_identifier: 201907041552
Slug: designing-data-intensive-applications-book-report-part10
Title: 《数据密集型应用系统设计》读书笔记整理（10）-- 批处理系统
Category: Web Arch
Tags: web arch, database, book report

> 一个系统如果受到个人影响太大，这个系统就不可能成功。一旦最初的设计完成并且足够健壮，那么真正的测试就开始于许多持不同观点的人进行他们各自的实验。  
> ——Donald Knuth

### 概述

存储与处理数据的系统可以分为两大类：

* 记录系统，即真实记录系统，拥有数据的权威版本，每个记录只在系统中表示一次。
* 派生数据系统，此类系统的数据是从另一个系统中获取并以某种方式进行转换或处理的结果。

从技术上说，派生数据是冗余的，也就是说它是对现有信息的复制，但是，派生数据对于获得良好的读取查询性能通常很重要。

三种不同类型的系统：

* 在线服务（或称在线系统），响应时间通常是服务性能的主要衡量指标，而可用性同样非常重要。
* 批处理系统（或称离线系统），吞吐量通常是主要性能衡量标准。
* 流处理系统（或称近实时系统），介于在线与离线之间。

UNIX设计哲学：

* 统一接口
* 逻辑与布线分离，是一种松耦合，后期绑定或控制反转，更容易将小工具组合成更大的系统。
* 透明与测试，可以非常轻松地观察事情的进展。

### MapReduce与分布式文件系统

#### MapReduce作业执行

MapReduce是一个编程框架，可以使用它编写代码来处理HDFS等分布式文件系统中的大型数据集，Hadoop是一个MapReduce的开源实现。

MapReduce的数据处理模式：

0. 读取一组输入文件，并将其分解成记录
0. 调用mapper函数从每个输入记录中提取一个键值对。
0. 按照关键字将所有的键值对排序。
0. 调用reducer函数遍历排序后的键值对。

上述四个步骤可以由一个MapReduce作业执行。因此创建MapReduce作业，需要实现两个回调函数，即mapper和reducer。mapper的作用是将数据放入一个适合排序的表单中，而reducer的作用是处理排序好的数据。MapReduce与UNIX命令管道的主要区别在于它可以跨多台机器并行执行计算，而不必编写代码来指示如何并行化。

map任务的数量由输入文件块的数量决定，而reduce任务的数量则是由作业的作者来配置的。进行mapper时，框架使用关键字的哈希值来确定哪个reduce任务接收特定的键值对。

#### Reduce端的join

一般使用排序-合并join算法，mapper和排序过程确保将执行特定键join操作的所有必要数据都放在一起，这样只需要一次reducer调用。

使用MapReduce将计算中的物理网络通信部分从应用逻辑中分离出来，避免了应用程序代码处理网络的局部故障。

#### Map端join操作

广播哈希join特别适合大数据集与小数据集join。大数据集的每个文件对应一个mapper，每个mapper还负责将小数据集全部加载到内存中或将其保存在本地磁盘上的只读索引中（由于频繁访问，索引内容大部分驻留在OS的页面缓存中）。

分区哈希join，对map端join的输入进行分区，如此可以确定所有要join的记录都位于相同编号的分区中，因此每个mapper只需从每个输入数据集中读取一个分区就足够了。

#### 批处理工作流的输出

* 生成搜索索引
* 构建机器学习系统，如分类器和推荐系统，可将输出直接构建数据库文件并加载到处理只读查询的服务器中。

批处理输出的哲学：

* 将输入视为不可变，容错性良好，且由于没有副作用，自动重试也是安全的。
* 使不可逆性最小化的原则对于敏捷开发是有益的。
* 相同的输入可以用于不同的作业
* 程序逻辑和布线分离，更好地松耦合、隔离问题。

#### 对比hadoop和分布式数据库

hadoop开放了将数据不加区分地转存到HDFS的可能性。不加区分地数据转储转移了数据解释的负担，不是强迫数据集的生产者将其转化为标准化格式，而是将解释数据变为消费者的问题。以原始形式简单地转储数据可以进行多次这样的转换。这种方法被称为寿司原则。

MapReduce被设计为容忍意外任务终止的原因：不是因为硬件特别不可靠，而是因为任意终止进程的灵活性能够更好地利用集群资源。

### 超越MapReduce

与UNIX管道相比，MapReduce完全实体化中间状态的方法有一些不利之处：

* MapReduce作业只有在前面作业中的所有任务都完成时才能启动，必须等待前面作业中所有任务的完成必然会减慢整个工作流的执行。
* 进行多个作业时，mapper通常是冗余的。
* 中间状态存储在分布式文件系统中意味着这些文件被复制到多个节点，对于临时数据来说有点大材小用了。

为了解决MapReduce的这些问题，开发了新的分布式批处理执行引擎，有Spark、Tez、Flink。他们把整个工作流作为一个作业来处理，而不是把它分解成独立的子作业，他们的每个工作阶段称为函数运算符，类似MapReduce的一个个作业。与MapReduce相比优点：

* 排序只在需要的地方进行，而不是在map和reduce之间默认发生。
* 没有不必要的map任务。
* 工作流中数据依赖性是明确声明的，因此调度器可以对任务进行本地优化。
* 将运算符之间的中间状态保存在内存中或写入本地磁盘通常就足够了，比写入HDFS需要更少的I/O。
* 运算符在输入准备就绪后就可以开始执行，不需要等待前一个阶段全部完成。
* 现有的Java虚拟机进程可以被重用来运行新的运算符，从而减少启动开销（MapReduce为每个任务启动一个新的JVM）。

由于通过若干个处理阶段明确地建模数据流，所以这些系统被称为数据流引擎。

---

参考文献：  
[1] \(美\)Martin Kleppmann. [数据密集型应用系统设计（赵军平，吕云松，耿煜，李三平 译）](https://www.bicky.me/url.html#https://book.douban.com/subject/30329536/)[M]. 北京：中国电力出版社，2018.