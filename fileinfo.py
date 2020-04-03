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
def text_word_list():        #获得文本单词列表
    x = textPad.get(1.0,END)
    for i in punctuation_list:
        x = x.replace(i,' ')
    x = x.lower().split()
    return x

def text_format():
    y = ''
    for i in text_word_list():
        y = y+i+' '
    top0 = Toplevel()
    top0.title('文本格式化')
    top0.geometry('800x500')
    textPad0 = ScrolledText(top0,width=600,height=300)
    textPad0.pack()
    textPad0.insert(1.0,y)

def word_number():        #获得单词总数
    showinfo(title='单词总数', message='单词总数为：'+str(len(text_word_list())))

def word_frequency():        #获得词频
    x = {}
    for i in set(text_word_list()):
        x[i] = text_word_list().count(i)
    y = ''
    for j in x:
        y = y + j+':'+str(x[j])+'\n'
    top1 = Toplevel()
    top1.title('词频统计')
    top1.geometry('600x300')
    textPad1 = ScrolledText(top1,width=600,height=300)
    textPad1.pack()
    textPad1.insert(1.0,y)

def list_order_test(x):        #列表冒泡检验
    for i in range(len(x)-1):
        if x[i+1] > x[i]:
            return 0
    return 1

    #词频可视化
def barshow():
    global word_list
    global number_list
    plt.bar(word_list,number_list)
    plt.title('高频单词top6')
    plt.xlabel('单词')
    plt.ylabel('频数')
    plt.show()
    #词频可视化
