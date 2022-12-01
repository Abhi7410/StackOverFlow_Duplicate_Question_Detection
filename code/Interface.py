# Libraries
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import tkinter.scrolledtext as scrolledtext
import PIL
import time


rootWindow = tk.Tk()
rootWindow.title('StackOverFlow Duplicate Question Detector')
rootWindow.resizable(True, True)
rootWindow.geometry('1920x1080')

my_frame = Frame(rootWindow, width=576, height=324, bg='black')
my_frame.pack(fill="both", expand=True)

imgaddress = PIL.Image.open(
    "/home/abhishek/Desktop/3-1/smai/StackOverFlow_Duplicate_Question_Detection/images/bg7.jpg")
img = ImageTk.PhotoImage(imgaddress)
label = Label(
    my_frame,
    image=img
)
label.place(x=0, y=0)

# global &/ initialisations
title, body, tag = "Title", "Body", "Tag" 
titles = ["one", "two", "three"]
kval = 5

#######################

# changing the title and retrieving the title
def onChangeTitle(tite): 
    global title, titles
    title = tite.widget.get()
    print("Title Entered:", title)

# changing the body and retrieving the body
def onChangeBody(bode):  
    global body
    body = bode.widget.get()
    print("Body Entered:", body)

# changing the tag and retrieving the tag
def onChangetags(tags): 
    global tag
    tag = tags.widget.get()
    print("Tags Entered:", tag)

# changing the k value and retrieving the k value
def onChangek(k): 
    global kval
    kval = int(k.widget.get())
    print("K-value Entered:", kval)

# show (top-k questions) results in output section 
def showResults():
    global title, body, tag
    fs = TopKQuestions(title, body, tag, kval)
    txt.delete('1.0', END)
    txt.insert('insert', fs, "\n")


#=============Title Box =============#
L2 = Label(rootWindow, text="Enter the Title:", fg='black', bg='white')
L2.pack(side=LEFT)
L2.place(x=70, y=55)
EntryTitle = Entry(rootWindow, bd=2, textvariable=title)
EntryTitle.pack()
EntryTitle.place(x=200, y=50, width=1200, height=35)
EntryTitle.bind("<Return>", onChangeTitle)

#=============Body Box =============#
L3 = Label(rootWindow, text="Enter the Body:", fg='black', bg='white')
L3.pack(side=LEFT)
L3.place(x=70, y=110)
EntryBody = Entry(rootWindow, bd=2, textvariable=body)
EntryBody.pack()
EntryBody.place(x=200, y=105, width=1200, height=35)
EntryBody.bind("<Return>", onChangeBody)

# =============Tags Box =============#
L4 = Label(rootWindow, text="Enter the Tags:", fg='black', bg='white')
L4.pack(side=LEFT)
L4.place(x=70, y=165)
EntryTags = Entry(rootWindow, bd=2, textvariable=tag)
EntryTags.pack()
EntryTags.place(x=200, y=160, width=1200, height=35)
EntryTags.bind("<Return>", onChangetags)

# =============K-value Box =============#
L5 = Label(rootWindow, text="Enter k-value:", fg='black', bg='white')
L5.pack(side=LEFT)
L5.place(x=70, y=220)
ke = Entry(rootWindow, bd=2, textvariable=kval)
ke.pack()
ke.place(x=200, y=215, width=100, height=35)
ke.bind("<Return>", onChangek)

# ================submit button=================#
submitButton = Button(rootWindow, bg='black', fg='white', text='Submit', command=showResults)
submitButton.pack(expand=True)
submitButton.place(x=950, y=245)

txt = scrolledtext.ScrolledText(rootWindow, undo=True, wrap='word', width=150, height=20)
txt['font'] = ('consolas', '12')
txt.pack(expand=True, fill='both')
txt.place(x=200, y=290)

rootWindow.mainloop()
