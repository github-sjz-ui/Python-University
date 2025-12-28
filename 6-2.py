# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 13:07:37 2025

@author: ASUS
"""

'''
把密码安全强度分为强密码、中高、中低、弱密码。
其中强密码表示字符串中同时含有数字、小写字母、大写字母、标点符号这4类字符，
而弱密码表示字符串中仅包含4类字符中的一种。编写程序，输入一个字符串，
输出该字符串作为密码时的安全强度。
'''
password=input()
c1,c2,c3,c4=0,0,0,0
for s in password:
    if '0'<=s<='9':
        c1=1
    if 'a'<=s<='z':
        c2=1
    if 'A'<=s<='Z':
        c3=1
    if s in ".,:;'":
        c4=1
res=sum([c1,c2,c3,c4])
if res==1:
    print("弱密码")
if res==2:
    print("中低密码")
if res==3:
    print("中高密码")
if res==4:
    print("强密码")