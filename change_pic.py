import tkinter as tk
from itertools import cycle


class MainWindow(tk.Tk):

    def grab_pic(self):
        print("Bild holen")
        self.bild_wechsel()



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
        self.image_label.after(1000, self.grab_pic)




        tk.Button(self, text="o.k.", command=self.destroy).pack()



    def bild_wechsel(self):
        self.image_label["image"] = next(self.bilder_karusell)
        self.image_label.after(1000, self.grab_pic)


def main():
    root = MainWindow()
    root.mainloop()


if __name__ == "__main__":
    main()