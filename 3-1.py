# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 15:06:54 2025

@author: ASUS
"""

'''
组合数求解
'''
def cni(n,i):
    minNI = min(i, n-i)
    result = 1
    res=1
    for j in range(0, minNI):
        result = result * (n-j) // (minNI-j)
        res = res * (n-j) // (j+1)
    return result,res
print(cni(5, 2))