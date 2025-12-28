# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 14:28:32 2025

@author: ASUS
"""

'''
2， 编写程序，实现磁盘垃圾文件清理功能。
要求指定要清理的文件夹，
然后删除该文件夹及其子文件夹中所有扩展名为
tmp、log、obj、txt以及大小为0的文件。
函数参数为文件夹名称及路径。
'''
from os.path import isdir, join, splitext, getsize
from os import remove, listdir


filetypes=[".tmp",".log",".obj",".txt"]
def delfiles(pwd):
    if not isdir(pwd):
        return 
    for filename in listdir(pwd):
        temp=join(pwd,filename)
        if isdir(temp):
            delfiles(temp)
        if splitext(temp)[1] in filetypes or getsize(temp)==0:
            remove(temp)
pwd=r"D:\testDirectory"
delfiles(pwd)
