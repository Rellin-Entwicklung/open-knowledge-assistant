import tkinter as tk
from itertools import cycle
import time
import imutils
import cv2
from PIL import Image
from PIL import ImageTk


class PhotoWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.bilder = [
            tk.PhotoImage(file="Bild.gif"),
            tk.PhotoImage(file="Bild2.gif")
        ]
        self.bilder_karusell = cycle(self.bilder)
        self.image_label = tk.Label(self)
        self.image_label["image"] = next(self.bilder_karusell)
        self.image_label.pack()


        self.cap = cv2.VideoCapture(0)
        time.sleep(1)
        # Capture frame-by-frame
        self.ret, self.frame = self.cap.read()

        time.sleep(1)
        #cv2.imshow("test", self.frame)
        tk.Button(self, text="save pic", command=self.bild_holen).pack()
        tk.Button(self, text="quit", command=self.destroy).pack()
        self.bild_holen()


    def savePic





    def bild_holen(self):


        self.ret, self.frame = self.cap.read()
        #cv2.imshow("test",self.frame)
        self.frame = imutils.resize(self.frame, width=300)

        # OpenCV represents images in BGR order; however PIL
        # represents images in RGB order, so we need to swap
        # the channels, then convert to PIL and ImageTk format
        self.image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)

        self.image = Image.fromarray(self.image)
        self.image = ImageTk.PhotoImage(self.image)

        self.image_label["image"] = self.image
        self.image_label.after(1000,self.bild_holen)



def main():
    root = PhotoWindow()
    root.mainloop()


if __name__ == "__main__":
    main()