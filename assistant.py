from tkinter import *
from tkinter import ttk
import datetime
import logging
import tkinter.font as tkFont
import xml.etree.ElementTree as ET
import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')



def Wizard():
    global ctr

    def next():

        global weiter
        global ctr
        ctr = ctr + 1
        print("next aufgerufen ", ctr)
        info = "Step-No.:   " + str(ctr)
        StepNr = Label(master=para, text=info, font=fontStyle_1)
        StepNr.place(x=0, y=160, width=800, height=20)
        weiter = True
        # info = param.status[params[ctr]]
        ## TODO: eher brutale Methode, über config lösen !
        # Label(para, text=info).place(x=200, y=250, width=200, height=50)

        info = params[ctr]
        Action = Label(master=para, text=info, font=fontStyle_1)
        Action.place(x=300, y=220, width=250, height=20)
        info = params1[ctr]
        Label(para, text=info).place(x=300, y=260, width=200, height=20)

    tree = ET.parse('commissioinng.xml')
    xml_root = tree.getroot()
    ActionList = []
    for action in xml_root.iter('comm_item'):
        ActionList.append(str(action.text.strip()))
    print(ActionList)

    params = ["Please start inspection drive up",
              "Please start inspection drive down",
              "up",
              "down",
              "rated speed",
              "jog",
              "crawl",
              "speed 4",
              "speed 5",
              "speed 6",
              "speed 7",
              "input_01",
              "input_02",
              "input_03",
              "input_04",
              "input_05"]

    params1 = ["Richtung (UP)  o.k ? speed o.k. ?",
               "Richtung (DOWN) o.k ? speed o.k. ?",
               "up",
               "down",
               "rated speed",
               "jog",
               "crawl",
               "speed 4",
               "speed 5",
               "speed 6",
               "speed 7",
               "input_01",
               "input_02",
               "input_03",
               "input_04",
               "input_05"]

    #fontStyle = tkFont.Font(family="Lucida Grande", size=20)
    #fontStyle_1 = tkFont.Font(family="Lucida Grande", size=12)
    weiter = False
    ctr = 0
    print("commisioning wizard aufgerufen")
    para = Toplevel()
    para.title('comissioning wizard')
    para.geometry('800x500')
    # Seitenüberschrift
    ScreenTitle = Label(master=para,
                        text='Commisioning Wizard')
    ScreenTitle.place(x=0, y=110, width=800, height=50)

    #info = "project:  " + param.status["project"]
    ProjectTitle = Label(master=para, text=info, font=fontStyle_1, anchor=W, justify=LEFT)
    ProjectTitle.place(x=10, y=20, width=800, height=20)
    info = "user:  " + param.status["user"]
    ProjectUser = Label(master=para, text=info, font=fontStyle_1, anchor=W, justify=LEFT)
    ProjectUser.place(x=10, y=40, width=800, height=20)
    info = "date:  " + param.status["date/time"]
    ProjectDate = Label(master=para, text=info, font=fontStyle_1, anchor=W, justify=LEFT)
    ProjectDate.place(x=600, y=20, width=800, height=20)

    # TODO: ueberlegen, wie man das mit Schleifen (iterativ) hinbekommen könnte

    # for aktuell in params:
    # print("param.status "," ",aktuell,  param.status[aktuell])

    ButtonNoOK = Button(master=para, text='NOT OK', command=irgendwas)
    ButtonNoOK.place(x=200, y=320, width=150, height=20)

    ButtonNext = Button(master=para, text='Function OK', command=next)
    ButtonNext.place(x=400, y=320, width=150, height=20)
    weiter = True
    for aktuell in params:
        if weiter == True:
            print("param.status ", " ", aktuell, param.status[aktuell])

            weiter = False

    # eintragen in Datenbank

    para.mainloop()


Wizard()