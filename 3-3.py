# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 15:48:08 2025

@author: ASUS
"""

'''
输入一个大于2的自然数，输出小于该数字的所有素数组成的集合。
（使用集合实现筛选法求素数）
'''
#差集
a=int(input())+1
res=set(range(2,a))
for i in range(2,int(a**0.5)+1):
    res-=set(range(i*i,a,i))
print(res)    