import tkinter as tk

# Klassendefinition
class fenster:

    def __init__(self):
        self.fenster = tk.Tk()
        # definiere leeren Label
        self.label = tk.Label(master=self.fenster, \
                              text=" ")
        # definiere Knopf, klicken ruft self.grusse auf
        self.button = tk.Button(master=self.fenster, \
                                text="Sage Hallo", \
                                command=self.gruesse)
        self.button1 = tk.Button(master=self.fenster, \
                                text="Timer", \
                                command=self.Timerwindow)

        # packen
        self.label.pack()
        self.button.pack()
        self.button1.pack()
        # anzeigen
        self.fenster.mainloop()

    def gruesse(self):
        # andere den Label Text
        self.label.config(text="Hallo!")

    def Timerwindow(self):
        self.timerW = tk.Toplevel()
        # definiere leeren Label
        self.label = tk.Label(master=self.timerW, \
                              text=" neues Fenster für Timer ")
        # definiere Knopf, klicken ruft self.grusse auf
        self.button2 = tk.Button(master=self.timerW, \
                                text="Hier ist der Timer", \
                                command=self.gruesse)
        self.button2.pack()
        




# Hauptprogramm
if __name__ == '__main__':
    # erzeuge ein Fenster Objekt
    anwendung = fenster()