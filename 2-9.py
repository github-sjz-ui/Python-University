# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 14:59:32 2025

@author: ASUS
"""

'''
编写程序，输入包含若干集合的列表，输出这些集合的并集。
要求使用reduce()函数和lambda表达式完成。
'''
from functools import reduce
x=eval(input())
res=reduce(lambda x,y:x|y ,x)
print(res)