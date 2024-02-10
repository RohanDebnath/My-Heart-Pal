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


root.mainloop()
