# -*- coding: utf-8 -*-
"""
Created on Wed Dec 24 14:55:11 2025

@author: ASUS
"""
'''
 编写程序，模拟决赛现场最终成绩计算过程。
 首先输入大于2的整数作为评委人数，然后依次输入每个评委的打分，
 要求每个分数都介于0和100之间。输入完所有评委打分之后，
 去掉一个最高分，去掉一个最低分，剩余分数的平均分即为该选手的最终得分。
'''
n=int(input())
score=list(map(int,input().split()))
if n<=2 or list(filter(lambda x:x>=100 ,score)):
    print("error")
else:
    score.sort()
    score=score[1:n]
    print(f"result score:{sum(score)/n:.2f}")
    