Author: levin
Date: 2014-04-15 22:10
disqus_identifier: 201404152210
Slug: find-files-in-specified-time
Title: 使用find指令查找特定/指定时间内的文件
Category: Unix/Linux
Tags: shell

需求查找某个时间点之后修改的文件，于是使用了下面的shell指令：<!-- more -->

    touch -t 201404151200.00 /tmp/cmp.time      #生成对比文件，时间为2014年4月15日12点整
    find . -type f -newer /tmp/cmp.time         #查找比cmp.time修改时间更新的文件

后来研究了下，find指令还带有-mtime指令，分三种参数情况：

**1.从现在算起向前n\*24小时之内修改过的文件：**

    find . -type f -mtime -n

图例(等号段为-mtime选项指定的时间区间，下同)：

                 {  n*24 h  }
    ----------n*24==========now----------

**2.从现在算起向前n\*24小时之前24小时之内修改过的文件：**

    find . -type f -mtime n

图例：

                                   {   n*24 h }
    ----------(n+1)*24==========n*24----------now----------

**3.从现在算起(n+1)\*24小时之前修改过的文件：**

    find . -type f -mtime +n

图例：

                     {(n+1)*24 h}
    ==========(n+1)*24----------now----------

**结合以上两种指令来查找某时间区间内的文件：**

    #先查找比cmp.time更新的文件，在此结果中查找24小时之前的文件
    find . -type f -newer cmp.time -exec find {} -mtime +0 \;

图例：

                                      {(n+1)*24 h}
    ----------(newer)==========(n+1)*24----------now----------
