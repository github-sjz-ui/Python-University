# -*- coding: utf-8 -*-
"""
Created on Wed Dec 24 11:25:47 2025

@author: phy12
"""
'''
编写程序，输入掷飞镖次数，然后输出圆周率近似值。
'''
from random import random
cnt=int(input())
res=0
x=[random() for i in range(cnt)]
y=[random() for i in range(cnt)]
for i in range(cnt):
    if x[i]**2+y[i]**2<=1:
        res+=1
print(res/cnt*4)