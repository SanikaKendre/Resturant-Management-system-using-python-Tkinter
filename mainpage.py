# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 15:47:03 2023

@author: DELL
"""

from tkinter import *
from tkinter import filedialog,messagebox
import random
import time
import requests
#functions
def reset():
    textreceipt.delete(1.0,END)
    e_roti.set('0')
    e_daal.set('0')
    e_fish.set('0')
    e_paneer.set('0')
    e_chiken.set('0')
    e_mutton.set('0')
    e_rice.set('0')
    e_kolhapuri.set('0')
    e_pulav.set('0')
    e_biryani.set('0')

    e_coffee.set('0')
    e_tea.set('0')
    e_lassi.set('0')
    e_faluda.set('0')
    e_mocktail.set('0')
    e_milkshake.set('0')
    e_coldcoffee.set('0')
    e_soda.set('0')
    e_matani.set('0')
    e_juice.set('0')

    e_choco.set('0')
    e_straw.set('0')
    e_pina.set('0')
    e_butter.set('0')
    e_black.set('0')
    e_white.set('0')
    e_oreo.set('0')
    e_kitkat.set('0')
    e_wel.set('0')
    e_ras.set('0')
    textroti.config(state=DISABLED)
    textdaal.config(state=DISABLED)
    textfish.config(state=DISABLED)
    textpaneer.config(state=DISABLED)
    textchiken.config(state=DISABLED)
    textmutton.config(state=DISABLED)
    textrice.config(state=DISABLED)
    textkolhapuri.config(state=DISABLED)
    textpulav.config(state=DISABLED)
    textbiryani.config(state=DISABLED)
    
    textcoffee.config(state=DISABLED)
    texttea.config(state=DISABLED)
    textlassi.config(state=DISABLED)
    textfaluda.config(state=DISABLED)
    textmocktail.config(state=DISABLED)
    textmilkshake.config(state=DISABLED)
    textcoldcoffee.config(state=DISABLED)
    textsoda.config(state=DISABLED)
    textmastani.config(state=DISABLED)
    textjuice.config(state=DISABLED)
    
    textchoco.config(state=DISABLED)
    textstraw.config(state=DISABLED)
    textpina.config(state=DISABLED)
    textbutter.config(state=DISABLED)
    textblack.config(state=DISABLED)
    textwhite.config(state=DISABLED)
    textoreo.config(state=DISABLED)
    textkitkat.config(state=DISABLED)
    textwelvet.config(state=DISABLED)
    textrasmalai.config(state=DISABLED)
    
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)
    var28.set(0)
    var29.set(0)
    var30.set(0)
    
    costfoodvar.set('')
    costdrinksvar.set('')
    costcakesvar.set('')
    costsubtotalvar.set('')
    costservicetaxvar.set('')
    totalcostvar.set('')
    
import requests
import json
from tkinter import *

import requests
import json
from tkinter import *

def send():
    if textreceipt.get(1.0, END) == '\n':
        pass 
    else:
        def send_msg():
            message = textarea.get(1.0, END)
            number = numberfield.get()
            auth = 'uLAVkW32XcP5R7zlHYGaiMBs8Cvm64ITpnUwrdeKOby09ExFjQJGhR09vHmWNjCIzESi43eZqr7nAQLP'
            url = 'https://www.fast2sms.com/dev/bulk'
            params = {
                'authorization': auth,
                'message': message,
                'numbers': number,
                'sender_id': 'FSTSMS',
                'route': 'p',
                'language': 'english'
            }
            try:
                # Enable SSL verification by setting verify to True
                response = requests.get(url, params=params, verify=True)
                
                # Check if the response status code is OK (200)
                if response.status_code == 200:
                    try:
                        dic = response.json()
                        result = dic.get('return')
                        if result == True:
                            messagebox.showinfo("send successfully", "Message sent successfully")
                        else:
                            messagebox.showinfo("Error", "Something went wrong")
                    except json.JSONDecodeError:
                        # If response is not in JSON format, handle it accordingly
                        messagebox.showinfo("Error", "Invalid JSON in response")
                else:
                    # If the response status code is not OK, handle it accordingly
                    messagebox.showinfo("Error", f"Request failed with status code {response.status_code}")
            except requests.exceptions.SSLError as e:
                messagebox.showinfo("Error", f"SSL Certificate Verification Failed: {str(e)}")
        
        root2 = Toplevel()
        root2.title("SEND BILL")
        root2.config(bg='red4')
        root2.geometry('485x620+50+50')
        
        numberlabel = Label(root2, text='Mobile Number', font=('arial', 18, 'bold underline'), bg='red4', fg='white')
        numberlabel.pack(pady=5)
    
        numberfield = Entry(root2, font=('helvetica', 22, 'bold'), bd=3, width=24)
        numberfield.pack(pady=5)
    
        billlabel = Label(root2, text='Bill Details', font=('arial', 18, 'bold underline'), bg='red4', fg='white')
        billlabel.pack(pady=5)
    
        textarea = Text(root2, font=('arial', 12, 'bold'), bd=3, width=42, height=14)
        textarea.pack(pady=5)
        textarea.insert(END, 'Reciept Ref:\t\t' + billnumber + '\t\t' + date + '\n')
        if costfoodvar.get() != '0 Rs':
            textarea.insert(END, f'Cost of Food\t\t\t{priceoffood}Rs\n')
        if costdrinksvar.get() != '0 Rs':
            textarea.insert(END, f'Cost of Drinks\t\t\t{priceofdrinks}Rs\n')
        if costcakesvar.get() != '0 Rs':
            textarea.insert(END, f'Cost of Cakes\t\t\t{priceofcakes}Rs\n')
        textarea.insert(END, f'Sub Total\t\t\t{subtotalitem}Rs\n\n')
        textarea.insert(END, f'Service Tax\t\t\t{50}Rs\n\n')
        textarea.insert(END, f'Total Cost\t\t\t{subtotalitem+50}Rs\n\n')
    
        sendbutton = Button(root2, text='SEND', font=('arial', 19, 'bold'), bg='white', fg='red4', bd=7, relief=GROOVE, command=send_msg)
        sendbutton.pack(pady=5)
    
        root2.mainloop()



def save():
    if textreceipt.get(1.0, END) == '\n':
        pass
    else:
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        if url is None:
            pass
        else:
            bill_data = textreceipt.get(1.0, END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo("Information", "Your bill is successfully saved")

def receipt():
    global billnumber,date
    if costfoodvar.get()!='' or costcakesvar.get()!='' or costdrinksvar.get()!='':
      textreceipt.delete(1.0, END)

      x=random.randint(100,10000)
      billnumber='BILL'+str(x)
      date=time.strftime('%d/%m/%Y')
      textreceipt.insert(END,'Receipt Ref:\t\t' +billnumber+ 't\t'+date+'\n')
      textreceipt.insert(END,'*******************************************************\n')
      textreceipt.insert(END,'Items:\t\t Cost Of Items(Rs)\n')
      textreceipt.insert(END,'*******************************************************\n')
   
      if e_roti.get()!='0':
       textreceipt.insert(END,f'Roti\t\t\t{int(e_roti.get())*10}\n\n')
      if e_daal.get()!='0':
        textreceipt.insert(END,f'Daal\t\t\t{int(e_daal.get())*60}\n\n')
      if e_fish.get()!='0':
        textreceipt.insert(END,f'Fish\t\t\t{int(e_fish.get())*100}\n\n')
      if e_paneer.get()!='0':
        textreceipt.insert(END,f'Panner\t\t\t{int(e_paneer.get())*200}\n\n')
      if e_chiken.get()!='0':
        textreceipt.insert(END,f'chiken\t\t\t{int(e_chiken.get())*250}\n\n')
      if e_mutton.get()!='0':
        textreceipt.insert(END,f'Mutton\t\t\t{int(e_mutton.get())*600}\n\n')
      if e_rice.get()!='0':
        textreceipt.insert(END,f'Rice\t\t\t{int(e_rice.get())*50}\n\n')
      if e_kolhapuri.get()!='0':
        textreceipt.insert(END,f'Veg Kolhapuri\t\t\t{int(e_kolhapuri.get())*180}\n\n')
      if e_pulav.get()!='0':
        textreceipt.insert(END,f'Pulav\t\t\t{int(e_pulav.get())*150}\n\n')
      if e_biryani.get()!='0':
        textreceipt.insert(END,f'Biryani\t\t\t{int(e_biryani.get())*300}\n\n')
   
      if e_coffee.get()!='0':
        textreceipt.insert(END,f'Coffee\t\t\t{int(e_coffee.get())*80}\n\n')
      if e_tea.get()!='0':
        textreceipt.insert(END,f'Tea\t\t\t{int(e_tea.get())*50}\n\n')
      if e_lassi.get()!='0':
        textreceipt.insert(END,f'Lassi\t\t\t{int(e_lassi.get())*70}\n\n')
      if e_faluda.get()!='0':
        textreceipt.insert(END,f'Faluda\t\t\t{int(e_faluda.get())*100}\n\n')
      if e_mocktail.get()!='0':
        textreceipt.insert(END,f'Mocktail\t\t\t{int(e_mocktail.get())*150}\n\n')
      if e_milkshake.get()!='0':
        textreceipt.insert(END,f'Milkshake\t\t\t{int(e_milkshake.get())*100}\n\n')
      if e_coldcoffee.get()!='0':
        textreceipt.insert(END,f'Coldcoffee\t\t\t{int(e_coldcoffee.get())*50}\n\n')
      if e_soda.get()!='0':
        textreceipt.insert(END,f'Soda\t\t\t{int(e_soda.get())*50}\n\n')
      if e_matani.get()!='0':
        textreceipt.insert(END,f'Mastani\t\t\t{int(e_matani.get())*80}\n\n')
      if e_juice.get()!='0':
        textreceipt.insert(END,f'Juice\t\t\t{int(e_juice.get())*50}\n\n')
    
      if e_choco.get()!='0':
        textreceipt.insert(END,f'Chocolatecake\t\t\t{int(e_choco.get())*300}\n\n')
      if e_straw.get()!='0':
        textreceipt.insert(END,f'Strawbwerry\t\t\t{int(e_straw.get())*250}\n\n')
      if e_pina.get()!='0':
        textreceipt.insert(END,f'Pinapple\t\t\t{int(e_pina.get())*200}\n\n')
      if e_butter.get()!='0':
        textreceipt.insert(END,f'Butterscoch\t\t\t{int(e_butter.get())*210}\n\n')
      if e_black.get()!='0':
        textreceipt.insert(END,f'BlackForest\t\t\t{int(e_black.get())*350}\n\n')
      if e_white.get()!='0':
        textreceipt.insert(END,f'WhiteForest\t\t\t{int(e_white.get())*350}\n\n')
      if e_oreo.get()!='0':
        textreceipt.insert(END,f'Oreo\t\t\t{int(e_oreo.get())*400}\n\n')
      if e_kitkat.get()!='0':
        textreceipt.insert(END,f'Kitkat\t\t\t{int(e_kitkat.get())*450}\n\n')
      if e_wel.get()!='0':
        textreceipt.insert(END,f'Welvet\t\t\t{int(e_wel.get())*280}\n\n')
      if e_ras.get()!='0':
        textreceipt.insert(END,f'Rasmalai\t\t\t{int(e_ras.get())*500}\n\n')
   
      textreceipt.insert(END,'*********************************************************\n')
      if costfoodvar.get()!='0 Rs':
        textreceipt.insert(END,f'Cost of Food\t\t\t{priceoffood}Rs\n\n' )
      if costfoodvar.get()!='0 Rs':
        textreceipt.insert(END,f'Cost of Drinks\t\t\t{priceofdrinks}Rs\n\n' )
      if costfoodvar.get()!='0 Rs':
        textreceipt.insert(END,f'Cost of Cakes\t\t\t{priceofcakes}Rs\n\n' )
      textreceipt.insert(END,f'Sub Total\t\t\t{subtotalitem}Rs\n\n')
      textreceipt.insert(END,f'Service Tax\t\t\t{50}Rs\n\n')
      textreceipt.insert(END,f'Total Cost\t\t\t{subtotalitem+50}Rs\n\n')
      textreceipt.insert(END,'*********************************************************\n')
    else:
        messagebox.showinfo("Error","Item is not selected")
    
    
def totalcost():
    global priceoffood,priceofdrinks,priceofcakes,subtotalitem
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or var6.get() != 0 or var8.get() != 0 or \
       var9.get() != 0 or var10.get() != 0 or var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
       var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or var21.get() != 0 or var22.get() != 0 or \
       var23.get() != 0 or var24.get() != 0 or var25.get() != 0 or var26.get() != 0 or var27.get() != 0 or var28.get() != 0 or var29.get() != 0 or \
       var30.get() != 0:
     item1=int(e_roti.get())
     item2=int(e_daal.get())
     item3=int(e_fish.get())
     item4=int(e_paneer.get())
     item5=int(e_chiken.get())
     item6=int(e_mutton.get())
     item7=int(e_rice.get())
     item8=int(e_kolhapuri.get())
     item9=int(e_pulav.get())
     item10=int(e_biryani.get())
    
    
    
     item11=int(e_coffee.get())
     item12=int(e_tea.get())
     item13=int(e_lassi.get())
     item14=int(e_faluda.get())
     item15=int(e_mocktail.get())
     item16=int(e_milkshake.get())
     item17=int(e_coldcoffee.get())
     item18=int(e_soda.get())
     item19=int(e_matani.get())
     item20=int(e_juice.get())
    
    
    
     item21=int(e_choco.get())
     item22=int(e_straw.get())
     item23=int(e_pina.get())
     item24=int(e_butter.get())
     item25=int(e_black.get())
     item26=int(e_white.get())
     item27=int(e_oreo.get())
     item28=int(e_kitkat.get())
     item29=int(e_wel.get())
     item30=int(e_ras.get())
     
    
     priceoffood=(item1*10)+(item2*60)+(item3*100)+(item4*200)+(item5*250)+(item6*600)+(item7*50)+(item8*180)+(item9*150)+(item10*300)
     priceofdrinks=(item11*80)+(item12*50)+(item13*70)+(item14*100)+(item15*150)+(item16*100)+(item17*50)+(item18*50)+(item19*80)+(item20*50)
     priceofcakes=(item21*300)+(item22*250)+(item23*200)+(item24*210)+(item25*350)+(item26*350)+(item27*400)+(item28*450)+(item29*280)+(item30*500)
 
     costfoodvar.set(str(priceoffood)+ ' Rs')
     costdrinksvar.set(str(priceofdrinks)+ ' Rs')
     costcakesvar.set(str(priceofcakes)+ ' Rs')
    
     subtotalitem=priceoffood+priceofdrinks+priceofcakes
     costsubtotalvar.set(str(subtotalitem) + ' Rs')

    
     costservicetaxvar.set('50 Rs')
    
     totalcost=subtotalitem+50
     totalcostvar.set(str(totalcost) + ' Rs')

    else:
        messagebox.showinfo("Error","there are no item is elected")

    
def roti():
    if var1.get() == 1:
        textroti.config(state=NORMAL)
        textroti.delete(0, END)
        textroti.focus()
    else:
        textroti.config(state=DISABLED)
        e_roti.set('0')

def daal():
    if var2.get() == 1:
        textdaal.config(state=NORMAL)
        textdaal.delete(0, END)
        textdaal.focus()
    else:
        textdaal.config(state=DISABLED)
        e_daal.set('0')

def fish():
    if var3.get() == 1:
        textfish.config(state=NORMAL)
        textfish.delete(0, END)
        textfish.focus()
    else:
        textfish.config(state=DISABLED)
        e_fish.set('0') 
def paneer():
    if var4.get() == 1:
        textpaneer.config(state=NORMAL)
        textpaneer.delete(0, END)
        textpaneer.focus()
    else:
        textpaneer.config(state=DISABLED)
        e_paneer.set('0')

def chiken():
    if var5.get() == 1:
        textchiken.config(state=NORMAL)
        textchiken.delete(0, END)
        textchiken.focus()
    else:
        textchiken.config(state=DISABLED)
        e_chiken.set('0')
def mutton():
    if var6.get() == 1:
        textmutton.config(state=NORMAL)
        textmutton.delete(0, END)
        textmutton.focus()
    else:
        textmutton.config(state=DISABLED)
        e_mutton.set('0')
        
def rice():
    if var7.get() == 1:
        textrice.config(state=NORMAL)
        textrice.delete(0, END)
        textrice.focus()
    else:
        textrice.config(state=DISABLED)
        e_rice.set('0')
def vegkolhapuri():
    if var8.get() == 1:
        textkolhapuri.config(state=NORMAL)
        textkolhapuri.delete(0, END)
        textkolhapuri.focus()
    else:
        textkolhapuri.config(state=DISABLED)
        e_kolhapuri.set('0')
def pulav():
    if var9.get() == 1:
        textpulav.config(state=NORMAL)
        textpulav.delete(0, END)
        textpulav.focus()
    else:
        textpulav.config(state=DISABLED)
        e_pulav.set('0')
def biryani():
    if var10.get() == 1:
        textbiryani.config(state=NORMAL)
        textbiryani.delete(0, END)
        textbiryani.focus()
    else:
        textbiryani.config(state=DISABLED)
        e_biryani.set('0')
        
        
        
def coffee():
    if var11.get() == 1:
        textcoffee.config(state=NORMAL)
        textcoffee.delete(0, END)
        textcoffee.focus()
    else:
        textcoffee.config(state=DISABLED)
        e_mcoffee.set('0')
        
def tea():
    if var12.get() == 1:
        texttea.config(state=NORMAL)
        texttea.delete(0, END)
        texttea.focus()
    else:
        texttea.config(state=DISABLED)
        e_tea.set('0')
def lassi():
    if var13.get() == 1:
        textlassi.config(state=NORMAL)
        textlassi.delete(0, END)
        textlassi.focus()
    else:
        textlassi.config(state=DISABLED)
        e_lassi.set('0')
def faluda():
    if var14.get() == 1:
        textfaluda.config(state=NORMAL)
        textfaluda.delete(0, END)
        textfaluda.focus()
    else:
        textfaluda.config(state=DISABLED)
        e_faluda.set('0')
def mocktail():
    if var15.get() == 1:
        textmocktail.config(state=NORMAL)
        textmocktail.delete(0, END)
        textmocktail.focus()
    else:
        textmocktail.config(state=DISABLED)
        e_mocktail.set('0')
def milkshake():
    if var16.get() == 1:
        textmilkshake.config(state=NORMAL)
        textmilkshake.delete(0, END)
        textmilkshake.focus()
    else:
        textmilkshake.config(state=DISABLED)
        e_milkshake.set('0')
def coldcoffee():
    if var17.get() == 1:
        textcoldcoffee.config(state=NORMAL)
        textcoldcoffee.delete(0, END)
        textcoldcoffee.focus()
    else:
        textcoldcoffee.config(state=DISABLED)
        e_coldcoffee.set('0')
def soda():
    if var18.get() == 1:
        textsoda.config(state=NORMAL)
        textsoda.delete(0, END)
        textsoda.focus()
    else:
        textsoda.config(state=DISABLED)
        e_soda.set('0')
def mastani():
    if var19.get() == 1:
        textmastani.config(state=NORMAL)
        textmastani.delete(0, END)
        textmastani.focus()
    else:
        textmastani.config(state=DISABLED)
        e_matani.set('0')
def juice():
    if var20.get() == 1:
        textjuice.config(state=NORMAL)
        textjuice.delete(0, END)
        textjuice.focus()
    else:
        textjuice.config(state=DISABLED)
        e_juice.set('0')
        
        
def chocolate():
    if var21.get() == 1:
        textchoco.config(state=NORMAL)
        textchoco.delete(0, END)
        textchoco.focus()
    else:
        textchoco.config(state=DISABLED)
        e_choco.set('0')
def strawberry():
    if var22.get() == 1:
        textstraw.config(state=NORMAL)
        textstraw.delete(0, END)
        textstraw.focus()
    else:
        textstraw.config(state=DISABLED)
        e_straw.set('0')
def pinapple():
    if var23.get() == 1:
        textpina.config(state=NORMAL)
        textpina.delete(0, END)
        textpina.focus()
    else:
        textpina.config(state=DISABLED)
        e_pina.set('0')
def butterscoch():
    if var24.get() == 1:
        textbutter.config(state=NORMAL)
        textbutter.delete(0, END)
        textbutter.focus()
    else:
        textbutter.config(state=DISABLED)
        e_butter.set('0')
def blackforest():
    if var25.get() == 1:
        textblack.config(state=NORMAL)
        textblack.delete(0, END)
        textblack.focus()
    else:
        textblack.config(state=DISABLED)
        e_black.set('0')
def whiteforest():
    if var26.get() == 1:
        textwhite.config(state=NORMAL)
        textwhite.delete(0, END)
        textwhite.focus()
    else:
        textwhite.config(state=DISABLED)
        e_white.set('0')
def oreo():
    if var27.get() == 1:
        textoreo.config(state=NORMAL)
        textoreo.delete(0, END)
        textoreo.focus()
    else:
        textoreo.config(state=DISABLED)
        e_oreo.set('0')
def kitkat():
    if var28.get() == 1:
        textkitkat.config(state=NORMAL)
        textkitkat.delete(0, END)
        textkitkat.focus()
    else:
        textkitkat.config(state=DISABLED)
        e_kitkat.set('0')
def welvet():
    if var29.get() == 1:
        textwelvet.config(state=NORMAL)
        textwelvet.delete(0, END)
        textwelvet.focus()
    else:
        textwelvet.config(state=DISABLED)
        e_wel.set('0')
def rasmalai():
    if var30.get() == 1:
        textrasmalai.config(state=NORMAL)
        textrasmalai.delete(0, END)
        textrasmalai.focus()
    else:
        textrasmalai.config(state=DISABLED)
        e_ras.set('0')
root=Tk()
root.geometry('1270x690+0+0')
#root.resizable(0,0)
root.title("Welcome to Resturant Management application")
root.config(bg="#8B7500")
topFrame=Frame(root,bd=10,relief=RIDGE,bg='#00008B')
topFrame.pack(side=TOP)

LabelTitle=Label(topFrame,text='Restaurant Management system',font=('arial',30,'bold'),fg='#DC143C',bd=9,bg='black',width=51)
LabelTitle.grid(row=0,column=0)

menuFrame=Frame(root,bd=10,relief=RIDGE,bg='#B8860B',width=100,height=550)
menuFrame.pack(side=LEFT)

costFrame=Frame(menuFrame,bd=4,relief=RIDGE,bg="#2F4F4F")
costFrame.pack(side=BOTTOM)

foodFrame=LabelFrame(menuFrame,text='Food',font=('arial',19,'bold'),bd=10,relief=RIDGE,bg='#B8860B')
foodFrame.pack(side=LEFT)

drinksFrame=LabelFrame(menuFrame,text='Drinks',font=('arial',19,'bold'),bd=10,relief=RIDGE,bg='#B8860B')
drinksFrame.pack(side=LEFT)

cakesFrame=LabelFrame(menuFrame,text='Cakes',font=('arial',19,'bold'),bd=10,relief=RIDGE,bg='#B8860B')
cakesFrame.pack(side=LEFT)

rightFrame=Frame(root,bd=5,relief=RIDGE,bg='#528B8B')
rightFrame.pack(side=RIGHT)

calculatorFrame=Frame(rightFrame,bd=1,relief=RIDGE,bg='#528B8B')
calculatorFrame.pack()

recieptFrame=Frame(rightFrame,bd=4,relief=RIDGE,bg='#528B8B')
recieptFrame.pack()

buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE,bg='#528B8B')
buttonFrame.pack()

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()

var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()


var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()
var27=IntVar()
var28=IntVar()
var29=IntVar()
var30=IntVar()

e_roti=StringVar()
e_daal=StringVar()
e_fish=StringVar()
e_paneer=StringVar()
e_chiken=StringVar()
e_mutton=StringVar()
e_rice=StringVar()
e_kolhapuri=StringVar()
e_pulav=StringVar()
e_biryani=StringVar()

e_coffee=StringVar()
e_tea=StringVar()
e_lassi=StringVar()
e_faluda=StringVar()
e_mocktail=StringVar()
e_milkshake=StringVar()
e_coldcoffee=StringVar()
e_soda=StringVar()
e_matani=StringVar()
e_juice=StringVar()


e_choco=StringVar()
e_straw=StringVar()
e_pina=StringVar()
e_butter=StringVar()
e_black=StringVar()
e_white=StringVar()
e_oreo=StringVar()
e_kitkat=StringVar()
e_wel=StringVar()
e_ras=StringVar()

costfoodvar=StringVar()
costdrinksvar=StringVar()
costcakesvar=StringVar()
costsubtotalvar=StringVar()
costservicetaxvar=StringVar()
totalcostvar=StringVar()


e_roti.set('0')
e_daal.set('0')
e_fish.set('0')
e_paneer.set('0')
e_chiken.set('0')
e_mutton.set('0')
e_rice.set('0')
e_kolhapuri.set('0')
e_pulav.set('0')
e_biryani.set('0')

e_coffee.set('0')
e_tea.set('0')
e_lassi.set('0')
e_faluda.set('0')
e_mocktail.set('0')
e_milkshake.set('0')
e_coldcoffee.set('0')
e_soda.set('0')
e_matani.set('0')
e_juice.set('0')

e_choco.set('0')
e_straw.set('0')
e_pina.set('0')
e_butter.set('0')
e_black.set('0')
e_white.set('0')
e_oreo.set('0')
e_kitkat.set('0')
e_wel.set('0')
e_ras.set('0')

roti=Checkbutton(foodFrame,text='Roti',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var1,bg="#B8860B",command=roti)
roti.grid(row=0,column=0,sticky=W)

daal=Checkbutton(foodFrame,text='Daal',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var2,bg="#B8860B",command=daal)
daal.grid(row=1,column=0,sticky=W)

fish=Checkbutton(foodFrame,text='Fish',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var3,bg="#B8860B",command=fish)
fish.grid(row=2,column=0,sticky=W)

panner=Checkbutton(foodFrame,text='Paneer',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var4,bg="#B8860B",command=paneer)
panner.grid(row=3,column=0,sticky=W)

chiken=Checkbutton(foodFrame,text='Chiken',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var5,bg="#B8860B",command=chiken)
chiken.grid(row=4,column=0,sticky=W)

mutton=Checkbutton(foodFrame,text='Mutton',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var6,bg="#B8860B",command=mutton)
mutton.grid(row=5,column=0,sticky=W)

rice=Checkbutton(foodFrame,text='Rice',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var7,bg="#B8860B",command=rice)
rice.grid(row=6,column=0,sticky=W)

vegkolhapuri=Checkbutton(foodFrame,text='Veg Kolhapuri',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var8,bg="#B8860B",command=vegkolhapuri)
vegkolhapuri.grid(row=7,column=0,sticky=W)

pulav=Checkbutton(foodFrame,text='Pulav',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var9,bg="#B8860B",command=pulav)
pulav.grid(row=8,column=0,sticky=W)

biryani=Checkbutton(foodFrame,text='Biryani',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var10,bg="#B8860B",command=biryani)
biryani.grid(row=9,column=0,sticky=W)

textroti=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_roti)
textroti.grid(row=0,column=1)

textdaal=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_daal)
textdaal.grid(row=1,column=1)

textfish=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_fish)
textfish.grid(row=2,column=1)

textpaneer=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_paneer)
textpaneer.grid(row=3,column=1)

textchiken=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_chiken)
textchiken.grid(row=4,column=1)

textmutton=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_mutton)
textmutton.grid(row=5,column=1)

textrice=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_rice)
textrice.grid(row=6,column=1)

textkolhapuri=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_kolhapuri)
textkolhapuri.grid(row=7,column=1)

textpulav=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_pulav)
textpulav.grid(row=8,column=1)

textbiryani=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_biryani)
textbiryani.grid(row=9,column=1)

##Drinks

cofee=Checkbutton(drinksFrame,text='Coffee',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var11,bg="#B8860B",command=coffee)
cofee.grid(row=0,column=0,sticky=W)

tea=Checkbutton(drinksFrame,text='Tea',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var12,bg="#B8860B",command=tea)
tea.grid(row=1,column=0,sticky=W)

lassi=Checkbutton(drinksFrame,text='Lassi',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var13,bg="#B8860B",command=lassi)
lassi.grid(row=2,column=0,sticky=W)

faluda=Checkbutton(drinksFrame,text='Faluda',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var14,bg="#B8860B",command=faluda)
faluda.grid(row=3,column=0,sticky=W)

mocktail=Checkbutton(drinksFrame,text='Mocktail',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var15,bg="#B8860B",command=mocktail)
mocktail.grid(row=4,column=0,sticky=W)

milkshake=Checkbutton(drinksFrame,text='Milkshake',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var16,bg="#B8860B",command=milkshake)
milkshake.grid(row=5,column=0,sticky=W)

coldcoffee=Checkbutton(drinksFrame,text='Cold coffee',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var17,bg="#B8860B",command=coldcoffee)
coldcoffee.grid(row=6,column=0,sticky=W)

soda=Checkbutton(drinksFrame,text='Soda',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var18,bg="#B8860B",command=soda)
soda.grid(row=7,column=0,sticky=W)

mastani=Checkbutton(drinksFrame,text='Mastani',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var19,bg="#B8860B",command=mastani)
mastani.grid(row=8,column=0,sticky=W)

juice=Checkbutton(drinksFrame,text='Juice',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var20,bg="#B8860B",command=juice)
juice.grid(row=9,column=0,sticky=W)

#drinksentry

textcoffee=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_coffee)
textcoffee.grid(row=0,column=1)

texttea=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_tea)
texttea.grid(row=1,column=1)

textlassi=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_lassi)
textlassi.grid(row=2,column=1)

textfaluda=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_faluda)
textfaluda.grid(row=3,column=1)

textmocktail=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_mocktail)
textmocktail.grid(row=4,column=1)

textmilkshake=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_milkshake)
textmilkshake.grid(row=5,column=1)

textcoldcoffee=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_coldcoffee)
textcoldcoffee.grid(row=6,column=1)

textsoda=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_soda)
textsoda.grid(row=7,column=1)

textmastani=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_matani)
textmastani.grid(row=8,column=1)

textjuice=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_juice)
textjuice.grid(row=9,column=1)

#cakes

chocolatecake=Checkbutton(cakesFrame,text='Chocolate',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var21,bg="#B8860B",command=chocolate)
chocolatecake.grid(row=0,column=0,sticky=W)

strawberrycake=Checkbutton(cakesFrame,text='Strawberry',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var22,bg="#B8860B",command=strawberry)
strawberrycake.grid(row=1,column=0,sticky=W)

pinapplecake=Checkbutton(cakesFrame,text='Pinapple',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var23,bg="#B8860B",command=pinapple)
pinapplecake.grid(row=2,column=0,sticky=W)

buttercake=Checkbutton(cakesFrame,text='Buteerscoch',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var24,bg="#B8860B",command=butterscoch)
buttercake.grid(row=3,column=0,sticky=W)

blackcake=Checkbutton(cakesFrame,text='Black Forest',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var25,bg="#B8860B",command=blackforest)
blackcake.grid(row=4,column=0,sticky=W)

whitecake=Checkbutton(cakesFrame,text='White Forest',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var26,bg="#B8860B",command=whiteforest)
whitecake.grid(row=5,column=0,sticky=W)

oreocake=Checkbutton(cakesFrame,text='Oreo',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var27,bg="#B8860B",command=oreo)
oreocake.grid(row=6,column=0,sticky=W)

kitkatcake=Checkbutton(cakesFrame,text='Kitkat',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var28,bg="#B8860B",command=kitkat)
kitkatcake.grid(row=7,column=0,sticky=W)

welvetcake=Checkbutton(cakesFrame,text='Welvet',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var29,bg="#B8860B",command=welvet)
welvetcake.grid(row=8,column=0,sticky=W)

rasmalaicake=Checkbutton(cakesFrame,text='Rasmalai',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var30,bg="#B8860B",command=rasmalai)
rasmalaicake.grid(row=9,column=0,sticky=W)


#cakes entry
textchoco=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_choco)
textchoco.grid(row=0,column=1)

textstraw=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_straw)
textstraw.grid(row=1,column=1)

textpina=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_pina)
textpina.grid(row=2,column=1)

textbutter=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_butter)
textbutter.grid(row=3,column=1)

textblack=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_black)
textblack.grid(row=4,column=1)

textwhite=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_white)
textwhite.grid(row=5,column=1)

textoreo=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_oreo)
textoreo.grid(row=6,column=1)

textkitkat=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_kitkat)
textkitkat.grid(row=7,column=1)

textwelvet=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_wel)
textwelvet.grid(row=8,column=1)

textrasmalai=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_ras)
textrasmalai.grid(row=9,column=1)

#Cost

labelcostfood=Label(costFrame,text='Cost of Food',font=('arial',16,'bold'),bg='#2F4F4F',fg='white')
labelcostfood.grid(row=0,column=0)

textcostfood=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costfoodvar)
textcostfood.grid(row=0,column=1,padx=41)

labelcostdrinks=Label(costFrame,text='Cost of Drinks',font=('arial',16,'bold'),bg='#2F4F4F',fg='white')
labelcostdrinks.grid(row=1,column=0)

textcostdrinks=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costdrinksvar)
textcostdrinks.grid(row=1,column=1,padx=41)

labelcostcake=Label(costFrame,text='Cost of Cakes',font=('arial',16,'bold'),bg='#2F4F4F',fg='white')
labelcostcake.grid(row=2,column=0)

textcostcake=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costcakesvar)
textcostcake.grid(row=2,column=1,padx=41)

labelsubtotal=Label(costFrame,text='Sub Total',font=('arial',16,'bold'),bg='#2F4F4F',fg='white')
labelsubtotal.grid(row=0,column=2)

textsubtotal=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costsubtotalvar)
textsubtotal.grid(row=0,column=3,padx=41)

labelservicetax=Label(costFrame,text='Service Tax',font=('arial',16,'bold'),bg='#2F4F4F',fg='white')
labelservicetax.grid(row=1,column=2)

textservicetax=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costservicetaxvar)
textservicetax.grid(row=1,column=3,padx=41)

labeltotalcost=Label(costFrame,text='Total Cost',font=('arial',16,'bold'),bg='#2F4F4F',fg='white')
labeltotalcost.grid(row=2,column=2)

texttotalcost=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=totalcostvar)
texttotalcost.grid(row=2,column=3,padx=41)

##Buttons

buttontotal=Button(buttonFrame,text='Total',font=('arial',14,'bold'),fg='white',bg='#8B3A62',bd=3,padx=5,command=totalcost)
buttontotal.grid(row=0,column=0)

buttonreciept=Button(buttonFrame,text='Receipt',font=('arial',14,'bold'),fg='white',bg='#8B3A62',bd=3,padx=5,command=receipt)
buttonreciept.grid(row=0,column=1)

buttonsave=Button(buttonFrame,text='Save',font=('arial',14,'bold'),fg='white',bg='#8B3A62',bd=3,padx=5,command=save)
buttonsave.grid(row=0,column=2)

buttonsend=Button(buttonFrame,text='Send',font=('arial',14,'bold'),fg='white',bg='#8B3A62',bd=3,padx=5,command=send)
buttonsend.grid(row=0,column=3)

buttonreset=Button(buttonFrame,text='Reset',font=('arial',14,'bold'),fg='white',bg='#8B3A62',bd=3,padx=5,command=reset)
buttonreset.grid(row=0,column=4)

textreceipt=Text(recieptFrame,font=('arial',12,'bold'),bd=3,width=42,height=14)
textreceipt.grid(row=0,column=0)

#Calculator

operator=''
def buttonclick(numbers):
    global operator
    operator=operator+numbers
    calculatorfield.delete(0,END)
    calculatorfield.insert(END,operator)
def clear():
    global operator
    operator=''
    calculatorfield.delete(0,END)
def answer():
    global operator
    result=str(eval(operator))
    calculatorfield.delete(0,END)
    calculatorfield.insert(0,result)
    operator=''
    

calculatorfield=Entry(calculatorFrame,font=('arial',16,'bold'),width=32,bd=4)
calculatorfield.grid(row=0,column=0,columnspan=4)

button7=Button(calculatorFrame,text='7',font=('arial',16,'bold'),fg='black',bg='#FF6A6A',bd=6,width=6,command=lambda:buttonclick('7'))
button7.grid(row=1,column=0)

button8=Button(calculatorFrame,text='8',font=('arial',16,'bold'),fg='black',bg='#FF6A6A',bd=6,width=6,command=lambda:buttonclick('8'))
button8.grid(row=1,column=1)

button9=Button(calculatorFrame,text='9',font=('arial',16,'bold'),fg='black',bg='#FF6A6A',bd=6,width=6,command=lambda:buttonclick('9'))
button9.grid(row=1,column=2)

buttonplus=Button(calculatorFrame,text='+',font=('arial',16,'bold'),fg='black',bg='#FF6A6A',bd=6,width=6,command=lambda:buttonclick('+'))
buttonplus.grid(row=1,column=3)

button4=Button(calculatorFrame,text='4',font=('arial',16,'bold'),fg='black',bg='#FF6A6A',bd=6,width=6,command=lambda:buttonclick('4'))
button4.grid(row=2,column=0)

button5=Button(calculatorFrame,text='5',font=('arial',16,'bold'),fg='black',bg='white',bd=6,width=6,command=lambda:buttonclick('5'))
button5.grid(row=2,column=1)

button6=Button(calculatorFrame,text='6',font=('arial',16,'bold'),fg='black',bg='white',bd=6,width=6,command=lambda:buttonclick('6'))
button6.grid(row=2,column=2)

buttonminus=Button(calculatorFrame,text='-',font=('arial',16,'bold'),fg='black',bg='#FF6A6A',bd=6,width=6,command=lambda:buttonclick('-'))
buttonminus.grid(row=2,column=3)

button1=Button(calculatorFrame,text='1',font=('arial',16,'bold'),fg='black',bg='#FF6A6A',bd=6,width=6,command=lambda:buttonclick('1'))
button1.grid(row=3,column=0)

button2=Button(calculatorFrame,text='2',font=('arial',16,'bold'),fg='black',bg='white',bd=6,width=6,command=lambda:buttonclick('2'))
button2.grid(row=3,column=1)

button3=Button(calculatorFrame,text='3',font=('arial',16,'bold'),fg='black',bg='white',bd=6,width=6,command=lambda:buttonclick('3'))
button3.grid(row=3,column=2)

buttonmul=Button(calculatorFrame,text='*',font=('arial',16,'bold'),fg='black',bg='#FF6A6A',bd=6,width=6,command=lambda:buttonclick('*'))
buttonmul.grid(row=3,column=3)

buttonans=Button(calculatorFrame,text='Ans',font=('arial',16,'bold'),fg='black',bg='#FF6A6A',bd=6,width=6,command=answer)
buttonans.grid(row=4,column=0)

buttonclear=Button(calculatorFrame,text='Clear',font=('arial',16,'bold'),fg='black',bg='#FF6A6A',bd=6,width=6,command=clear)
buttonclear.grid(row=4,column=1)

button0=Button(calculatorFrame,text='0',font=('arial',16,'bold'),fg='black',bg='#FF6A6A',bd=6,width=6,command=lambda:buttonclick('7'))
button0.grid(row=4,column=2)

buttondiv=Button(calculatorFrame,text='/',font=('arial',16,'bold'),fg='black',bg='#FF6A6A',bd=6,width=6,command=lambda:buttonclick('/'))
buttondiv.grid(row=4,column=3)

root.mainloop()

