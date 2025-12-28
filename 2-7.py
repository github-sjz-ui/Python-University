# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 14:42:47 2025

@author: ASUS
"""

'''
（7）	编写程序，输入一个包含若干整数的列表，
输出列表中所有整数连乘的结果。
'''
from functools import reduce


lst=list(map(int,input().split(',')))
res=reduce(lambda x,y : x*y ,lst)
print(res)

