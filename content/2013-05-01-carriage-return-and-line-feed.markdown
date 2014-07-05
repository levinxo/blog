Author: levin
Date: 2013-05-01 11:33
Slug: carriage-return-and-line-feed
Title: "carriage return"和"line feed"的区别
Category: Uncategorized

carriage return 中文叫回车(真难听)，就是光标回到一行的开头位置。用\r表示。

line feed 中文叫换行，指光标往下移一行。用\n表示。<!-- more -->
两个合起来就是\r\n，即我们平常说的回车符，光标往下一行并回到行首。

1. 在win下使用\r\n，16进制为0D0A
2. unix和linux下使用\n，16进制为0A
3. mac下使用\r，16进制为0D
