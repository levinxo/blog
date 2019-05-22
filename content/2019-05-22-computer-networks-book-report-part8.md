Author: Levin
Date: 2019-05-22 16:33
disqus_identifier: 201905221633
Slug: computer-networks-book-report-part8
Title: 《计算机网络》读书笔记整理（8）-- 互联网的音频/视频服务
Category: Network
Tags: network, book report

互联网提供的音频/视频服务可分为三种类型：

* 流式（streaming）存储音频/视频
* 流式实况音频/视频
* 交互式音频/视频

流媒体相关的一些协议：

* 实时流式协议RTSP（Real-TIme Streaming Protocol）是一个应用层的多媒体播放控制的信令协议，可以在UDP或TCP上传送。
* 实时运输协议RTP（Real-Time Transport Protocol）为实时应用提供端到端的运输，但不提供服务质量的保证，使用UDP传送。
* 实时运输控制协议RTCP（RTP Control Protocol）是与RTP配合使用的协议，主要功能：服务质量的监视与反馈、媒体间的同步以及多播组中成员的标志，也使用UDP传送。
* H.323是互联网的端系统之间进行实时声音和视频会议的信令标准，由多个协议组成，由ITU-T制定。
* 会话发起协议SIP（Session Initiation Protocol），是使用文本方式的信令协议，使用TCP传送。

---

参考文献：  
[1] 谢希仁. [计算机网络（第7版）](https://www.bicky.me/url.html#https://book.douban.com/subject/26960678/)[M]. 北京：电子工业出版社，2017.

