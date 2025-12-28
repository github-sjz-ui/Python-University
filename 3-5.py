# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 16:45:57 2025

@author: ASUS
"""

'''
编写程序，输入等比数列的首项、
公比（不等于1且小于36的正整数）和一个自然数n，输出这个数列前n项的和。
关键步骤要求使用内置函数int()
'''
a=int(input())
q=int(input())
n=int(input())
res=0
if q==1 or q>=36:
    print("error")
else:
    res=a*(1-q**n)/(1-q)
    print(res)