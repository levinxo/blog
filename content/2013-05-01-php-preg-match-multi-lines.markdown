Author: levin
Date: 2013-05-01 11:35
disqus_identifier: 201305011135
Slug: php-preg-match-multi-lines
Title: php正则匹配多行
Category: Program language
Tags: PHP

一般用php正则匹配时，没有特殊指明，都是匹配一行而已，碰到换行符就自动忽略了。

要想匹配多行，在表达式后加个修饰符s即可<!-- more -->

例如：

    <?php
    $str = "first line\nsecend line\nthird line\nlast line";
    
    preg_match('/first\sline(.*)last\sline/s', $str, $match);
    
    echo $match[1];
    
    /**输出
    secend line
    third line
    匹配成功
    **/
    
    //end
