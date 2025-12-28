# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 13:41:11 2025

@author: ASUS
"""

'''
一般来说，在一封正常邮件中，
是不会出现太多类似于【、】、*、-、/这样的字符的。
如果一封邮件中包含的类似字符数量超过一定的比例，
我们可以直接认为是垃圾邮件，编写程序，对给定的邮件内容进行分类，
提示“垃圾邮件”或“正常邮件”。
'''
s="【】*-/"
str1="fshdfsdfsndsfsf/////////【【】【【】【--**】【】"
cnt=0
for i in str1:
    if i in s:
        cnt+=1
print(f"{round(cnt/len(str1)*100,2):.2f}","%")