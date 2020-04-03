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

def high_frequency_word():        #获得高频单词(还未考虑第7及以后！)
    global word_list
    global number_list
    x = {}
    dict1 = {}
    word_list = []
    number_list = []
    for k in set(text_word_list()):
        x[k] = text_word_list().count(k)
    for i in x:
        if i not in stop_word_list:
            dict1[i] = x[i]
    for j in dict1:
        word_list.append(j)
        number_list.append(dict1[j])
    while list_order_test(number_list) == 0:
        for m in range(len(word_list)-1):
            if number_list[m] < number_list[m+1]:
                word_list[m],word_list[m+1] = word_list[m+1],word_list[m]
                number_list[m],number_list[m+1] = number_list[m+1],number_list[m]
    word_list = word_list[:6]
    number_list = number_list[:6]
    z = ''
    for k in range(6):
        z = z+word_list[k]+':'+str(number_list[k])+'\n'
    
    top2 = Toplevel()
    top2.title('高频单词top6')
    top2.geometry('300x180+200+200')
    textPad2 = ScrolledText(top2,width=40,height=10)
    textPad2.pack()
    textPad2.insert(1.0,z)
    button = Button(top2,text='显示统计柱状图',bg='Linen',width=42,height=2,command=barshow)
    button.pack()
#文本状态查看
    
#文件菜单
def newfile():
    global filename
    window.title('未命名文件')
    filename = ''
    textPad.delete(1.0,END)

def openfile():
    global filename
    filename = askopenfilename(defaultextension = '.txt')
    if filename == '':
        pass
    else:
        textPad.delete(1.0,END)
        with open(filename,'r') as f:
            textPad.insert(1.0,f.read())

def savefile():
    global filename
    if filename != '': 
        with open(filename,'w') as file:
            file.write(textPad.get(1.0,END))
    else:
        savethefileas()

def savethefileas():
    global filename
    filename = asksaveasfilename(initialfile= '未命名.txt', defaultextension='.txt')
    if filename != '':
        savefile()
#文件菜单

#关于菜单
def author():
    showinfo(title='关于', message='作者：Jeffery')
def version():
    showinfo(title='关于', message='当前版本为1.0')
#关于菜单

#编辑
def clearall():        #清除
    textPad.delete(1.0,END)
def selectall():        #全选
    textPad.tag_add('sel',1.0,END)
def key_callback(event):
    textPad.edit_separator()
    textPad.bind(sequence='<Key>',func=key_callback)
def undo():        #撤销
    textPad.edit_undo()
def redo():        #恢复
    textPad.edit_redo()
#编辑
    
#GUI
    #主窗口
window = Tk()
window.title('Text Editor')
window.geometry('800x500+100+100')
    #主窗口

    #菜单
menubar = Menu(window)
window['menu'] = menubar

filemenu = Menu(menubar,tearoff=False)
menubar.add_cascade(label='文件',menu=filemenu)
filemenu.add_command(label='新建',command=newfile)
filemenu.add_command(label='打开',command=openfile)
filemenu.add_command(label='保存',command=savefile)
filemenu.add_command(label='另存为',command=savethefileas)

editmenu = Menu(menubar,tearoff=False)
menubar.add_cascade(label='编辑',menu=editmenu)
editmenu.add_command(label='清除',command=clearall)
editmenu.add_command(label='全选',command=selectall)
editmenu.add_command(label='撤销',command=undo)
editmenu.add_command(label='恢复',command=redo)

statusmenu = Menu(menubar,tearoff=False)
menubar.add_cascade(label='文本状态查看',menu=statusmenu)
statusmenu.add_command(label='文本格式化结果',command=text_format)
statusmenu.add_command(label='单词总数',command=word_number)
statusmenu.add_command(label='词频',command=word_frequency)
statusmenu.add_command(label='高频单词',command=high_frequency_word)

aboutmenu = Menu(menubar,tearoff=False)
menubar.add_cascade(label='关于',menu=aboutmenu)
aboutmenu.add_command(label='作者',command=author)
aboutmenu.add_command(label='版本',command=version)
    #菜单

    #工具栏
toolbar = Frame(window,bg='LightSkyBlue')
Label(toolbar,text='便捷工具栏：',fg='LightCoral',bg='LightSkyBlue').grid(row=0,column=0)
b1 = Button(toolbar,text='新建',command=newfile,bg='Linen')
b2 = Button(toolbar,text='打开',command=openfile,bg='Linen')
b3 = Button(toolbar,text='保存',command=savefile,bg='Linen')
b4 = Button(toolbar,text='清除',command=clearall,bg='Linen')
b5 = Button(toolbar,text='全选',command=selectall,bg='Linen')
b6 = Button(toolbar,text='撤销',command=undo,bg='Linen')
b7 = Button(toolbar,text='恢复',command=redo,bg='Linen')
b = [b1,b2,b3,b4,b5,b6,b7]
for i in range(7):
    b[i].grid(row=0,column=i+1,padx=0,pady=2)
toolbar.pack(fill=X)
    #工具栏

    #操作框
textPad = ScrolledText(window,width=220,height=60,undo=True)
textPad.edit_separator()
textPad.pack()
    #操作框

window.mainloop()
#GUI