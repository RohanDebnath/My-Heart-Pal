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
Label(Heading_entry, text="Date:", font="Arial 13", bg="#FDD0D3", fg="black").place(x=450, y=20)
Label(Heading_entry, text="Patient Name:", font="Arial 13", bg="#FDD0D3", fg="black").place(x=10, y=100)
Label(Heading_entry, text="Date of Birth:", font="Arial 13", bg="#FDD0D3", fg="black").place(x=450, y=100)

Label(Heading_entry, font="Arial 13", bg="white",width=30, fg="black").place(x=150, y=20)
Label(Heading_entry, font="Arial 13", bg="white",width=30, fg="black").place(x=550, y=20)
Label(Heading_entry, font="Arial 13", bg="white",width=30, fg="black").place(x=150, y=100)
Label(Heading_entry, font="Arial 13", bg="white",width=30, fg="black").place(x=550, y=100)


root.mainloop()
