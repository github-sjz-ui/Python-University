# -*- coding: utf-8 -*-
"""
Created on Wed Dec 24 15:19:29 2025

@author: ASUS
"""

'''
假设一段楼梯共15个台阶，小朋友一步最多能上3个台阶。
编写程序计算小明上这段楼梯一共有多少种方法。
要求给出递推法和递归法两种代码。
'''
def floor1(x):
    if x==1 or x==0:
        return 1
    elif x==2:
        return 2
    else:
        return floor1(x-1)+floor1(x-2)+floor1(x-3)
print(floor1(15))

def floor2(f):
    if f==1:
        print(1)
    elif f==0:
        print(1)
    elif f==2:
        print(2)
    else:
        a,b,c=2,1,1
        while f>=3:
            a,b,c=a+b+c,a,b
            f-=1
        print(a)
floor2(15)
