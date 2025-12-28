# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 14:56:09 2025

@author: ASUS
"""

'''
编写程序，输入两个各包含2个整数的列表，
分别表示城市中两个地点的坐标，输出两点之间的曼哈顿距离。
'''
x1,y1=list(map(int,input().split()))
x2,y2=list(map(int,input().split()))
print(abs(x1-x2)+abs(y1-y1))