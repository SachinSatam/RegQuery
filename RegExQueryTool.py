import tkinter as tk
from tkinter import *
from tkinter import filedialog
import re
import urllib.request
root=tk.Tk()
root.geometry('500x450')
root.title("RegEx Query tool")

def clear():
    txtbox.delete(1.0,END)
    textbox.delete(1.0,END)
    search_label1.destroy()
    

    
def gettxt():
    my_label.config(text=txtbox.get(1.0,END))

def open_text():
    text_file=filedialog.askopenfilename(initialdir="C:",title="Open Text File",filetypes=(("Text Files","*.txt"),))
    text_file=open(text_file,'r',encoding="utf-8")
    txt=text_file.read()
    txtbox.insert(END,txt)
    text_file.close()
    
def save_text():
    text_file=filedialog.askopenfilename(initialdir="C:",title="Open Text File",filetypes=(("Text Files","*.txt"),))
    text_file=open(text_file,'w',encoding="utf-8")
    text_file.write(txtbox.get(1.0,END))


def searchbtn():
    global selection
    global top1
    top1=Toplevel()
    top1.geometry("400x400")
    label1=Label(top1,text="Search By:")
    label1.grid(row=0,column=1)
    clicked=StringVar()
    #drop=OptionMenu(top1,clicked,"Pattern","Starting letter","Starting and Ending")
    #drop.grid(row=0,column=2)
    btn1=Button(top1,text="Pattern",command=search)
    btn1.grid(row=1,column=2)
    lblx=Label(top1,text="")
    lblx.grid(row=1,column=3)
    btn2=Button(top1,text="Starting letter",command=searchByStart)
    btn2.grid(row=1,column=4)
    lbly=Label(top1,text="")
    lbly.grid(row=1,column=5)
    btn3=Button(top1,text=" Starting and Ending letter",command=searchByStartandEnd)
    btn3.grid(row=1,column=6)
   
    
def search():
    global textbox
    lbl1=Label(top1,text="Enter the Pattern:")
    lbl1.grid(row=2,column=1)
    textbox=Text(top1,width=10,height=1,font=("Helvetica",10))
    textbox.grid(row=2,column=2)
    btn1=Button(top1,text="Search",command=search1)
    btn1.grid(row=2,column=3)
    btn2=Button(top1,text="clear",command=clear)
    btn2.grid(row=5,column=2)
def search1():    
    Str1=txtbox.get(1.0,END)
    Str2=textbox.get(1.0,END)
    global search_label1
    search_label1=Label(top1,text=" ")
    search_label1.grid(row=3,column=2)
    global search_label2
    search_label2=Label(top1,text=" ")
    search_label2.grid(row=4,column=2)
    count=len(re.findall(Str2,Str1))
    search_label2.config(text="Number of Matches Found:{cnt}".format(cnt=count))
    if re.search(Str2,Str1,re.IGNORECASE):
        search_label1.config(text="Matches Found") 
    else:
        search_label1.config(text="No Match Found")

      
def searchByStart():
    global textbox1
    global textbox2
    lbl1=Label(top1,text="Enter the Starting two letters:")
    lbl1.grid(row=2,column=1)
    textbox1=Text(top1,width=3,height=1,font=("Helvetica",10))
    textbox1.grid(row=2,column=2)
    textbox2=Text(top1,width=3,height=1,font=("Helvetica",10))
    textbox2.grid(row=2,column=3)
    btn1=Button(top1,text="Search",command=searchByStart1)
    btn1.grid(row=2,column=4)

def searchByStart1():
    text=txtbox.get(1.0,END)
    var1=textbox1.get(1.0)
    var2=textbox2.get(1.0)
    match=re.findall(r'\b{va1}{va2}\w+\b'.format(va1=var1,va2=var2),text)
    file=open('demo1.txt','w')
    file.write('\n'.join(match))
    file.close()
    btn2=Button(top1,text="Show Matches",command=searchByStart2)
    btn2.grid(row=4,column=5)

def searchByStart2():
    file1=open('demo1.txt','r')
    txt=file1.read()
    lbl2=Label(top1,text="")
    lbl2.grid(row=4,column=4)
    lbl2.config(text="Following matches were found:")
    txtbox1=Text(top1,width=10,height=10,font=("Helvetica",16))
    txtbox1.grid(row=6,column=4)
    txtbox1.insert(END,txt)
    file1.close()
    
def searchByStartandEnd():
    global textbox3
    global textbox4
    lbl1=Label(top1,text="Enter the Starting and Ending letter:")
    lbl1.grid(row=2,column=5)
    textbox3=Text(top1,width=3,height=1,font=("Helvetica",10))
    textbox3.grid(row=2,column=6)
    textbox4=Text(top1,width=3,height=1,font=("Helvetica",10))
    textbox4.grid(row=2,column=7)
    btn1=Button(top1,text="Search",command=searchByStartandEnd1)
    btn1.grid(row=2,column=4)
    
def searchByStartandEnd1():
    text=txtbox.get(1.0,END)
    var1=textbox3.get(1.0)
    var2=textbox4.get(1.0)
    match=re.findall(r'\b[{va1}]\w+[{va2}]\b'.format(va1=var1,va2=var2),text,re.IGNORECASE)
    file=open('demo1.txt','w')
    file.write('\n'.join(match))
    file.close()
    btn2=Button(top1,text="Show Matches",command=searchByStartandEnd2)
    btn2.grid(row=4,column=5)

def searchByStartandEnd2():
    file1=open('demo1.txt','r')
    txt=file1.read()
    lbl2=Label(top1,text="")
    lbl2.grid(row=4,column=4)
    lbl2.config(text="Following matches were found:")
    txtbox1=Text(top1,width=10,height=10,font=("Helvetica",16))
    txtbox1.grid(row=6,column=4)
    txtbox1.insert(END,txt)
    file1.close()

def Replacebtn():
    global top2
    top2=Toplevel()
    top2.geometry("400x400")
    label1=Label(top2,text="Replace:")
    label1.grid(row=0,column=1)
    btn1=Button(top2,text="Single Pattern",command=Replace)
    btn1.grid(row=1,column=2)
    lblx=Label(top2,text="")
    lblx.grid(row=1,column=3)
    btn2=Button(top2,text="Two patterns",command=Replace3)
    btn2.grid(row=1,column=4)
    lbly=Label(top2,text="")
    lbly.grid(row=1,column=5)
  
def Replace():
    global textbox5
    global textbox6
    global str2
    global str1
    global str3
    lbl1=Label(top2,text="Enter the String to be replaced:")
    lbl1.grid(row=2,column=5)
    textbox5=Text(top2,width=3,height=1,font=("Helvetica",10))
    textbox5.grid(row=2,column=6)
    textbox6=Text(top2,width=3,height=1,font=("Helvetica",10))
    textbox6.grid(row=3,column=6)
    lbl2=Label(top2,text="Enter Replacement:")
    lbl2.grid(row=3,column=5)
    btn1=Button(top2,text="Replace",command=Replace2)
    btn1.grid(row=4,column=5)
   
     

def Replace2():
    str1=txtbox.get(1.0,END)
    str2=textbox5.get(1.0,END)
    str3=textbox6.get(1.0,END)
    rpl=re.sub(str2,str3,str1)
    txtbox2=Text(top2,width=15,height=10,font=("Helvetica",16))
    txtbox2.grid(row=6,column=4)
    text_file=open('demo2.txt','w',encoding="utf-8")
    text_file.write(rpl)
    text_file.close()
    text_file1=open('demo2.txt','r',encoding="utf-8")
    txt=text_file1.read()
    txtbox2.insert(END,txt)

def Replace3():
    global textbox7
    global textbox8
    global textbox9
    global textbox10
    global st1
    global st2
    global st3
    global st4
    lbl1=Label(top2,text="Enter the 1st String to be replaced:")
    lbl1.grid(row=2,column=5)
    textbox7=Text(top2,width=3,height=1,font=("Helvetica",10))
    textbox7.grid(row=2,column=6)
    lbl2=Label(top2,text="Enter the 2nd String to be replaced:")
    lbl2.grid(row=2,column=7)
    textbox8=Text(top2,width=3,height=1,font=("Helvetica",10))
    textbox8.grid(row=2,column=8)
    lbl3=Label(top2,text="Enter Replacement for 1st string:")
    lbl3.grid(row=3,column=5)
    textbox9=Text(top2,width=3,height=1,font=("Helvetica",10))
    textbox9.grid(row=3,column=6)
    lbl4=Label(top2,text="Enter Replacement for 2nd string:")
    lbl4.grid(row=3,column=7)
    textbox10=Text(top2,width=3,height=1,font=("Helvetica",10))
    textbox10.grid(row=3,column=8)            
    btn1=Button(top2,text="Replace",command=Replace4)
    btn1.grid(row=4,column=5)
    
def Replace4():
    text=txtbox.get(1.0,END)
    st1=textbox7.get(1.0,END)
    st3=textbox9.get(1.0,END)
    regex=re.sub(st1,st3,text)
    st2=textbox8.get(1.0,END)
    st4=textbox10.get(1.0,END)
    regex1=re.sub(st2,st4,regex,re.IGNORECASE)
    txtbox3=Text(top2,width=15,height=10,font=("Helvetica",16))
    txtbox3.grid(row=6,column=4)
    text_file=open('demo1.txt','w',encoding="utf-8")
    text_file.write(regex1)
    #text_file.close()
    text_file1=open('demo1.txt','r',encoding="utf-8")
    txt=text_file1.read()
    txtbox3.insert(END,txt)
    
def Extractbtn():
    global top3
    top3=Toplevel()
    top3.geometry("400x400")
    label1=Label(top3,text="Extract:")
    label1.grid(row=0,column=1)
    btn1=Button(top3,text="Phone Num",command=Extractbtn1)
    btn1.grid(row=1,column=2)
    lblx=Label(top3,text="")
    lblx.grid(row=1,column=3)
    btn2=Button(top3,text="Email",command=Extractbtn2)
    btn2.grid(row=1,column=4)
    lbly=Label(top3,text="")
    lbly.grid(row=1,column=5)

def Extractbtn1():
    text=txtbox.get(1.0,END)
    usphnum=re.findall("\+1\(\d{3}\)-\d{3}-\d{4}",text)
    inphnum=re.findall("\+91\d{10}",text)
    text_file=open('demo3.txt','w',encoding="utf-8")
    text_file.write("India Phone Numbers:{inphn}\nUS phone Numbers:{usphn}".format(inphn=inphnum,usphn=usphnum))
    
def Extractbtn2():
    text=txtbox.get(1.0,END)
    pattern="^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
    email=re.findall(pattern,text)
    text_file=open('demo4.txt','w',encoding="utf-8")
    text_file.write("Valid Emails:{eml}".format(eml=email))
    #text_file.close()
    #txtbox6=Text(top3,width=20,height=20)
    #txtbox6.grid(row=6,column=6)
    #text_file1=open('demo4.txt','w',encoding="utf-8")
    #txt=text_file1.read()
    #txtbox6.insert(END,txt)
def WebScrapping():
    url=txtbox.get(1.0,END)
    response=urllib.request.urlopen(url)
    html=response.read()
    text=html.decode()
    phonenum=re.findall("\(\d{3}\)\s\d{3}-\d{4}",text)
    usphnum=re.findall("\+1\(\d{3}\)-\d{3}-\d{4}",text)
    inphnum=re.findall("\+91\d{10}",text)
    email=re.findall("^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$",text)
    text_file=open('INFO.txt','w',encoding="utf-8")
    text_file.write("Phone nums:{phnnum}\nIndia Phone Numbers:{inphn}\nUS phone Numbers:{usphn}\nemails{emls}".format(phnnum=phonenum,inphn=inphnum,usphn=usphnum,emls=email))
    text_file.close()
    
txtbox=Text(root,width=40,height=10,font=("Helvetica",16))
txtbox.pack(pady=20)

button_frame=Frame(root)
button_frame.pack()

clear_button=Button(button_frame,text="Clear",command=clear)
clear_button.grid(row=0,column=0)

#get_text_button=Button(button_frame,text="Get text",command=gettxt)
#get_text_button.grid(row=0,column=1,padx=20)

open_button=Button(root,text="Open Text File",command=open_text)
open_button.pack(pady=20)

my_label=Label(root,text=" ")
my_label.pack(pady=20)

#save_button=Button(root,text="Save",command=save_text)
#save_button.pack(pady=20)

bottom_frame=Frame(root)
bottom_frame.pack(side=TOP,pady=10)

btn1=Button(bottom_frame,text="search",command=searchbtn)
btn1.grid(row=0,column=0)
btn2=Button(bottom_frame,text="Replace",command=Replacebtn)
btn2.grid(row=0,column=1)
btn3=Button(bottom_frame,text="Extract",command=Extractbtn)
btn3.grid(row=0,column=2)
btn4=Button(bottom_frame,text="WebScrapping",command=WebScrapping)
btn4.grid(row=0,column=3)
root.mainloop()
