# -*- coding: utf-8 -*-
"""
Created on Wed Dec 24 16:17:06 2025

@author: ASUS
"""

'''
编写程序，模拟抓土拨鼠小游戏。
假设一共有一排5个洞口，土拨鼠最开始的时候在其中一个洞口，
然后玩家随机打开一个洞口，如果里面有土拨鼠就抓到了。
如果洞口里没有土拨鼠就第二天再来抓，
但是第二天土拨鼠会在玩家来抓之前跳到隔壁洞口里。
如果在规定的次数内抓到了土拨鼠就提前结束游戏并提示成功；
如果规定的次数用完还没有抓到土拨鼠，就结束游戏并提示失败。
'''
from random import randint
hole=[0]*5
a=[-1,1]
choice=randint(0,4)
hole[choice]=1
cnt=5
while cnt>0:
    x=int(input())
    if x==choice:
        print("find it!")
        break
    elif choice==0:
        chioce=1
    elif choice==4:
        choice=3
    else:
        choice+=a[randint(0,1)]
    cnt-=1
if x!=choice:
    print("次数用尽")