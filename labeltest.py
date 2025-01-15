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
from pyzbar import pyzbar
from PIL import Image
from PIL import ImageTk
import os


root = Tk()

# Create a photoimage object of the image in the path
image1 = Image.open("Bild.gif")
test = ImageTk.PhotoImage(image1)

label1 = Label(root, image=test)
label1.image = test

# Position image
label1.place(x=30, y=30)
root.mainloop()