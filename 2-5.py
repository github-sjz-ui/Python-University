# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 14:06:12 2025

@author: ASUS
"""

'''
（5）	编写程序，输入两个分别包含若干整数的列表lstA和lstB，
输出一个字典，要求使用列表lstA中的元素作为键，
列表lstB中的元素作为值，并且最终字典中的元素数量取决于lstA和lstB
中元素最少的列表的数量。
'''
lstA=eval(input())
lstB=eval(input())
lst_len_min=min(len(lstA),len(lstB))
res=dict()# or {}
#set() 集合
for i in range(lst_len_min):
    res[lstA[i]]=lstB[i]
print(res)