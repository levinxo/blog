Author: levin
Date: 2013-03-12 15:33
disqus_identifier: 201303121533
Slug: assembly-long-overflow
Title: 汇编.long申明数组元素溢出的问题
Category: Program language

<!-- more -->

    .section .data
    data_items:
    .long 5,6,44,56,41,37,124,7,87,43,243,67,2,0
    
    .section .text
    
    .globl _start
    _start:
    
    movl $0, %edi
    movl data_items(, %edi, 4), %eax
    movl %eax, %ebx
    
    start_loop:
    incl %edi
    movl data_items(, %edi, 4), %eax
    cmpl $0, $eax
    je end_loop
    
    cmpl %ebx, %eax
    jle start_loop
    
    movl %eax, %ebx
    jmp start_loop
    
    end_loop:
    movl $1, %eax
    int $0x80
    
    #end


此汇编程序在一组数字中找最大的数并将最大的数存入%ebx寄存器中给系统函数\_exit()调用。
在32位centos下汇编、链接、运行：

    as compare.s -o compare.o && ld compare.o -o compare && ./compare
    echo $?

输出结果为243，没错。然后将243改为一个比255大的数以后，比如256，再重新汇编链接运行，发现输出结果为0，此结果溢出了。

    movl data_items(, %edi, 4), %eax

上面的4表示元素占4个字节，那么每个元素应该是4\*8=32位，.long申明的数组元素占的是32位没错，所以很有可能是系统返回函数获取%ebx的数据时溢出了。

写个c文件返回大于255的数试试：

    int main(void){
    	return 256;
    }

编译运行：

    gcc test.c && ./a.out
    echo $?

输出为0，所以此猜想正确，linux内核系统的返回函数获取%ebx寄存器中的值时溢出了。
