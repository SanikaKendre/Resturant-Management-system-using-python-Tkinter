# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 19:43:02 2023

@author: DELL
"""

from tkinter import *
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
root= Tk()
root.title("Welcome to Resturant Management application")
root.geometry('450x300')
root.configure(bg="#DC143C")

Name=StringVar()
Username=StringVar()
Password=StringVar()

db = sqlite3.connect('restproject.db')
cursor = db.cursor()
create_table ='''CREATE TABLE IF NOT EXISTS adsignup(
                            Name TEXT,
                            Username TEXT,
                            Password TEXT
                          );'''
cursor.execute(create_table)
db.commit()

def password_check(passwd): 
	
	SpecialSym =['$', '@', '#', '%'] 
	val = True
	
	if len(passwd) < 6: 
		print('length should be at least 6') 
		val = False
		
	if len(passwd) > 20: 
		print('length should be not be greater than 8') 
		val = False
		
	if not any(char.isdigit() for char in passwd): 
		print('Password should have at least one numeral') 
		val = False
		
	if not any(char.isupper() for char in passwd): 
		print('Password should have at least one uppercase letter') 
		val = False
		
	if not any(char.islower() for char in passwd): 
		print('Password should have at least one lowercase letter') 
		val = False
		
	if not any(char in SpecialSym for char in passwd): 
		print('Password should have at least one of the symbols $@#') 
		val = False
        
	if val: 
		return val 
def insert():
    name = Name.get()
    user = Username.get()
    pas = Password.get()
    db = sqlite3.connect('restproject.db')
    cursor = db.cursor()
    find_user = ('SELECT * FROM adsignup WHERE Username = ?')
    cursor.execute(find_user, [(Username.get())])
    
    
    if (name.isdigit() or (name == "")):
       ms.showinfo("Message", "please enter valid name")
    elif(user.isdigit()or(user=="")):
       ms.showinfo("Message", "please enter valid username")
    elif (cursor.fetchall()):
       ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
    elif (pas == ""):
       ms.showinfo("Message", "Please Enter valid password")
    elif(pas=="")or(password_check(pas))!=True:
       ms.showinfo("Message", "password must contain atleast 1 Uppercase letter,1 symbol,1 number")
    else:
       db = sqlite3.connect('restproject.db')
       cursor = db.cursor()
       
       insert_query='''INSERT INTO adsignup(Name,Username,Password) VALUES(?,?,?);'''
       user_data=(name,user,pas)
       cursor.execute(insert_query,user_data)
       db.commit()
       db.close()
       ms.showinfo('Success!', 'Account Created Successfully !')
       from subprocess import call
       call(['python','adminsignin.py'])

sub_label=Label(root,bg="#CD5B45",width=90,height=2,fg="white",font=("times",20,"bold"))
sub_label.place(x=0,y=0)

main_label=Label(root,text="RESTURANT MANAGEMENT SYSTEM",width=43,height=1,fg="white",bg="#CD5B45",font=("times",30,"bold"))
main_label.place(x=150,y=0)

image1=Image.open("hhh.jpg")
image1=image1.resize((300,150),Image.ANTIALIAS)
background_image=ImageTk.PhotoImage(image1)
background_label=Label(root,image=background_image)
background_label.image=background_image
background_label.place(x=0,y=60)

image1=Image.open("h2.jpg")
image1=image1.resize((300,150),Image.ANTIALIAS)
background_image=ImageTk.PhotoImage(image1)
background_label=Label(root,image=background_image)
background_label.image=background_image
background_label.place(x=300,y=60)

image1=Image.open("h4.jpg")
image1=image1.resize((300,150),Image.ANTIALIAS)
background_image=ImageTk.PhotoImage(image1)
background_label=Label(root,image=background_image)
background_label.image=background_image
background_label.place(x=600,y=60)

image1=Image.open("hhhh.jpg")
image1=image1.resize((300,150),Image.ANTIALIAS)
background_image=ImageTk.PhotoImage(image1)
background_label=Label(root,image=background_image)
background_label.image=background_image
background_label.place(x=900,y=60)

image1=Image.open("h3.jpg")
image1=image1.resize((170,150),Image.ANTIALIAS)
background_image=ImageTk.PhotoImage(image1)
background_label=Label(root,image=background_image)
background_label.image=background_image
background_label.place(x=1200,y=60)

image1=Image.open("h.jpg")
image1=image1.resize((350,550),Image.ANTIALIAS)
background_image=ImageTk.PhotoImage(image1)
background_label=Label(root,image=background_image)
background_label.image=background_image
background_label.place(x=0,y=210)

image1=Image.open("h5.jpg")
image1=image1.resize((500,550),Image.ANTIALIAS)
background_image=ImageTk.PhotoImage(image1)
background_label=Label(root,image=background_image)
background_label.image=background_image
background_label.place(x=900,y=210)

frame_alpr=LabelFrame(root,width=600,height=493,font=("times",14,"bold"),bg="black")
frame_alpr.grid(row=0,column=0)
frame_alpr.place(x=350,y=210)

label=Label(root,text="SIGN UP",bg="black",width=20,height=1,fg="pink",font=("Arial",25,"underline bold"),underline=0)
label.place(x=450,y=240)

name1=Label(root,text="Name",bg="black",width=15,height=1,fg="white",font=("times",20,"bold"))
name1.place(x=380,y=350)

nentry=Entry(root,textvar=Name,width=15,font=("times",15,"bold"))
nentry.place(x=700,y=355)

username1=Label(root,text="Username",bg="black",width=15,height=1,fg="white",font=("times",20,"bold"))
username1.place(x=380,y=450)

uentry=Entry(root,textvar=Username,width=15,font=("times",15,"bold"))
uentry.place(x=700,y=455)

password1=Label(root,text="Password",bg="black",width=15,height=1,fg="white",font=("times",20,"bold"))
password1.place(x=380,y=550)

pentry=Entry(root,textvar=Password,width=15,font=("times",15,"bold"))
pentry.place(x=700,y=555)

button=Button(root,text="Sign Up",bg="#8FBC8F",width=10,height=1,fg="black",font=("times",15,"bold"),command=insert)
button.place(x=575,y=640)

root.mainloop()