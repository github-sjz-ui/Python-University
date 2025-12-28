# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 14:02:28 2025

@author: ASUS
"""

'''
（4）	编写程序，输入一个包含若干整数的列表，
输出一个新列表，要求新列表中只包含原列表中的偶数。
'''
from random import randint
x=[ randint(0,10) for i in range(10) ]
res=[]
for i in range(len(x)):
    if x[i] % 2==0:
        res.append(x[i])
print(res)