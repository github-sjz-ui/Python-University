# -*- coding: utf-8 -*-
"""
Created on Wed Dec 24 15:08:09 2025

@author: ASUS
"""

'''
 编写程序模拟猜数游戏。
 程序运行时，系统生成一个随机数，然后提示用户进行猜测，
 并根据用户输入进行必要的提示（猜对了、太大了、太小了），
 如果猜对则提前结束程序，如果次数用完仍没有猜对，
 提示游戏结束并给出正确答案。
'''
from random import randint
x=randint(0, 100)
cnt=5#次数
while cnt>0:
    g=int(input())
    cnt-=1
    if g>x:
        print("bigger")
    elif g<x:
        print("smaller")
    else:
        print("equal")
        break
if cnt==0 and g!=x:
    print("次数用尽")