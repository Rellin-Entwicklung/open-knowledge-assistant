import tkinter as tk
import imutils
import cv2
import numpy as np
import os
import time

from PIL import Image
from PIL import ImageTk


class TaskWindow(tk.Tk):
    def __init__(self):
        #tk.Tk.__init__(self)
        #self.cancel_id = None
        self.step_label = tk.Label(root, text="test")
        self.step_label.pack()
        tk.Button(self, text="fwd", command=self.step_fwd()).pack()
        tk.Button(self, text="bwd", command=self.step_fwd()).pack()

       

    def step_fwd(self):
         print("fwd")


    def step_bwd(selfelf):
         print("bwd")



def main():
    root = TaskWindow()
    root.mainloop

if __name__ == '__main__':
    main()