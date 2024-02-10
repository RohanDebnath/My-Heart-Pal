from tkinter import *
from datetime import date
from tkinter.ttk import Combobox
import tkinter as tk 
from tkinter import ttk 
import os 
import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasAgg

from matplotlib.figure import Figure
import numpy as np 
import matplotlib.pyplot as plt 

background="#f0ddd5"
framebg="#62a7ff"
framefg="#fefbfb"

root=Tk()
root.title("Heart Attack Prediction System Using Machine Learning")
root.geometry("1450x730+60+80")
root.state('zoomed')
root.resizable(False,False)
root.config(bg=background)

#Logo portion
img_icon = PhotoImage(file="D:\Project\Python AI Projects\My Heart Pal\icon.png")
root.iconphoto(False, img_icon)

#header
logo=PhotoImage(file="D:\Project\Python AI Projects\My Heart Pal\header.png")
myImage=Label(image=logo,bg=background)
myImage.place(x=-200,y=-20)

#frame portion

Heading_entry = Frame(root, width=800, height=190, bg="#FDD0D3", highlightthickness=0)
Heading_entry.place(x=0, y=0)
Label(Heading_entry, text="Registration No:", font="Arial 13", bg="#FDD0D3", fg="black").place(x=10, y=20)
Label(Heading_entry, text="Date:", font="Arial 13", bg="#FDD0D3", fg="black").place(x=550, y=20)
Label(Heading_entry, text="Patient Name:", font="Arial 13", bg="#FDD0D3", fg="black").place(x=10, y=100)
Label(Heading_entry, text="Date of Birth:", font="Arial 13", bg="#FDD0D3", fg="black").place(x=550, y=100)

Label(Heading_entry, font="Arial 13", bg="white",width=30, fg="black").place(x=150, y=20)
Label(Heading_entry, font="Arial 13", bg="white",width=30, fg="black").place(x=650, y=20)
Label(Heading_entry, font="Arial 13", bg="white",width=30, fg="black").place(x=150, y=100)
Label(Heading_entry, font="Arial 13", bg="white",width=30, fg="black").place(x=650, y=100)

Registration=IntVar()
reg_entry=Entry(Heading_entry,textvariable=Registration,width=30,font="Arial 15",bg="white",fg="black",).place(x=150,y=20)

Date=StringVar()
today=date.today()
d1=today.strftime("%d/%m/%y")
date_entry=Entry(Heading_entry,textvariable=Date,width=15,font="Arial 15",bg="white",fg="black").place(x=650,y=20)
Date.set(d1)

Name=StringVar()
name_entry=Entry(Heading_entry,textvariable=Name,width=30,font="Arial 15",bg="white",fg="black",).place(x=150,y=100)

DOB=IntVar()
dob_entry=Entry(Heading_entry,textvariable=DOB,width=10,font="Arial 15",bg="white",fg="black",bd=0).place(x=650,y=100)


#Body Portion
Detail_entry=Frame(root,width=600,height=600,bg="#FDD0D3")
Detail_entry.place(x=0,y=335)

#radio Button
Label(Detail_entry,text="Sex: ",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=10)
Label(Detail_entry,text="Fbs: ",font="arial 13",bg=framebg,fg=framefg).place(x=180,y=10)
Label(Detail_entry,text="Exang: ",font="arial 13",bg=framebg,fg=framefg).place(x=335,y=10)

def selection():
    if gen.get()==1:
        Gender=1
        return(Gender)
        print(Gender)
    elif gen.get()==2:
        Gender=0
        return(Gender)
        print(Gender)
    else:
        print(Gender)

def selection2():
    if fbs.get()==1:
        Fbs=1
        return(Fbs)
        print(Fbs)
    elif fbs.get()==2:
        Fbs=0
        return(Fbs)
        print(Fbs)
    else:
        print(Fbs)

def selection3():
    if exang.get()==1:
        Exang=1
        return(Exang)
        print(Exang)
    elif exang.get()==2:
        Exang=0
        return(Exang)
        print(Exang)
    else:
        print(Exang)

gen = IntVar()
R1 = Radiobutton(Detail_entry, text="Male", variable=gen, value=1, command=selection)
R1.place(x=43, y=10)
R2 = Radiobutton(Detail_entry, text="Female", variable=gen, value=2, command=selection)
R2.place(x=93, y=10)

fbs = IntVar()
R3 = Radiobutton(Detail_entry, text="True", variable=fbs, value=1, command=selection2)
R3.place(x=213, y=10)
R4 = Radiobutton(Detail_entry, text="False", variable=fbs, value=2, command=selection2)
R4.place(x=263, y=10)

exang = IntVar()
R5 = Radiobutton(Detail_entry, text="Yes", variable=exang, value=1, command=selection3)
R5.place(x=387, y=10)
R6 = Radiobutton(Detail_entry, text="No", variable=exang, value=2, command=selection3)
R6.place(x=430, y=10)

#ComboBox
Label(Detail_entry,text="cp:",font="arial 13",width=8,bg=framebg,fg=framefg).place(x=10,y=50)
Label(Detail_entry,text="restecg:",font="arial 13",width=8,bg=framebg,fg=framefg).place(x=10,y=90)
Label(Detail_entry,text="slope:",font="arial 13",width=8,bg=framebg,fg=framefg).place(x=10,y=130)
Label(Detail_entry,text="ca:",font="arial 13",width=8,bg=framebg,fg=framefg).place(x=10,y=170)
Label(Detail_entry,text="thal:",font="arial 13",width=8,bg=framebg,fg=framefg).place(x=10,y=210)

def selection4():
    input=cp_combobox.get()
    if input=="0=typical angina":
        return(0)
    elif input=="1=atypical angina":
        return(1)
    elif input=="2=non-angial pain":
        return(2)
    elif input=="3-asymtomatic":
        return(3)
    else:
        print(exang)

def selection4():
    input=slope_combobox.get()
    if input=="0=unsloping":
        return(0)
    elif input=="1=flat":
        return(1)
    elif input=="2=downsloping":
        return(2)
    else:
        print(exang)


cp_combobox=Combobox(Detail_entry,values=["0=typical angina","1=atypical angina","2=non-angial pain","3-asymtomatic"],font="arial 12",state="r",width=20)
restecg_combobox=Combobox(Detail_entry,values=["0","1","2"],font="arial 12",state="r",width=20)
slope_combobox=Combobox(Detail_entry,values=["0=unsloping","1=flat","2=downsloping"],font="arial 12",state="r",width=20)
ca_combobox=Combobox(Detail_entry,values=["0","1","2","3","4"],font="arial 12",state="r",width=20)
thal_combobox=Combobox(Detail_entry,values=["0","1","2","3"],font="arial 12",state="r",width=20)

cp_combobox.place(x=100,y=50)
restecg_combobox.place(x=100,y=90)
slope_combobox.place(x=100,y=130)
ca_combobox.place(x=100,y=170)
thal_combobox.place(x=100,y=210)

#DataEntry Box
Label(Detail_entry,text="Smoking",font="arial 13",width=8,bg=framebg,fg=framefg).place(x=10,y=250)
Label(Detail_entry,text="trestbps",font="arial 13",width=8,bg=framebg,fg=framefg).place(x=10,y=290)
Label(Detail_entry,text="chol",font="arial 13",width=8,bg=framebg,fg=framefg).place(x=10,y=330)
Label(Detail_entry,text="thalach",font="arial 13",width=8,bg=framebg,fg=framefg).place(x=10,y=370)
Label(Detail_entry,text="oldpeak",font="arial 13",width=8,bg=framebg,fg=framefg).place(x=10,y=410)

trestbps=StringVar()
chol=StringVar()
thalach=StringVar()
oldpeak=StringVar()

trestbps_entry=Entry(Detail_entry,textvariable=trestbps,width=20,font="arial 12",bg="white",fg="black",bd=0)
chol_entry=Entry(Detail_entry,textvariable=chol,width=20,font="arial 12",bg="white",fg="black",bd=0)
thalach_entry=Entry(Detail_entry,textvariable=thalach,width=20,font="arial 12",bg="white",fg="black",bd=0)
oldpeak_entry=Entry(Detail_entry,textvariable=oldpeak,width=20,font="arial 12",bg="white",fg="black",bd=0)
trestbps_entry.place(x=100,y=290)
chol_entry.place(x=100,y=330)
thalach_entry.place(x=100,y=370)
oldpeak_entry.place(x=100,y=410)

#Report
square_report_image = PhotoImage(file="D:/Project/Python AI Projects/My Heart Pal/My Heart Pal Report window.png")
# Create a Label widget to contain the image
report_background = Label(root, image=square_report_image, bg=background,width=535,height=500)
report_background.place(x=800, y=340)
report=Label(root,font="arial 25 bold",bg="white",fg="black",text="Hi")
report.place(x=820,y=460)
report1=Label(root,font="arial 12 bold",bg="white",fg="black",text="hello")
report1.place(x=820,y=540)



root.mainloop()