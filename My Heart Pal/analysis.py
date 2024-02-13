from tkinter import *
import datetime
from datetime import date
from tkinter.ttk import Combobox
import tkinter as tk 
from tkinter import ttk 
import os 
from tkinter import messagebox
import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

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
# root.resizable(False,False)
root.config(bg=background)

#analysis

def analysisOfHeart():
    name=Name.get()
    D1=Date.get()
    today=datetime.date.today()
    A=today.year-DOB.get()

    try:
        B=selection()
    except:
        messagebox.showerror("Missing", "please select Gender!!")
        return

    try:
        F=selection2()
    except:
        messagebox.showerror("Missing", "please select fbs!!")
        return

    try:
        I=selection3()
    except:
        messagebox.showerror("Missing", "please select exang!!")
        return

    try:
        C=int(selection4())
    except:
        messagebox.showerror("Missing", "please select cp!!")
        return
 
    try:
        K=int(selection5())
    except: 
        messagebox.showerror("Missing", "please select slope!!")
        return
    try:
        G=int(restecg_combobox.get())
    except: 
        messagebox.showerror("Missing", "please select resteg!!")
        return 
    try:
        L=int(ca_combobox.get())
    except: 
        messagebox.showerror("Missing", "please select ca!!")
        return   
    try:
        M=int(thal_combobox.get())
    except: 
        messagebox.showerror("Missing", "please select thal!!")
        return
    try:
        D=int(trestbps.get())
        E=int(chol.get())
        H=int(thalach.get())
        J=int(oldpeak.get())
    except:
        messagebox.showerror("Missing data","Few Data are missing")
        return

    # First Graph
    f = Figure(figsize=(5, 5), dpi=100)
    a = f.add_subplot(111)
    a.plot(["Sex", "fbs", "exang"], [B, F, I])
    # Create a FigureCanvasTkAgg object
    canvas = FigureCanvasTkAgg(f, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
    canvas.get_tk_widget().place(width=158, height=165, x=600, y=340)


    # Second Graph
    f2 = Figure(figsize=(5, 5), dpi=100)
    a2 = f2.add_subplot(111)
    a2.plot(["age ", "tresbps ", "chol ","thalach   "], [A, D, E, H])
    # Create a FigureCanvasTkAgg object
    canvas2 = FigureCanvasTkAgg(f2, master=root)
    canvas2.draw()
    canvas2.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
    canvas2.get_tk_widget().place(width=158, height=165, x=800, y=340)


#Opening info window by button 
def Info():
    Icon_window=Toplevel(root)
    Icon_window.title("Info")
    Icon_window.geometry("700x600+400+100")

    #Icon Setting
    icon_Image=PhotoImage(file="D:\Project\Python AI Projects\My Heart Pal\info-icon.png")
    Icon_window.iconphoto(False,icon_Image)

    #Heading
    Label(Icon_window,text="Information Related to Dataset",font="robot 17 bold").pack(padx=20,pady=20)

    #info
    Label(Icon_window,text="age - age in years",font="arial 11").place(x=20,y=100)
    Label(Icon_window,text="sex - sex(1=male; 0=female)",font="arial 11").place(x=20,y=130)
    Label(Icon_window,text="cp - chest pain type (0 = typical angina; 1 = atypical angina; 2 = non-angial pain; 3 = asymptomatic)",font="arial 11").place(x=20,y=160)
    Label(Icon_window,text="trestbps - resting blood pressure (in mm Hg on admission to the hospital)",font="arial 11").place(x=20,y=190)
    Label(Icon_window,text="chol - serum cholestoral in mg/dl",font="arial 11").place(x=20,y=220)
    Label(Icon_window,text="fbs - fasting blood sugar > 120 mg/dl (1 = true; 0 = false)",font="arial 11").place(x=20,y=250)
    Label(Icon_window,text="restecg - resting electrocardiographic result (0 = normal; 1 = having ST-T; 2 = hypertrophy)",font="arial 11").place(x=20,y=280)
    Label(Icon_window,text="thalach - maximum heart rate achieved",font="arial 11").place(x=20,y=310)
    Label(Icon_window,text="exang - exercise include angina (1 = yes; 0 = no)",font="arial 11").place(x=20,y=340)
    Label(Icon_window,text="oldpeak - ST depression included by exercise relative to rest",font="arial 11").place(x=20,y=370)
    Label(Icon_window,text="slope - the slope of the peak exercise ST segment (0= upsloping: 1 = flat; 2 = downsloping)",font="arial 11").place(x=20,y=400)
    Label(Icon_window,text="ca - number of major vessels (0-3) colored by flourospy",font="arial 11").place(x=20,y=430)
    Label(Icon_window,text="thal - 0 - normal; 1 = fixed defect ; 2 = reversable defect",font="arial 11").place(x=20,y=460)

    Icon_window.mainloop()

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

def selection5():
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
report_background.place(x=980, y=340)
report=Label(root,font="arial 25 bold",bg="white",fg="black",text="Hi")
report.place(x=1000,y=460)
report1=Label(root,font="arial 12 bold",bg="white",fg="black",text="hello")
report1.place(x=1000,y=540)

#Graph
graph_image=PhotoImage(file="D:\Project\Python AI Projects\My Heart Pal\graph.png")
Label(image=graph_image).place(x=600,y=340)
Label(image=graph_image).place(x=800,y=340)
Label(image=graph_image).place(x=600,y=540)
Label(image=graph_image).place(x=800,y=540)

#Analysis Button
analysis_button=PhotoImage(file="D:\Project\Python AI Projects\My Heart Pal\Analysis button.png")
Button(root,image=analysis_button,bg="#FDD0D3",border=0,cursor="hand2",command=analysisOfHeart).place(x=400,y=720)

#Info Button
info_button=PhotoImage(file="D:\Project\Python AI Projects\My Heart Pal\info-icon.png")
Button(root,image=info_button,bd=0,bg=background,cursor="hand2",command=Info).place(x=1450,y=390)

#save  button
save_btn=PhotoImage(file="D:\Project\Python AI Projects\My Heart Pal\save button.png")
Button(root,image=save_btn,bg=background,bd=0,cursor="hand2").place(x=1450,y=450)

#Smoking and Non Smoking
button_mode = True
choice = "Smoking"

def changemode():
    global button_mode
    global choice
    if button_mode:
        choice = "non_Smoking"
        mode.config(image=Nonsmoking_icon, activebackground="white")
        button_mode = False
    else:
        choice = "Smoking"
        mode.config(image=smoking_icon, activebackground="white")
        button_mode = True
    
    print(choice)

Nonsmoking_icon = PhotoImage(file="D:/Project/Python AI Projects/My Heart Pal/smoker na.png")
smoking_icon = PhotoImage(file="D:/Project/Python AI Projects/My Heart Pal/smoker.png")

mode = Button(root, image=Nonsmoking_icon, bg="white", cursor="hand2", height=25, command=changemode)
mode.place(x=100, y=585)


root.mainloop()