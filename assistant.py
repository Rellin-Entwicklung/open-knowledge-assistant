from tkinter import *
from tkinter import ttk
import datetime
import logging
import tkinter.font as tkFont
import xml.etree.ElementTree as ET
import logging

ctr = 0

class param:
    status = {
        "project": "",
        "inverter": "",
        "user": "Alex",
        "date/time": "",
        "Inp_BLOCK": "not used",
        "Inp_RUN": "not used",
        "Inp_UP": "not used",
        "Inp_DOWN": "not used",
        "RATED SPEED": "50 hz",
        "JOG Speed": "15 hz",
        "CRAWL Speed": "2 hz",
        "SPEED 4": "not used",
        "SPEED 5": "not used",
        "SPEED 6": "not used",
        "SPEED 7": "not used",
        "Input_01": "MPI_01",
        "Input_02": "MPI_02",
        "Input_03": "MPI_03",
        "Input_04": "MPI_04",
        "Input_05": "MPI_05",
        "acel_time": "1.5",
        "decel__time": "1.5",
        "braking_frequ": "2.5",
        "braking_time": "2.5",
        "motor_rated_speed": "1400",
        "motor_rated_torque": "7.5",
        "motor_rated_voltage": "3 * 400 V",
        "motor_rated_current": " 27 A",

    }


param.status["project"] = "Test Assistant"
param.status["user"] = "Alex"
param.status["inverter"] = "Yaskawa G7"
param.status["date/time"] = "2021-01-22"
print("klasse param-status ", param.status)
print("einzelene Werte: ", param.status["project"])
#fontStyle = tkFont.Font(family="Lucida Grande", size=20)
#fontStyle_1 = tkFont.Font(family="Lucida Grande", size=12)





logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')



def irgendwas():
    print("irgendwas")

def Wizard():
    global ctr

    def next():

        global weiter
        global ctr
        ctr = ctr + 1
        print("next aufgerufen ", ctr)
        info = "Step-No.:   " + str(ctr)
        StepNr = Label(master=para, text=info, font =fs02)
        StepNr.place(x=0, y=160, width=800, height=20)
        weiter = True
        # info = param.status[params[ctr]]
        ## TODO: eher brutale Methode, über config lösen !
        # Label(para, text=info).place(x=200, y=250, width=200, height=50)

        info = params[ctr]
        Action = Label(master=para, text=info, font =fs02)
        Action.place(x=0, y=220, width=800, height=20)
        info = params1[ctr]
        Label(para, text=info, font =fs02).place(x=0, y=260, width=800, height=20)

    tree = ET.parse('task01.xml')
    xml_root = tree.getroot()
    ActionList = []
    for action in xml_root.iter('comm_item'):
        ActionList.append(str(action.text.strip()))
    print("actions in List", ActionList)
    # das ist jetzt nur zum Testen, Werte kommen eigentlich aus der xml - Liste
    params = ["Please Check: red Cable in connector 1",
              "Please Check: blue Cable in connector 2",
              "Please Check: green Cable in connector 3",
              "Please Check: gray Cable in connector 4",
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

    params1 = ["Connection 1  o.k. ?",
               "Connection 2  o.k. ?",
               "Connection 3  o.k. ?",
               "Connection 4  o.k. ?",
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


    weiter = False
    ctr = 0
    print("commisioning wizard aufgerufen")
    para = Tk()
    para.title('open knowledge assistant')
    para.geometry('800x500')
    # Seitenüberschrift
    fs01="Helvetica 16 bold italic"
    fs02 ="Helvetica 12 italic"
    ScreenTitle = Label(master=para,
                        text='Task Assistant',font=fs01)
    ScreenTitle.place(x=0, y=110, width=800, height=50)

    info = "project:  " + param.status["project"]
    ProjectTitle = Label(master=para, text=info , anchor=W, justify=LEFT)
    ProjectTitle.place(x=10, y=20, width=800, height=20)
    info = "user:  " + param.status["user"]
    ProjectUser = Label(master=para, text=info,  anchor=W, justify=LEFT)
    ProjectUser.place(x=10, y=40, width=800, height=20)
    info = "date:  " + param.status["date/time"]
    ProjectDate = Label(master=para, text=info, anchor=W, justify=LEFT)
    ProjectDate.place(x=600, y=20, width=800, height=20)

    # TODO: ueberlegen, wie man das mit Schleifen (iterativ) hinbekommen könnte

    # for aktuell in params:
    # print("param.status "," ",aktuell,  param.status[aktuell])

    ButtonNoOK = Button(master=para, text='NOT OK', bg= 'red' , command=irgendwas)
    ButtonNoOK.place(x=220, y=320, width=150, height=60)

    ButtonNext = Button(master=para, text='Function OK', bg ='green', command=next)
    ButtonNext.place(x=420, y=320, width=150, height=60)

    ButtonPhoto = Button(master=para, text='Add Photo', command=irgendwas)
    ButtonPhoto.place(x=630, y=320, width=150, height=60)

    ButtonComment = Button(master=para, text=' Add Comment', command=irgendwas)
    ButtonComment.place(x=20, y=320, width=150, height=60)

    weiter = True



    # eintragen in Datenbank oder xml - file ergänzen

    para.mainloop()


Wizard()