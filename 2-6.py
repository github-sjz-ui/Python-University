# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 14:21:16 2025

@author: ASUS
"""

'''
（6）	编写程序，输入一个包含若干整数的列表，
输出新列表，要求新列表中的所有元素来自于输入的列表，
并且降序排列。
'''
x=list(map(int,input().split(',')))
x.sort(reverse=True)
print(x)