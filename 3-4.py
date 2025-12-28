# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 16:25:56 2025

@author: ASUS
"""

'''
使用filter()函数统计列表中所有非素数
'''
from sympy import isprime
from random import randint
a=[randint(0,100) for i in range(10)]
print(a)
b=list(filter(lambda x:not isprime(x) ,a))
print(b)