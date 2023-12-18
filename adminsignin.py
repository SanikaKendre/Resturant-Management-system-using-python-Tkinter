# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 16:09:56 2023

@author: DELL
"""

from tkinter import *
from PIL import Image,ImageTk
import sqlite3
from tkinter import messagebox as ms
import re
root= Tk()
root.title("Welcome to Resturant Management application")
root.geometry('450x300')
root.configure(bg="black")

image1=Image.open("hhhh.jpg")
image1=image1.resize((700,700),Image.ANTIALIAS)
background_image=ImageTk.PhotoImage(image1)
background_label=Label(root,image=background_image)
background_label.image=background_image
background_label.place(x=0,y=0)

Username=StringVar()
Password=StringVar()

def insert():
    
    user = Username.get()
    pas = Password.get()
    if not user.strip or not pas.strip():
       ms.showinfo("Error!","username and password cannot be blank") 
       return
    db = sqlite3.connect('restproject.db')
    cursor = db.cursor()
    find_user = ('SELECT * FROM adsignup WHERE Username = ? AND Password=?')
    cursor.execute(find_user,[(Username.get()),(Password.get())])
    result=cursor.fetchall()
    if result:
        msg=""
        print(msg)   
        ms.showinfo("message","login successfully")
        from subprocess import call
        call(['python','operation.py'])
    else:
        ms.showinfo("oops!","username or password are not found match")
    
     
    
   
frame_alpr=LabelFrame(root,width=500,height=400,font=("times",14,"bold"),bg="#8B4500")
frame_alpr.grid(row=0,column=0)
frame_alpr.place(x=800,y=150)

label=Label(root,text="SIGN IN",bg="#8B4500",width=20,height=1,fg="black",font=("Arial",25,"underline bold"),underline=0)
label.place(x=850,y=200)

username1=Label(root,text="Username",bg="#8B4500",width=15,height=1,fg="white",font=("times",20,"bold"))
username1.place(x=800,y=280)

uentry=Entry(root,textvar=Username,width=15,font=("times",15,"bold"))
uentry.place(x=1100,y=280)

password1=Label(root,text="Password",bg="#8B4500",width=15,height=1,fg="white",font=("times",20,"bold"))
password1.place(x=800,y=360)

pentry=Entry(root,textvar=Password,width=15,font=("times",15,"bold"))
pentry.place(x=1100,y=360)

button=Button(root,text="Sign In",bg="#8FBC8F",width=10,height=1,fg="black",font=("times",15,"bold"),command=insert)
button.place(x=990,y=450)

root.mainloop()
