from tkinter import *
import imutils
import cv2
import numpy as np
import os
import time

from PIL import Image
from PIL import ImageTk



root = Tk()
cap = cv2.VideoCapture(0)
time.sleep(1)
    # Capture frame-by-frame
ret, frame = cap.read()
time.sleep(1)
ret, frame = cap.read()



frame = imutils.resize(frame, width=300)

                # OpenCV represents images in BGR order; however PIL
                # represents images in RGB order, so we need to swap
                # the channels, then convert to PIL and ImageTk format
image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

image = Image.fromarray(image)
image = ImageTk.PhotoImage(image)




logo = (image)
w1 = Label(root, image=logo).pack(side="right")
explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface 
exists to allow additional image file
formats to be added easily."""
w2 = Label(root,
           justify=LEFT,
           padx = 10,
           text=explanation).pack(side="left")

root.mainloop()