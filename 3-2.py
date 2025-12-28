# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 15:39:37 2025

@author: ASUS
"""

'''
编写程序，输入一个大于2的自然数，
然后输出小于该数字的所有素数组成的列表。
(使用列表实现筛选法求素数)
'''
from math import sqrt
from sympy import isprime
def is_prime(a):
    if a<=1:
        return False
    else:
        for i in range(2,int(sqrt(a))+1):
            if a%i==0:
                return False
        return True

n=int(input())
res=[]
for i in range(2,n+1):
    if is_prime(i):
        res.append(i)
print(res)
