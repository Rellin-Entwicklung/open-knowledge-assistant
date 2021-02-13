from tkinter import *
from tkinter import ttk
import datetime
import logging
import tkinter.font as tkFont
import xml.etree.ElementTree as ET
import logging
import time
import imutils
import cv2
from PIL import Image
from PIL import ImageTk


def photo_quit():
    root.destroy()


def change_pic():
    global w1
    image = cv2.imread('maske_02.PNG')
    logo = imutils.resize(image, width=300)
    # logo = imutils.resize(logo, width=300)
    # logo = PhotoImage(file='Maske_V2.PNG')
    logo = Image.fromarray(logo)
    # image = imutils.resize(image, width=300)
    image = ImageTk.PhotoImage(logo)

    w1.configure(image=logo)

root = Tk()
#cap = cv2.VideoCapture(0)
#time.sleep(1)
# Capture frame-by-frame
#ret, frame = cap.read()
# TODO Unterverzeichnis adressieren
# logo = PhotoImage(file='\doku-files\screen-test04.png')
image = cv2.imread('Maske_V2.PNG')
image = imutils.resize(image, width=300)
#logo = imutils.resize(logo, width=300)
#logo = PhotoImage(file='Maske_V2.PNG')
image = Image.fromarray(image)
#image = imutils.resize(image, width=300)
image = ImageTk.PhotoImage(image)

w1 = Label(root, image = image).pack(side="right")
explanation = """The open konwledge assistant takes pictures to document situations. 
           If there is any text in the picture, the open knowledge assistent will find and recognize it
           and save it in a separate file"""
#w1.after(2000,change_pic)
print("type", type(w1))
w2 = Label(root,
           justify=LEFT,
           padx=10,
           text=explanation).pack(side="left")

btn_close = Button(root, text='click to quit', command=photo_quit)
btn_close.pack()
time.sleep(3)
w1.configure(image=image)





root.mainloop()
