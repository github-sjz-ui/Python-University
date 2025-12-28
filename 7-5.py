# -*- coding: utf-8 -*-
"""
Created on Sun Dec 28 16:34:55 2025

@author: ASUS
"""

'''
编写程序，读取Word文件中的所有段落文本，
然后输出其中所有红色的文本和加粗的文本以及同时具有这两种属性的文本。
'''
from docx import Document
from docx.shared import RGBColor

boldText = []
redText = []
doc = Document('test.docx')
for p in doc.paragraphs:
    for r in p.runs:
        # 加粗字体
        if r.bold:
            boldText.append(r.text)
        # 红色字体
        if r.font.color.rgb == RGBColor(255,0,0):
            redText.append(r.text)

result = {'red text': redText,
          'bold text': boldText,
          'both': set(redText) & set(boldText)}
#  输出结果
for title in result.keys():
    print(title.center(30, '='))
    for text in result[title]:
        print(text)
