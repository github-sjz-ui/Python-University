# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 17:01:37 2025

@author: ASUS
"""

'''
编写程序，输入一个字符串，
输出其中出现次数最多的字符及其出现的次数。要求使用字典。
'''
x=input()
dic=dict()
for s in x:
    dic[s]=dic.get(s,0)+1
print(dic)
max_s=max(dic,key=dic.get)
print(max_s)