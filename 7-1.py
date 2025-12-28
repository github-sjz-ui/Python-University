# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 13:53:40 2025

@author: ASUS
"""

'''
编写一个程序demo.py，要求运行该程序后，生成demo_new.py文件，
其中内容与demo.py一样，只是在每一行的后面加上行号。要求行号以#开始，
并且所有行的#符号垂直对齐。
'''
filename="demo.py"
with open(filename,"r") as fp:
    lines=fp.readlines()
maxline=len(max(lines,key=len))
with open(filename[:-3]+"_new.py","w") as fp:
    lines=[line.rstrip().ljust(maxline)+"#"+str(i+1)+"\n" \
           for i,line in enumerate(lines)]
    fp.writelines(lines)