# -*- coding: iso-8859-1 -*-
import os
import tkinter as tk
from tkinter import messagebox

APP_TITLE = "Hauptfenster"
APP_XPOS = 100
APP_YPOS = 100
APP_WIDTH = 300
APP_HEIGHT = 200


class MeineAnwendung(object):

    def __init__(self, hauptfenster):
        self.hauptfenster = hauptfenster
        self.menu(hauptfenster)

        self.entry_01 = tk.StringVar()
        self.entry_02 = tk.StringVar()

        self.enbbeded_frame = self.create_embbeded_frame(hauptfenster)
        # self.hide_embbeded_frame()
        self.show_embedded_frame()

        self.create_picture(hauptfenster)

    def menu(self, hauptfenster):
        menubar = tk.Menu(hauptfenster, bg='gray70')  # bg="#000000")

        # Erstelle das Skripte
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(
            label="Programm 1", command=self.show_embedded_frame)
        filemenu.add_separator()
        filemenu.add_command(
            label="Exit", command=hauptfenster.quit)
        menubar.add_cascade(
            label="Skripte", menu=filemenu)

        # Erstelle das Help
        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_separator()
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About...", command=self.show_version_info)
        menubar.add_cascade(label="Help", menu=helpmenu)

        hauptfenster.config(menu=menubar)

    def create_embbeded_frame(self, hauptfenster):
        # frame = tk.Frame(hauptfenster)
        frame = tk.Frame(hauptfenster, bg='green', padx=10, pady=10)
        frame.grid(row=0, column=0, padx=10, pady=10)

        tk.Entry(frame, textvariable=self.entry_01).grid(row=0, column=1)
        tk.Entry(frame, textvariable=self.entry_02).grid(row=1, column=1)

        tk.Label(frame, text="Eingabe1").grid(row=0)
        tk.Label(frame, text="Eingabe2").grid(row=1)

        tk.Label(frame, text="Standard", bg="#ffffbb", pady=10
                 ).grid(row=3, columnspan=2, sticky='we')

        tk.Button(frame, text="Schliessen", command=self.hide_embbeded_frame
                  ).grid(row=4, columnspan=2)
        return frame

    def create_picture(self, hauptfenster):
        #self.logo = tk.PhotoImage(file="C:/E/scripts/E_scripts/media/Loading.gif")
        self.logo = tk.PhotoImage(file="Bild.GIF")
        # self.logo = tk.PhotoImage(file="Loading.gif")
        # tk.Label(hauptfenster, image=self.logo).grid(row=2,column=0)
        tk.Label(hauptfenster, image=self.logo, bg='yellow',
                 ).grid(row=2, column=0, pady=10, ipadx=10, ipady=10)

    def show_embedded_frame(self):
        self.enbbeded_frame.grid()

    def hide_embbeded_frame(self):
        self.enbbeded_frame.grid_remove()

    def show_version_info(self):
        message = "************************\n"
        message += "Version: 1.00\n"
        message += "************************"
        messagebox.showinfo("info", message)


def main():
    hauptfenster = tk.Tk()
    hauptfenster.title(APP_TITLE)
    # hauptfenster.geometry("+{}+{}".format(APP_XPOS, APP_YPOS))
    # hauptfenster.geometry("{}x{}".format(APP_WIDTH, APP_HEIGHT))
    hauptfenster.config(bg='steelblue')
    app = MeineAnwendung(hauptfenster)

    hauptfenster.mainloop()


if __name__ == '__main__':
    main() # -*- coding: iso-8859-1 -*-
import os
import tkinter as tk
from tkinter import messagebox

APP_TITLE = "Hauptfenster"
APP_XPOS = 100
APP_YPOS = 100
APP_WIDTH = 300
APP_HEIGHT = 200

