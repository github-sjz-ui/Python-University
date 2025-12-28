# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 13:26:45 2025

@author: ASUS
"""

'''
写程序，模拟打字练习程序的成绩评定。
假设origin为原始内容，userInput为用户练习时输入的内容，
要求用户输入的内容长度不能大于原始内容的长度。
如果对应位置的字符一致则认为正确，否则判定输入错误。
最后成绩为：正确的字符数量/原始字符串长度，按百分制输出，
要求保留2位小数。
'''
origin="Hello World"
userInput=input()
if len(userInput)>len(origin):
    print("请重新输入")
else:
    cnt=0
    for i in range(len(userInput)):
        if origin[i]==userInput[i]:
            cnt+=1
print(f"{round(cnt/len(origin)*100,2):.2f}","%")
    
    