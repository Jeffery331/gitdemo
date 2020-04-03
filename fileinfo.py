# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 12:50:21 2019

@author: Jeffery
"""


import matplotlib.pyplot as plt
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import *
from tkinter.filedialog import *
plt.rcParams['font.sans-serif'] = ['SimHei']

#文本状态查看
with open('停用词表.txt','r') as g:        #导入停用词表
    stop_word_list = g.read()
stop_word_list = stop_word_list.split()        #获得停用词表列表

punctuation_list = [',','.','!','?','\'',';',':','\"', '“','‘','’','”']        #未用正则