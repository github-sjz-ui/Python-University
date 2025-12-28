# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 13:55:04 2025

@author: ASUS
"""

'''
（1）	编写程序，输入任意大的自然数，输出各位数字之和。
'''
x=int(input())
res=0
while x>0:
    res+=x%10
    x//=10
print(res)