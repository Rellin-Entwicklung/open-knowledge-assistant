from tkinter import *
from tkinter import ttk
import datetime
import logging
import tkinter.font as tkFont
import xml.etree.ElementTree as ET
import logging
import time
import imutils
import cv2
from pyzbar import pyzbar
from PIL import Image
from PIL import ImageTk



ctr = 0
counter = 0
zeit = (" ")
timerActive = False

weiter = False
ctr = 0
print(" wizard aufgerufen")
para = Tk()
para.title('open knowledge assistant')
para.geometry('1024x600')
# Seitenüberschrift
fs01 = "Helvetica 16 bold italic"
fs02 = "Helvetica 12 italic"
root = Tk()

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

def getBarcode():
    def Barcode_quit():
        root.destroy()

    def Barcode_save():
        print("save pic")
        Barcode_quit()
    def draw_barcode(decoded, image):
        # n_points = len(decoded.polygon)
        # for i in range(n_points):
        #     image = cv2.line(image, decoded.polygon[i], decoded.polygon[(i+1) % n_points], color=(0, 255, 0), thickness=5)
        image = cv2.rectangle(image, (decoded.rect.left, decoded.rect.top),
                              (decoded.rect.left + decoded.rect.width, decoded.rect.top + decoded.rect.height),
                              color=(0, 255, 0),
                              thickness=5)
        return image

    def decode(image):
        status = False
        # decodes all barcodes from an image
        decoded_objects = pyzbar.decode(image)
        for obj in decoded_objects:
            # draw the barcode
            image = draw_barcode(obj, image)
            # print barcode type & data
            status = True
            print("Type:", obj.type)
            w1.config(text = obj.type)
            print("Data:", obj.data)
            w2.config(text = obj.data)
            Success.config(text = 'Success')
            print()

        return image,status

    cap = cv2.VideoCapture(0)
    def getQR():
        # read the frame from the camera
        _, frame = cap.read()
        # decode detected barcodes & get the image
        # that is drawn
        frame,status = decode(frame)
        # show the image in the window
        cv2.imshow("ocr erkannt wenn grüner Rand", frame)
        print(status)
        if status == True:
            # TODO an dieser Stelle Sound einfügen
            print("Erfolg")
        #else:
            #time.sleep(1)
            #getQR()

    root = Toplevel()
    root.title('your assistents gets ocr / barcode')
    root.geometry('600x400')
    btn_close = Button(root, text='click to quit', command=Barcode_quit)
    btn_close.pack()
    btn_save = Button(root, text=' save content', command=Barcode_save)
    btn_save.pack()
    btn_save = Button(root, text=' new pic' ,command=getQR)
    btn_save.pack()
    Success= Label(root, text = 'no ocr /barcode found')
    Success.pack()
    w1 = Label(root,text='noch leer')
    w1.pack()
    w2 = Label(root,text='noch leer')
    w2.pack()

    getQR()

    root.mainloop


def photofunction():
    def photo_quit():
        root.destroy()

    def photo_save():
        print("save pic")
        photo_quit()
    root = Toplevel()
    cap = cv2.VideoCapture(0)
    def grab_frame():
        time.sleep(1)
        # Capture frame-by-frame
        ret, frame = cap.read()

        frame = imutils.resize(frame, width=300)

        # OpenCV represents images in BGR order; however PIL
        # represents images in RGB order, so we need to swap
        # the channels, then convert to PIL and ImageTk format
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        image = Image.fromarray(image)
        #image = ImageTk.PhotoImage(image)
        return image

    
    logo = ImageTk.PhotoImage(grab_frame())

    image_label = Label(root)
    image_label.config(image= logo)
    image_label.pack(side="right")
    #w1 = Label(root, image=logo).pack(side="right")
    explanation = """The open konwledge assistant takes pictures to document situations. 
    If there is any text in the picture, the open knowledge assistent will find and recognize it
    and save it in a separate file"""
    w2 = Label(root,
               justify=LEFT,
               padx=10,
               text=explanation).pack(side="left")
    btn_close = Button(root, text = 'click to quit', command = photo_quit)
    btn_close.pack()
    btn_save = Button(root, text=' save pic', command=photo_save)
    btn_save.pack()


    root.mainloop()


def timer_App():
    global timerActive,root
    def init():

        y_start = 80
        y_diff = 30
        counter = 0
        root = Toplevel()
        winTimer = root
        label = Label( root, text="", fg="Red", font=("Helvetica", 18))
        label.place(x=50,y=y_start)
        label1 = Label(root, text="label1", fg="Red", font=("Helvetica", 18))
        label1.place(x=50,y= y_start +y_diff)
        label2 = Label(text="label2", fg="Red", font=("Helvetica", 18))
        label2.place(x=50, y= y_start + 2 * y_diff)
        label3 = Label(text="label3", fg="Red", font=("Helvetica", 18))
        label3.place(x=50, y= y_start + 3 * y_diff)
        label4 = Label(text="label4", fg="Red", font=("Helvetica", 18))
        label4.place(x=50, y= y_start + 4 * y_diff)
        label5 = Label(text="label5", fg="Red", font=("Helvetica", 18))
        label5.place(x=50, y= y_start + 5 * y_diff)
        label6 = Label(text="label6", fg="Red", font=("Helvetica", 18))
        label6.place(x=50, y= y_start + 6 * y_diff)
        timerActive = True
        intervall = 10
        counter +=1
        now = time.strftime("%H:%M:%S")

        label.configure(text=now)
        if counter == intervall:
            label1.configure(bg='red')
            print(now)
        if counter == 2* intervall:
            label2.configure(bg='red')
        if counter == 3 * intervall:
            label3.configure(bg='red')
        if counter == 4 *intervall:
            label4.configure(bg='red')

        if counter == 5 * intervall:
            label5.configure(bg='red')
        if counter == 6 * intervall:
            label6.configure(bg='red')
            print(now)

    init()
    root.mainloop()







ScreenTitle = Label(master=para,
                    text='Task Assistant', font=fs01)
ScreenTitle.place(x=0, y=110, width=800, height=50)

info = "project:  " + param.status["project"]
ProjectTitle = Label(master=para, text=info, anchor=W, justify=LEFT, font = fs02)
ProjectTitle.place(x=10, y=20, width=800, height=20)
info = "user:  " + param.status["user"]
ProjectUser = Label(master=para, text=info, anchor=W, justify=LEFT, font = fs02)
ProjectUser.place(x=10, y=40, width=800, height=20)
info = "date:  " + param.status["date/time"]
ProjectDate = Label(master=para, text=info, anchor=W, justify=LEFT, font = fs02)
ProjectDate.place(x=650, y=20, width=800, height=20)

clockDisp = Label(master=para ,text = zeit, anchor=W, justify=LEFT, font = fs01)
clockDisp.place(x=650, y=430, width=200, height=20)

ButtonNoOK = Button(master=para, text='NOT OK', bg='red', command=timer_App)
ButtonNoOK.place(x=220, y=320, width=150, height=60)



ButtonPhoto = Button(master=para, text='Add Photo', command=photofunction)
ButtonPhoto.place(x=630, y=320, width=150, height=60)

ButtonComment = Button(master=para, text=' Add Comment', command=irgendwas)
ButtonComment.place(x=20, y=320, width=150, height=60)
y_line2 = 400

ButtonTimer = Button(master=para, text=' Timer ', command=irgendwas)
ButtonTimer.place(x=20, y=y_line2, width=150, height=60)

ButtonFunc1 = Button(master=para, text='get barcode', command=getBarcode)
ButtonFunc1.place(x=220, y=y_line2, width=150, height=60)

ButtonFunc2 = Button(master=para, text=' function 2', command=irgendwas)
ButtonFunc2.place(x=420, y=y_line2, width=150, height=60)

y_line2 = 480

ButtonFunc3 = Button(master=para, text=' function 3 ', command=irgendwas)
ButtonFunc3.place(x=20, y=y_line2, width=150, height=60)

ButtonFunc4 = Button(master=para, text=' function 4', command=irgendwas)
ButtonFunc4.place(x=220, y=y_line2, width=150, height=60)

ButtonFunc5 = Button(master=para, text=' function 5', command=irgendwas)
ButtonFunc5.place(x=420, y=y_line2, width=150, height=60)






date =""



def clockPuls():
    global date
    global zeit
    if timerActive == FALSE:
        print("clock aufgerufen", zeit)

        neuezeit = time.strftime('%H:%M:%S')

        newdate = time. strftime("%d.%m.%Y")


        if newdate != date:
            date = newdate
            ProjectDate.config(text=date)

        if neuezeit != zeit:
            zeit = neuezeit
            clockDisp.config(text=zeit)
        clockDisp.after(500, clockPuls)




def next():

    global weiter
    global ctr
    ctr = ctr + 1
    print("next aufgerufen ", ctr)
    info = "Step-No.:   " + str(ctr) +"  from: " + str(max)
    StepNr = Label(master=para, text=info, font =fs02)
    StepNr.place(x=0, y=160, width=800, height=20)
    weiter = True
        # info = param.status[params[ctr]]
        ## TODO: eher brutale Methode, über config lösen !
        # Label(para, text=info).place(x=200, y=250, width=200, height=50)

    info = ActionList[ctr]
    Action = Label(master=para, text=info, font =fs02)
    Action.place(x=0, y=220, width=800, height=20)
    #info = params1[ctr]
    Label(para, text=info, font =fs02).place(x=0, y=260, width=800, height=20)

tree = ET.parse('task01.xml')
xml_root = tree.getroot()
ActionList = []
for action in xml_root.iter('comm_item'):
    ActionList.append(str(action.text.strip()))
    print("actions in List", ActionList)
max = len(ActionList)
    # TODO: ueberlegen, wie man das mit Schleifen (iterativ) hinbekommen könnte

    # for aktuell in params:
    # print("param.status "," ",aktuell,  param.status[aktuell])

ButtonNext = Button(master=para, text='Function OK', bg='green', command=next)
ButtonNext.place(x=420, y=320, width=150, height=60)




weiter = True

clockPuls()



    # eintragen in Datenbank oder xml - file ergänzen

para.mainloop()


