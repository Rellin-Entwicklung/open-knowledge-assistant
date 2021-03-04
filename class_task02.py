import tkinter as tk
import xml.etree.ElementTree as ET
import os

print (os.path.abspath("doku-files"))
tree = ET.parse('task02.xml')
xml_root = tree.getroot()

class main():
    counter = 0
    tree = ET.parse('task02.xml')
    xml_root = tree.getroot()

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1200x800")
        self.label_step = tk.Label(self.root, text = "test", width = 120, height =30)
        self.label_step.place( x =50, y= 50)
        self.label_step = tk.Label(self.root, text="test", width=120, height=30)
        self.label_step.place(x=50, y=50)
        self.label_step = tk.Label(self.root, text="test", width=120, height=30)
        self.label_step.place(x=50, y=50)
        self.label_pic = tk.Label(self.root, image=, width=120, height=30)
        self.label_step.place(x=50, y=50)
        tk.Button(self.root, text="fwd", command=self.step_fwd).pack()
        tk.Button(self.root, text="bwd", command=self.step_bwd).pack()
        self.root.mainloop()


    def xml_read(self,Pos):

        srch_item = "step_item" + str(Pos)
        print("such_inhalt", srch_item)
        print("xml-root ",xml_root)
        for elem in xml_root.iter(srch_item):
            suchstring = str(elem.text.strip())
            print("suchen", suchstring)

    def step_fwd(self):
        main.counter += 1
        print("fwd ", main.counter)
        self.Wert= self.xml_read(main.counter)



    def step_bwd(self):
        main.counter -= 1
        print("bwd ", self.counter)



if __name__ == '__main__':
    main()


