from tkinter import *
import time
counter = 0

class App(Frame):
    def __init__(self,master=None):
        Frame.__init__(self, master)
        y_start = 80
        y_diff = 30
        counter = 0
        self.master = master
        self.label = Label(text="", fg="Red", font=("Helvetica", 18))
        self.label.place(x=50,y=y_start)
        self.label1 = Label(text="label1", fg="Red", font=("Helvetica", 18))
        self.label1.place(x=50,y= y_start +y_diff)
        self.label2 = Label(text="label2", fg="Red", font=("Helvetica", 18))
        self.label2.place(x=50, y= y_start + 2 * y_diff)
        self.label3 = Label(text="label3", fg="Red", font=("Helvetica", 18))
        self.label3.place(x=50, y= y_start + 3 * y_diff)
        self.label4 = Label(text="label4", fg="Red", font=("Helvetica", 18))
        self.label4.place(x=50, y= y_start + 4 * y_diff)
        self.label5 = Label(text="label5", fg="Red", font=("Helvetica", 18))
        self.label5.place(x=50, y= y_start + 5 * y_diff)
        self.label6 = Label(text="label6", fg="Red", font=("Helvetica", 18))
        self.label6.place(x=50, y= y_start + 6 * y_diff)
        self.update_clock()

    def update_clock(self):
        global counter
        intervall = 10
        counter +=1
        now = time.strftime("%H:%M:%S")

        self.label.configure(text=now)
        if counter == intervall:
            self.label1.configure(bg='red')
            print(now)
        if counter == 2* intervall:
            self.label2.configure(bg='red')
        if counter == 3 * intervall:
            self.label3.configure(bg='red')
        if counter == 4 *intervall:
            self.label4.configure(bg='red')

        if counter == 5 * intervall:
            self.label5.configure(bg='red')
        if counter == 6 * intervall:
            self.label6.configure(bg='red')
            print(now)


        self.after(1000, self.update_clock)

root = Tk()
app=App(root)

root.wm_title("digital assistant clock")
root.geometry("800x800")
root.after(1000, app.update_clock)
root.mainloop()