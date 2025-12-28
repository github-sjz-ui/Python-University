# -*- coding: utf-8 -*-
"""
Created on Wed Dec 24 16:51:40 2025

@author: ASUS
"""

'''
假设你正参加一个有奖游戏节目，前方有3道门可以选择，
其中一个后面是汽车，另外两个后面是山羊。你选择一个门，
比如说1号门，主持人当然知道每个门后面是什么并且打开了另一个门，
比如说3号门，后面是一只山羊。这时，主持人会问你"你想改选2号门吗？"，
然后根据你的选择确定最终要打开的门，并确定你获得山羊（输）或者汽车（赢）。
编写程序，模拟上面的游戏，比如模拟20局，统计次数。
'''
from random import randint
from random import choice
def memo1():
    door=[0]*3
    door[randint(0, 2)]=1
    you_choice=randint(0,2)
    cnt=0
    op=choice([i for i in range(3) if i!=you_choice and door[i]!=1])
    #改选
    res1=[i for i in range(3) if i!=you_choice and i!=op][0]
    if door[res1]==1:
        cnt+=1
    return cnt
def memo2():
    door=[0]*3
    door[randint(0, 2)]=1
    you_choice=randint(0,2)
    cnt=0
    #op=choice([i for i in door if i!=you_choice and door[i]!=1])
    #不改选
    res2=you_choice
    if door[res2]==1:
        cnt+=1
    return cnt

cnt1,cnt2=0,0
test=100000
for _ in range(test):
    cnt1+=memo1()
    cnt2+=memo2()
print(cnt1/test,cnt2/test)















