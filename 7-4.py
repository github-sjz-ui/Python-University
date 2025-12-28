# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 16:15:56 2025

@author: ASUS
"""

'''
安装Python扩展库python-docx，然后读取一个Word文章中所有段落的文本，
查找并输出其中所有AABB形式的词语，例如踏踏实实、密密麻麻、简简单单、时时刻刻。
'''
import re
from docx import Document
doc=Document("text.docx")
for para in doc.paragraphs:
    text=para.text
    pattern = r'(([\u4e00-\u9fa5])\2([\u4e00-\u9fa5])\3)'
    r = re.findall(pattern, text)
    if r:
        for word in r:
            print(word[0])