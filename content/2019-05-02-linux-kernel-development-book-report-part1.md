Author: Levin
Date: 2019-05-02 23:16
disqus_identifier: 201905022316
Slug: linux-kernel-development-book-report-part1
Title: 《Linux内核设计与实现》读书笔记整理（1）
Category: Unix/Linux
Tags: linux

#### 写在前面
花了大概一周时间读完。这本书页数不多，麻雀虽小，五脏俱全。作者在很小的篇幅里，将linux的核心都描述了一遍。收益颇多，整理读书笔记如下，有时间还会二刷。书是2010年的版本，基于2.6版本内核。

#### 进程：
* 进程是处于执行期的程序以及相关资源的总称，进程描述符存放在叫做任务队列的双向链表中。
* 进程描述符使用task\_struct数据结构，通过对象高速缓存slab分配器动态分配和复用。
* linux使用fork()+exec()来创建进程，先fork()创建进程描述符，再exec()加载代码至内存中，使用写时复制（copy-on-write）策略。
* 内核的线程本质为进程，和进程不同之处主要在于和进程共享地址空间。

#### 进程调度：
* 进程调度程序是在可运行态进程之间分配有限的处理器时间资源的内核子系统
* linux是抢占式多任务系统，即由调度程序来决定什么时候停止一个进程的运行。
* linux使用RSDL（反转楼梯最后期限调度，Rotating Staircase Deadline scheduler）算法实现的完全公平调度算法（CFS）来实现调度
* 影响进程调度的两个属性：进程的nice值和实时优先级
* 进程可得到运行的时间由其他可运行进程的nice值的相对差值决定
* 若新的可运行进程在之前实际消耗的处理器时间比处理器分配的时间片更少，则新进程立刻投入运行，抢占当前进程，在抢占前，需要检查当前被抢占的进程没有持有锁。
* CFS使用红黑树来组织可运行进程队列，当需要选下一个进程运行时，选取具有最小总运行时间的进程

#### 系统调用：
* 用户程序使用应用编程接口（API），API进行系统调用。
* 使用系统调用发生的事情：陷入内核，传递系统调用号和参数，执行正确的系统调用函数，并把返回值带回用户空间。

#### 内核数据结构：
* 内核的链表结构不是将数据结构塞入链表，而是将链表结点塞入数据结构。好处是创建、操作链表的方法都不需要知道链表所嵌入对象的数据结构。
* 还提到了其它几种数据结构：队列、映射、二叉树

#### 中断和中断处理：
* 异步中断流程：键盘->中断控制器->处理器->OS->中断处理程序
* linux将中断处理分为两个部分，中断处理程序是上半部（top half），只做有严格时限的工作，允许稍后完成的工作会推迟到下半部（bottom half）。这种设计可使系统处于中断屏蔽状态的时间尽可能的短，以此提高系统响应能力。
* 内核提供了三种下半部实现机制：软中断、tasklets和工作队列。
* 软中断：中断处理程序执行硬件设备的相关操作，然后触发相应的软中断，最后退出。接着软中断开始执行剩余的任务。
* tasklets：是利用软中断实现的一种下半部机制，所以它们本身也是软中断。大多数情况下应该使用tasklets。
* 工作队列：工作队列可以把工作退后交给一个内核线程去执行，所以此下半部会在进程上下文中执行，最重要的一点就是工作队列允许重新调度或睡眠。此方式造成的开销较大。

#### 内核同步：
* 临界区是访问和操作共享数据的代码段。两个线程处于同一个临界区中同时执行，就称为竞争条件。防止竞争条件称为同步。加锁粒度用来描述加锁保护的数据规模。
* 内核提供两种原子操作接口：一是针对整数进行操作，二是针对单独的位进行操作。原子操作通常是内联函数，往往通过内嵌汇编指令来实现。
* 锁：
    * 自旋锁（spin lock）：在短期内进行轻量级加锁，可防止多于一个执行线程进入临界区，当锁发生争用期间，请求锁的线程在等待时自旋。持有自旋锁的进程，内核不会进行抢占。
    * 读-写自旋锁：一个或多个读可以并发地持有读者锁；写锁只能被一个执行线程持有，而且此时不能有并发的读操作。这种机制更照顾读操作，大量读容易引发写饥饿。
    * 信号量（semaphore）：是一种睡眠锁。当一个执行线程试图获得一个被占用的信号量时，会被推进一个等待队列睡眠，当信号量可用后，该执行线程将被唤醒获得该信号量。信号量可允许同时被多个执行线程所持有，此值称为使用者数量（usage count）。当使用者数量为1时，就称为互斥信号量，大于1时称为计数信号量。
    * 互斥体（mutex）：可实现互斥的睡眠锁，也是一种信号锁。类似于信号量，mutex更简洁和高效，且它的使用者数量永远为1。
    * 顺序锁（seq lock）：依靠序列计数器实现的锁，用于读写共享数据，主要面向读者比写者多很多的场景。写入时，会得到一个锁，并增加序列值。读数据前后，各读取一次序列号，若两次序列号一致，说明读取过程中没有被写入过。

#### 定时器和时间管理：
系统定时器是一种可编程硬件芯片，以固定频率产生中断，即定时器中断。它对应的中断处理程序负责更新系统时间和执行周期性的任务。