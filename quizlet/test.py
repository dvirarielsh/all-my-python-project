import tkinter as tk
from tkinter import *
import random
import os
import sys
def resource_path(relative_path):
    """ מקבלת נתיב יחסי ומחזירה את הנתיב המתאים גם כאשר ארוזים ב-exe """
    try:
        # בעת הרצת קובץ exe
        base_path = sys._MEIPASS
    except Exception:
        # בעת הרצת סקריפט Python רגיל
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
root=textfielid= widget= widgetx=fontsize=hight=numbercorrect =stat=qusetion=numberworldmainlist =telltheanswer =restart=None 
correct = 0
listword = []
listwordcopy = []
listwordenglish = []
listwordhebrew =[]
path1 = resource_path("3acoreplusaenglist.txt")
path2 = resource_path("3acoreplusaheblist.txt")
path3 =resource_path("correct.txt")
path4 = resource_path("book_icon.ico")
d=0
def start():
    startroot()
    createlistofworld()
    setstat()
    starttextfiled()
    setquestion()
    createlistofqusetion()
    nextqusetion()
    settelltheanswer()
    setrestart()
def startroot():
    global  root
    if root is not None:
        root.destroy()
    root = Tk()
    root.title("Quizlet")
    root.geometry("700x500")
    root.iconbitmap(path4)
    root.configure(bg='lightblue')
    root.update()
def createlistofworld():
    global listword,d,listwordcopy
    with open(path1, 'r' , encoding='utf-8') as f:
        for line in f:
            listword.append([line.rstrip()])
    with open(path2, 'r' ) as f:
        for line in f:
            listword[d].append(line.rstrip())
            d = d + 1
    with open(path3, 'r', encoding='utf-8') as f:
        text = None
        for line in f:
            text = line.rstrip()
            for sublist in listword:
                if text is None:
                    continue
                elif text == sublist[0]:  # השוואה לערך הראשון בכל תת-רשימה
                    listword.remove(sublist)  # מחיקת תת-הרשימה כולה
    d = len(listword)
    if d == 0:
        with open(path1, 'r' , encoding='utf-8') as f:
            for line in f:
                listword.append([line.rstrip()])
        with open(path2, 'r' , encoding='utf-8') as f:
            for line in f:
                listword[d].append(line.rstrip())
                d = d + 1
        d = len(listword)
    listwordcopy = listword.copy()
    return listword
def starttextfiled():
    global textfielid,root,widget,widgetx,fontsize,hight
    a()
    textfielid = Entry(root,width=widget,font=("Arial", fontsize),justify='center')
    textfielid.place(x=widgetx,y=hight-fontsize ,width=widget)
    root.bind('<Configure>',c)
    textfielid.bind('<Return>',cheakanswer)
    root.update()
def setsizetextfield(event=None):
    global textfielid,root,widget,widgetx,fontsize,hight
    a()
    if textfielid is not None and root.winfo_exists() and len(listwordenglish) != 0:
        textfielid.configure(font=("Arial", fontsize))
        textfielid.place(x=widgetx,y=hight-fontsize ,width=widget)
    root.update()
def a():
    global root,widget,widgetx,fontsize,hight
    root.update()
    widget = int(root.winfo_width()/2) 
    widgetx = int(root.winfo_width()/4)  
    hight = int(root.winfo_height()/2)
    fontsize = 12* int(root.winfo_height() / 500)
def setstat():
    global stat, root, listword, correct, fontsize,widgetx,hight,widget,d
    asas = str(correct) + "/" + str(d)
    a()
    if stat is not None and root.winfo_exists():
        stat.destroy()
    stat = Label(root, text=asas, bg='lightblue', font=("Arial", 25*int(root.winfo_height() / 500)))
    stat.place(x=root.winfo_width()-widgetx,y=15*int(root.winfo_height() / 500))    
    root.update()
def fontsizex(event=None):
    global root,stat
    stat.configure(font=("Arial", 25*int(root.winfo_height() / 500)))
    stat.place(x=int(root.winfo_width()/2-50*int(root.winfo_width()/700)),y=15*int(root.winfo_height() / 500))
    root.update()
def c(event=None):
    if len(listwordenglish) != 0:
        if stat is not None:
            fontsizex()
        if textfielid is not None:
            setsizetextfield()
        if qusetion is not None:
            setfontquestion()
        if telltheanswer is not None:
            sizetelltheanswer()
        if restart is not None:
            setsizerestart()
def setquestion():
    global qusetion,root,listword,correctword
    a()
    if qusetion is not None:
        qusetion.destroy()
    qusetion = Label(root, bg='lightblue', font=("Arial", 25*int(root.winfo_height() / 500)))
    qusetion.place(x=widget,y=hight/4)
    root.update()
def setfontquestion():
    global qusetion,root
    qusetion.configure(font=("Arial", 25*int(root.winfo_height() / 500)))
    qusetion.place(x=int(root.winfo_width()/2)-50*int(root.winfo_width()/700),y=textfielid.winfo_y()-75*int(root.winfo_height() / 500))
    root.update()
def createlistofqusetion():
    global qusetion,root,listword,listwordhebrew,listwordenglish,numberworldmainlist
    numberworldmainlist = len(listword)
    for i in range(10):
        if len(listword) == 0:
            break
        randomnumber = random.randint(0,len(listword)-1)
        listwordenglish.append(listword[randomnumber][0])
        listwordhebrew.append(listword[randomnumber][1])
        listword.pop(randomnumber)
def Right():
    global qusetion,root,listword,listwordhebrew,listwordenglish,numberworldmainlist,numbercorrect,correct,telltheanswer
    correct = correct + 1
    setstat() 
    with open(path3, 'a') as file1:  # פתיחת הקובץ פעם אחת בלבד לכתיבה
        file1.write(listwordenglish[numbercorrect] + "\n")
    listwordhebrew.pop(numbercorrect)
    listwordenglish.pop(numbercorrect)
    telltheanswer.configure(text="Correct")
    if len(listword) != 0 and len(listwordhebrew) != 0 and len(listwordenglish) != 0:
        r = random.randint(0,len(listword)-1)
        listwordenglish.append(listword[r][0])
        listwordhebrew.append(listword[r][1])
        listword.pop(r)      
        root.update()
def cheakanswer(event=None):
    global textfielid,root,listwordhebrew,numbercorrect,listwordenglish
    t=listwordhebrew[numbercorrect]
    if textfielid.get() == listwordhebrew[numbercorrect][::-1]:
        Right()
    else:
        telltheanswer.configure(text="the correct answer is: " + listwordhebrew[numbercorrect][::-1])
    nextqusetion(t)
    if textfielid is not None and root.winfo_exists()and len(listwordenglish) != 0:
        textfielid.delete(0,END)
def nextqusetion(t=None):
    global qusetion,root,listwordhebrew,numbercorrect,listwordenglish,textfielid
    if len(listwordenglish) == 0:
        qusetion.configure(text="End")
        textfielid.destroy()
        telltheanswer.destroy()
        root.update()
    else:
        numbercorrect = random.randint(0,len(listwordenglish)-1)
        while t == listwordhebrew[numbercorrect]and len(listwordenglish) != 0 and len(listwordenglish) != 1 :
            numbercorrect = random.randint(0,len(listwordenglish)-1)
        qusetion.configure(text=listwordenglish[numbercorrect])
    root.update()
def settelltheanswer():
    global telltheanswer,root,widget,hight
    a()
    if telltheanswer is not None:
        telltheanswer.destroy()
    telltheanswer = Label(root, bg='lightblue', font=("Arial", 15*int(root.winfo_height() / 500)))
    telltheanswer.place(x=widget,y=hight/4)
    root.update()
def sizetelltheanswer():
    global telltheanswer,root,stat,hight,widget
    telltheanswer.configure(font=("Arial",12*int(root.winfo_height() / 500)))
    telltheanswer.place(x=stat.winfo_x()-80*int(root.winfo_width()/700),y=textfielid.winfo_y()+25*int(root.winfo_height() / 500))
    root.update()
def setrestart():
    global root,restart
    if restart is not None:
        restart.destroy()
    restart = Button(root, text="Restart", bg='lightblue', font=("Arial", 15*int(root.winfo_height() / 500)), command=startagain)
    restart.place(x=0,y=0)
    root.update()
def startagain():
    global correct,listword,listwordcopy,listwordenglish,listwordhebrew,d,root,numbercorrect,telltheanswer,stat,qusetion,textfielid,restart,widget,widgetx,fontsize,hight,numberworldmainlist
    root.destroy()
    root=textfielid= widget= widgetx=fontsize=hight=numbercorrect =stat=qusetion=numberworldmainlist =telltheanswer =restart=None 
    with open(path3, 'w') as file1:  # פתיחת הקובץ פעם אחת בלבד לכתיבה
        file1.write("")
    correct = 0
    listword = []
    listwordcopy = []
    listwordenglish = []
    listwordhebrew =[]
    d=0
    start()
def setsizerestart():
    global restart,root
    restart.configure(font=("Arial", 15*int(root.winfo_height() / 500)))
    restart.place(x=0,y=0)
    root.update()
start()
root.mainloop()