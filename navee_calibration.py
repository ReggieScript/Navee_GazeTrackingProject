from tkinter import *
from tkinter.tix import TList
from tkinter.messagebox import showinfo, showwarning, showerror
from tkinter import ttk
from turtle import back
import Functions_Navee as ftn
import time
from playsound import playsound
from datetime import timedelta
from gaze_tracking import GazeTracking
import math
import sys
import cv2

#variables
pauseText='Pause/Play'
breakTime=0
breakTime2=0
pauseTimeB=0
exitInt=1
breakCount=0
timeLeft=0
locTime=0
x=1
trabajando = 0
breakT=0
pausa=0
pauseTime=0

#paleta de colores
global letras
global backgnd
global fondocanva

newSesColor='#EC994B'
letras= '#F1EEE9'
backgnd='#4F6BFF'
fondocanva = "#15133C"

#configuracion de la ventana

gui = Tk() 
#####################################################################################################################################
#photoimage = PhotoImage(file='C:\\Users\\oguzm\\Logo.png')

gui.configure(bg=backgnd)

icon=PhotoImage(file=r'C:\Users\reegi\GazeTracking\icon.png')
photoimage = PhotoImage(file=r'C:\Users\reegi\GazeTracking\logoNavee.png')

def canva():
    gui.title('Navee: Focus Software')
    gui.iconphoto(True,icon)
    width, height = photoimage.width(), photoimage.height()
    canvas = Canvas(gui, bg=fondocanva, width=1.5*width, height=height)
    canvas.pack()
    canvas.create_image(280,0, image=photoimage, anchor=NW)
    gui.resizable(False,False)
canva()

def clear_frame(): #limpia la ventana de los widgets
        for widgets in gui.winfo_children():
            widgets.destroy()
        canva()

def newSes():
    clear_frame()
    newSesMenu()
    
def settings():
    clear_frame()
    settingsMenu()

def pomodoro():
    clear_frame()
    workMenu()

def calib():
    ftn.calibration()


def rtn():
    global trabajando
    trabajando=0
    clear_frame()
    mainMenu()

def mainMenu():
    #Boton para iniciar una nueva sesion

    newSesBut = Button(gui,
                    text= 'New Session',
                    command=newSes,
                    font=('Comic Sans',30),
                    height=1,
                    width=10,
                    fg=letras,
                    bg=newSesColor,
                    activeforeground=newSesColor,
                    activebackground=letras,)
    newSesBut.place(x=30, y=0+36)

    setBut = Button(gui,
                    text= 'Settings',
                    command=settings,
                    font=('Comic Sans',30),
                    height=1,
                    width=10,
                    fg=letras,
                    bg=backgnd,
                    activeforeground=backgnd,
                    activebackground=letras,)
    setBut.place(x=30, y=80+72)

    statBut = Button(gui,
                    text= 'View Stats',
                    command=viewStats,
                    font=('Comic Sans',30),
                    height=1,
                    width=10,
                    fg=letras,
                    bg=backgnd,
                    activeforeground=backgnd,
                    activebackground=letras,)
    statBut.place(x=30, y=160+108)

    exitBut = Button(gui,
                    text= 'Exit',
                    command=exitCom,
                    font=('Comic Sans',30),
                    height=1,
                    width=10,
                    fg=letras,
                    bg=backgnd,
                    activeforeground=backgnd,
                    activebackground=letras,)
    exitBut.place(x=30, y=240+144)

def exitCom(): #esto no funciona
    print('haha')

def viewStats():
    print("Perrón las stats")

def returnBut():
    returnB = Button(gui,
                    text= 'Return',
                    command=rtn,
                    font=('Comic Sans',30),
                    height=1,
                    width=10,
                    fg=letras,
                    bg=backgnd,
                    activeforeground=backgnd,
                    activebackground=letras,)
    returnB.place(x=30, y=240+144)

def newSesMenu():
    gui.title('New Session')
    pomoBut = Button(gui,
                    text= 'Pomodoro',
                    command=pomodoro,
                    font=('Comic Sans',30),
                    height=1,
                    width=10,
                    fg=letras,
                    bg=backgnd,
                    activeforeground=backgnd,
                    activebackground=letras,)
    pomoBut.place(x=30, y=0+36)
    #                       15,3,21
    progBut = Button(gui,
                    text= 'Program your own session',
                    command=progOwn,
                    font=('Comic Sans',15),
                    height=3,
                    width=21,
                    fg=letras,
                    bg=backgnd,
                    activeforeground=backgnd,
                    activebackground=letras,)
    progBut.place(x=30, y=80+72)
    returnBut()

def progOwn():
    print("Perrón las settings")

def settingsMenu():
    gui.title("Settings")
    calibrationB= Button(gui,
                    text='Calibration',
                    command= calib,
                    font=('Comic Sans',30),
                    height=1,
                    width=10,
                    fg=letras,
                    bg=backgnd,
                    activeforeground=backgnd,
                    activebackground=letras,)
    calibrationB.place(x=30, y=0+36)


    soundBut= Button(gui,
                    text='Choose sound package',
                    command= soundP,
                    font=('Comic Sans',15),
                    height=3,
                    width=21,
                    fg=letras,
                    bg=backgnd,
                    activeforeground=backgnd,
                    activebackground=letras,)
    soundBut.place(x=30, y=80+72)

    returnBut()

def soundP():
    print("Perrón el Sound")

def workMenu():
    global pauseText
    gui.title("Pomodoro Working Session")
    start= Button(gui,
                    text='Start',
                    command=startSessionPomo,
                    font=('Comic Sans',30),
                    height=1,
                    width=10,
                    fg=letras,
                    bg=backgnd,
                    activeforeground=backgnd,
                    activebackground=letras,)
    start.place(x=30, y=80+72)

    pause = Button(gui,
                    text=pauseText,
                    command=pauseSession,
                    font=('Comic Sans',30),
                    height=1,
                    width=10,
                    fg=letras,
                    bg=backgnd,
                    activeforeground=backgnd,
                    activebackground=letras,)
    pause.place(x=30, y=160+108)

    returnBut()

def pauseSession():
#Poner aqui un pop up de Pausa!
    global webcam
    global trabajando
    global gaze
    global pauseTime
    global times
    global pauseText
    if trabajando == 0:
        trabajando =1
        webcam = cv2.VideoCapture(0)
        gaze=GazeTracking()
        pauseTime= time.time()-newTime
        pauseText='Pause'
    elif trabajando ==1:
        pauseText='Un-Pause'
        trabajando=0
        webcam.release()

def breakMenu():
    clear_frame()
    gui.title("Pomodoro Break")
    startB= Button(gui,
                    text='Start Break',
                    command= breakStart,
                    font=('Comic Sans',30),
                    height=1,
                    width=10,
                    fg=letras,
                    bg=backgnd,
                    activeforeground=backgnd,
                    activebackground=letras,)
    startB.place(x=30, y=80+72)

    pauseB = Button(gui,
                    text=pauseText,
                    command=breakPause,
                    font=('Comic Sans',30),
                    height=1,
                    width=10,
                    fg=letras,
                    bg=backgnd,
                    activeforeground=backgnd,
                    activebackground=letras,)
    pauseB.place(x=30, y=160+108)
    returnBut()

def breakPause():
    global pauseTimeB
    global breakT
    if breakT==0:
        breakT=1
        pauseTimeB=time.time()-breakTime2
    elif breakT==1:
        breakT=0

def breakStart():
    global breakTime1
    global sT
    global breakCount
    global breakT
    global txtB
    breakTime1=time.time()
    breakT=1
    if breakCount>3:
        sT=int(900)
        breakCount=0
    elif breakCount<3:
        sT=int(15) # 5 mins ==500!!! cambia a 15 pa revisar si jala
        breakCount=breakCount+1
    txtB= Label(gui,
                text = 'Time left: ',
                font=('Comic Sans',15),
                height=3,
                width=21,
                fg=fondocanva,
                bg=newSesColor,
                activeforeground=newSesColor,
                activebackground=fondocanva,)
    txtB.place (x=30,y=36)

def startSessionPomo():
    #AQUI CORRO TODO POR PRIMERA VEZ!!!!!!
    global timeLeft
    timeLeft=0
    global txt
    global webcam
    webcam = cv2.VideoCapture(0)
    global gaze
    gaze=GazeTracking()
    global times
    times=time.time()
    global newTime
    newTime=time.time()
    global tL
    tL=1
    global trabajando
    trabajando=1
    global wt
    wt=int(15)
    print('start')
    global attention
    attention=r"C:\Users\reegi\GazeTracking\ZeldaSoundPack\attention.mp3"
    global alarmSound
    alarmSound= r'C:\Users\reegi\GazeTracking\ZeldaSoundPack\alarm.mp3'
    txt= Label(gui,
                text = 'Time left: ',
                font=('Comic Sans',15),
                height=3,
                width=21,
                fg=fondocanva,
                bg=newSesColor,
                activeforeground=newSesColor,
                activebackground=fondocanva,)
    txt.place (x=30,y=36)

def workingTime(time1,newTime,attention):
    global x
    global locTime
    global timeLeft
    global webcam
    global gaze

    _, frame = webcam.read()
    gaze.refresh(frame)
    located= gaze.pupils_located
    if located==False:
        if x==1:
            locTime=time.time()
            x=0
        if (newTime-locTime) > 10:
            playsound(attention)
            showwarning('Pay attention!','Hey! Remember your task? Go for it!')
            x=1
    else:
        x=1
        locTime=0

    if (newTime-time1)> 1200: #5 minutos en segundos, tampoco funciona
        if timeLeft == 0:
            showinfo('Time Left', 'Only 5 minutes left, you can do this!')

mainMenu() #VA FUERA NO LO MUEVAS

while 1:
    gui.update()
    if trabajando==1:
        newTime=time.time()-pauseTime
        workingTime(times,newTime,attention)
        txt['text']='Time Left: '+str(timedelta(seconds=math.trunc(wt-(newTime-times))))
        #workProgress(newTime,times)
        if (newTime-times)> wt:
            trabajando=0
            playsound(alarmSound)
            showinfo("Work time over!", "Great job! Time for a break! Go drink some water and stretch yourself")
            webcam.release()
            breakMenu()

    if breakT==1: #incorporar contador para que se pueda decidir si es descanso corto o largo
        breakTime2= time.time()-pauseTimeB
        txtB['text']='Time Left: '+str(timedelta(seconds=math.trunc(sT-(breakTime2-breakTime1))))
        if (breakTime2-breakTime1) >sT:
            breakT=0
            playsound(alarmSound)
            showinfo("Break Time over!","Hope you got some rest! Lets keep going!")
            workMenu()
