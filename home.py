from tkinter import *
from PIL import Image, ImageTk

# adjust window
root = Tk()
root.geometry("200x200")

# function to resize and load images
def load_and_resize_image(file_path, width, height):
    original_image = Image.open(file_path)
    resized_image = original_image.resize((width, height), Image.ANTIALIAS)
    return ImageTk.PhotoImage(resized_image)

# loading the resized images
img = load_and_resize_image("im1.jpg", 1500, 600)
img2 = load_and_resize_image("im2.jpg", 1500, 600)
img3 = load_and_resize_image("im3.jpg", 1500, 600)
img4 = load_and_resize_image("im4.jpg", 1500, 600)


l = Label()
l.pack()

# using recursion to slide to the next image
x = 1

# function to change to the next image
def move():
    global x
    if x == 5:
        x = 1
    if x == 1:
        l.config(image=img)
    elif x == 2:
        l.config(image=img2)
    elif x == 3:
        l.config(image=img3)
    elif x == 4:
        l.config(image=img4)
    l.place(x=0,y=100)
    x = x + 1
    root.after(1500, move)

# calling the function
move()


main_label=Label(root,text="RESTURANT MANAGEMENT SYSTEM",width=70,height=1,fg="black",bg="#FAEBD7",font=("times",25,"bold"))
main_label.place(x=0,y=0)

sub_label=Label(root,bg="#FFD39B",width=90,height=2,fg="white",font=("times",20,"bold"))
sub_label.place(x=0,y=40)

def home():
    from subprocess import call
    call(['python','home.py'])
def signup():
    from subprocess import call
    call(['python','adminsignup.py'])
def signin():
    from subprocess import call
    call(['python','adminsignin.py'])

button=Button(root,text="Sign Up",command=signup,bg="#FFBBFF",width=10,height=1,fg="blue",font=("times",15,"bold"))
button.place(x=100,y=50)

button1=Button(root,text="Sign In",command=signin,bg="#FFBBFF",width=10,height=1,fg="blue",font=("times",15,"bold"))
button1.place(x=1150,y=50)

button2=Button(root,text="Home",command=home,bg="#FFBBFF",width=10,height=1,fg="blue",font=("times",15,"bold"))
button2.place(x=650,y=50)

root.mainloop()