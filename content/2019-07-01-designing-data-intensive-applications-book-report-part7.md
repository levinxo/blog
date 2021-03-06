Author: Levin
Date: 2019-07-01 19:32
disqus_identifier: 201907011932
Slug: designing-data-intensive-applications-book-report-part7
Title: 《数据密集型应用系统设计》读书笔记整理（7）-- 事务
Category: Web Arch
Tags: web arch, database, book report

> 有些人抱怨，常用的两阶段提交在性能和可用性方面代价太高。而我们认为事务滥用和过度使用所引入的性能瓶颈应该主要由应用层来解决，而不是简单的抛弃事务。  
> ——James Corbett 等，Spanner：来自Google的全球分布式数据库（OSDI，2012）

### 事务

事务将应用程序的多个读、写操作捆绑在一起成为一个逻辑操作单元，不需要担心部分失败的情况，之后可以安全地重试。

#### ACID的含义

事务所提供的安全保证即ACID，分别代表原子性（Atomicity），一致性（Consistency），隔离性（Isolation）与持久性（Durability）。

* 原子性：在出错时中支事务，并将部分完成的写入全部丢弃。要么全部成功，要么全部失败。
* 一致性：数据库以一致状态启动，而事务将其从某个一致状态转换为另一个一致状态，我们期望数据库始终处于某种一致状态。
* 隔离性：并发执行的多个事务相互隔离，他们不能互相干扰，一个事务不应看到另一个事务的中间结果。数据库要确保当事务提交时，其结果和串行执行完全相同。
* 持久性：保证一旦事务提交成功，即使存在硬件故障或数据库崩溃，事务所写入的数据也不会消失。

### 弱隔离级别

某个事务修改数据而另一个事务同时要读取该数据，或者两个事务同时修改相同数据时，才会引发并发问题（引入了竞争条件）。

可串行化隔离会严重影响性能，而许多数据库却不愿意牺牲性能，因而更多倾向于采用较弱的隔离级别，它可以防止某些但并非全部的并发问题。

#### 读-提交

读-提交提供两个保证：

* 读数据库时，只能看到已成功提交的数据（防止”脏读”）。
* 写数据库时，只会覆盖已成功提交的数据（防止”脏写”）。

还有一种更弱的隔离级别：读-未提交。它只防止脏写，而不防止脏读。

脏读：某个事务已完成部分数据写入，但事务尚未提交（或中止），此时另一个事务如果可以看到尚未提交的数据，就是脏读。脏读会导致一个事务观察到部分更新的数据，或看到一些稍后被回滚的数据，从而造成困惑。

脏写：先前的写入是尚未提交事务的一部分，如果还是被覆盖，就是脏写。事务要更新多个对象时，脏写会带来非预期的错误结果。

读-提交主要解决脏读和脏写问题。

##### 实现读-提交

数据库通常采用行级锁来防止脏写：事务要修改某个对象时，必须先获得该对象的锁，然后一直持有锁直到事务提交（或中止）。在此期间，如果有另个事务尝试更新同一个对象，则必须等待，直到前面的事务完成了提交后，才能获得锁并继续。

数据库通常采用维护旧值的方式来防止脏读：对于每个待更新的对象，数据库会维护其旧值和当前锁事务要设置的新值两个版本。在事务提交之前，所有其它读操作都读取旧值，仅当写事务提交之后，才会切换到读取新值。

#### 快照级别隔离与可重复读

在一个事务中，期间可能有其它事务并发执行，该事务在开始和结束期间前后读取数据有不一致的情况，就是读倾斜问题（或不可重复读取），这时需要快照级别隔离来进行保证。备份场景和OLAP分析场景不能忍受读倾斜问题。

快照级别隔离下，每个事务都从数据库的一致性快照中读取，事务一开始所看到的是最近提交的数据，即使数据随后可能被另一个事务更改，但保证每个事务都只看到该特定时间点的旧数据。

##### 实现快照级别隔离

快照级别隔离通常采用写锁来防止脏写，和读-提交隔离类似。但是，读取不需要加锁，读操作不会阻止写操作，反之亦然。这使得数据库可以在处理正常写入的同时，在一致性快照上执行长时间的只读查询，且两者之间没有任何锁的竞争。

考虑到多个正在进行的事务可能会在不同的时间点查看数据库状态，所以数据库保留了对象多个不同的提交版本，这种技术因此也被称为多版本并发控制（Multi-Version Concurrency Control，MVCC）。

当事务开始时，首先赋予一个唯一的、单调递增的事务ID（txid）。每当事务向数据库写入新内容时，所写的数据都会被标记写入者的事务ID，即每次修改总创建一个新版本。当事务读数据库时，通过事务ID可以决定哪些对象可见，哪些不可见。

此时数据库需要定义数据的可见性规则：

* 每个事务开始时，列出所有当时正在进行的其它事务，然后忽略这些事务完成的部分写入，即不可见。
* 所有中止事务所做的修改全部不可见
* 较晚事务ID（晚于当前事务）所做的修改不可见，不管这些事务是否提交
* 事务开始的时刻，创建该对象的事务已经完成了提交。
* 对象没有被标记为删除；或者即使标记了，但删除事务在当前事务开始时还没有完成提交。

快照级别隔离主要解决不可重复读问题。快照级别隔离对于只读事务特别有效。具体到实现，Oracle称之为可串行化，PostgreSQL和MySQL称为可重复读。

#### 防止更新丢失

上述两个隔离级别主要解决只读事务遇到并发写时可以看到什么。而并发写会带来另外一些冲突问题，比较有代表性的是更新丢失问题。

##### 原子写操作

避免在应用层代码完成"读-修改-写回”操作，如果数据库支持的话，是最好的解决方案。原子操作通常采用对读取对象加独占锁的方式来实现，这样在更新被提交之前不会有其他事务可以读它。另一种实现方式是强制所有的原子操作都在单线程上执行。

##### 显式加锁

由应用程序显式锁定待更新对象，此时如果有其他事务尝试同时读取对象，则必须等待当前正在执行的序列全部完成。

##### 自动检测更新丢失

原子操作和锁都是通过强制”读-修改-写回"操作序列串行执行来防止丢失更新。另一种思路是先让他们并发执行，但如果事务管理器检测到了更新丢失风险，则会中止当前事务，并强制回退到安全的”读-修改-写回”方式。如果开发者不小心忘记使用原子操作或锁，更新丢失检测会自动生效，有效避免这类错误。

该方法的优点是数据库可以借助快照级别隔离来高效地执行检查。PostgreSQL的可重复读，Oricle的可串行化以及SQL Server的快照级别隔离等，都可以自动检测何时发生了更新丢失，然后会中止违规的那个事务。但MySQL/InnoDB的可重复读却并不支持检测更新丢失。

##### 原子比较和设置

只有在上次读取的数据没有发生变化时才允许更新，如果内容已经有了变化且值与”旧内容”不匹配，则更新失败，需要应用层再次检查并在必要时重试。但要注意的是，如果运行在数据库某个旧的快照上，比较条件依然有可能为真，最终可能无法防止此类问题。所以在使用之前，要检查原子比较设置的安全运行条件。

#### 写倾斜与幻读

当两笔事务根据读取相同的一组记录进行条件判断通过后，更新了不同的记录对象，刚刚的写操作改变了决定的前提条件，结果可能违背了业务约束要求，此时的异常情况称为写倾斜。既不是脏写，也不是更新丢失。

在一个事务中的写入改变了另一个事务查询结果的现象，称为幻读。

如果不能使用可串行化级别隔离，一个次优的选择是视情况对事务依赖的行显式的加锁。但查询时预期结果为空时，该方法不生效。

如果问题的关键是查询时没有对象可以加锁，可以考虑人为引入一些可加锁的对象，这种方法称为实体化冲突（或物化冲突）。它把幻读问题转变为针对数据库中一组具体行的锁冲突问题。但一般不推荐这种方式，因为这种把一个并发控制机制降级为数据模型的思路总是不够优雅。

### 串行化

可串行化隔离保证即使事务可能会并行执行，但最终的结果与每次一个即串行执行结果相同。目前大多数提供可串行化的数据库使用了以下三种技术之一：

* 严格按照串行顺序执行
* 两阶段锁定
* 乐观并发控制技术，例如可串行化的快照隔离

#### 实际串行执行

解决并发问题最直接的方法是避免并发：在一个线程上按顺序方式每次只执行一个事务。

VoltDB/H-Store、Redis和Datomic等采用串行方式执行事务。单线程执行有时可能会比支持并发的系统效率更高，尤其是可以避免锁开销。但是，其吞吐量上限是单个CPU核的吞吐量。

对于交互式的事务处理，大量时间花费在应用程序与数据库之间的网络通信。如果不允许事务并发，那么吞吐量会非常低。因此，采用单线程串行执行的系统往往不支持交互式的多语句事务。应用提交整个事务代码作为存储过程打包发送到数据库，从而无需等待网络。例如VoltDB使用Java或Groovy，Datomic使用Java或Clojure，而Redis使用Lua。

存储过程与内存式数据存储使得单线程上执行所有事务变得可行。他们不需要等待I/O，避免加锁开销等复杂的并发控制机制，可以获得相当不错的吞吐量。

当满足以下约束条件时，串行执行事务可以实现串行化隔离：

* 事务必须简短高效，否则一个缓慢的事务会影响到其他事务的执行性能
* 仅限于活动数据集完全可以加载到内存的场景。有些很少访问的数据可能会被移到磁盘，万一单线程事务需要访问它，就会严重拖累性能，此时可以使用反高速缓存方案。
* 写入吞吐量必须足够低，才能在单个CPU核上处理，否则就需要采用分区，最好没有跨分区事务。
* 跨分区事务虽然也可以支持，但占比必须很小。

#### 两阶段加锁（two-phase locking，2PL）

多个事务可以同时读取同个对象，但只要出现任何写操作（包括修改和删除），则必须加锁以独占访问。

* 如果事务A已经读取了某个对象，此时事务B想要写入该对象，那么B必须等到A提交或中止才能继续。以确保B不会在事务A执行的过程中间去修改对象。
* 如果事务A已经修改了对象，此时事务B想要读取该对象，则B必须等到A提交或中止之后才能继续。对于2PL，不会出现读到旧值的情况。

快照级别隔离的口号”读写互不干扰”非常准确地点明了它和两阶段加锁的关键区别。同时因为2PL提供了串行化，所以它可以防止前面讨论的所有竞争条件，包括更新丢失和写倾斜。

##### 实现两阶段加锁

数据库的每个对象都有一个读写锁来隔离读写操作。锁可以处于共享模式或独占模式。类似linux系统自旋锁的读锁和写锁，可能会发生写饥饿。由于使用了较复杂的锁机制，所以很容易出现死锁现象。

另外将两阶段加锁与谓词锁或索引区间锁结合使用，可以防止所有形式的写倾斜以及其它竞争条件，隔离变得真正可串行化。

#### 可串行化的快照隔离（Serializable Snapshot Isolation，SSI）

可串行化的快照隔离是一种乐观并发控制。如果可能发生潜在冲突，事务会继续执行而不是中止，寄希望于相安无事；而当事务提交时，数据库会检查是否确实发生了冲突，如果是的话，中止事务并接下来重试。SSI基于快照隔离，事务的读取操作基于数据库的一致性快照，在此基础上增加了相关算法来检测写入之间的串行化冲突从而决定中止哪些事务。数据库必须检测事务是否会修改其它事务的查询结果，并在此情况下中止写事务。

数据库知晓查询结果发生变化，分两种情况：

* 读取是否作用于一个（即将）过期的MVCC对象（读取之前已经有未提交的写入）。
* 检查写入是否影响即将完成的读取（写入之前，是否有其它读取）。

与两阶段加锁相比，可串行化快照隔离的优点是事务不需要等待其它事务所持有的锁。这点和快照隔离一样，读写通常不会互相阻塞。但事务中止的比例会显著影响SSI的性能表现。

---

参考文献：  
[1] \(美\)Martin Kleppmann. [数据密集型应用系统设计（赵军平，吕云松，耿煜，李三平 译）](https://www.bicky.me/url.html#https://book.douban.com/subject/30329536/)[M]. 北京：中国电力出版社，2018.

