from tkinter import *
gui = Tk()


#15133C AZUL MARINO(LOGO)
#73777B GRIS
#EC994B NARANJA
#F1EEE9 BLANCO
#4F6BFF AZUL CLARO

#GEOMETRIA DE LOGO ES 500X500

#### CONFIG
#####################################################################################################################################
photoimage = PhotoImage(file='C:\\Users\\oguzm\\Logo.png')
#### COLORES BOTONES
letras = "#F1EEE9"
backgnd = "#15133C"

### COLOR CANVA
fondocanva = "#EC994B"
#####################################################################################################################################


### NUEVO NUEVO NUEVO NUEVO
#######################                 CREAR CANVA CON LA IMAGEN DE FONDO
def Canva():
    width, height = photoimage.width(), photoimage.height()
    canvas = Canvas(gui, bg=fondocanva, width=1.5*width, height=height)
    canvas.pack()
    canvas.create_image(280,0, image=photoimage, anchor=NW)
Canva()
#####################################################################################################################################

### LÍNEA 111
#######################                 BOTON GLOBAL RETURN
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

def rtn():
    print("Perrón el return")
#####################################################################################################################################



#######################                 FUNCIONES: MAIN MENU                    ##################################################
def newSes():
    print("Perrón la newSes")

def settings():
    print("Perrón las settings")

def viewStats():
    print("Perrón las stats")

def exitCom():
    print("Perrón la exit")
#####################################################################################################################################


#######################                 BOTONES: MAIN MENU                      #####################################################
#                                               SON LOS PRIMEROS EN APARECER
def mainMenu():
    #Boton para iniciar una nueva sesion
    newSesBut = Button(gui,
                    text= 'New Session',
                    command=newSes,
                    font=('Comic Sans',30),
                    height=1,
                    width=10,
                    fg=letras,
                    bg=backgnd,
                    activeforeground=backgnd,
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
#####################################################################################################################################


#######################                 FUNCIONES: NEW SESSION                  ####################################################
def pomodoro():
    print("Perrón el pomodoro")

def progOwn():
    print("Perrón las settings")

def viewStats():
    print("Perrón las stats")

def exitCom():
    print("Perrón la exit")
#####################################################################################################################################

# LÍNEA 152
#######################                 BOTONES: NEW SESS MENU                  ####################################################
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
#####################################################################################################################################


#######################                 FUNCIONES: NEW SESSION                  ###################################################
def calib():
    print("Perrón el CALIB")

def soundP():
    print("Perrón el Sound")
#####################################################################################################################################

### LÍNEA 162
#######################                 BOTONES: SETTINGS MENU                  ####################################################
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
#####################################################################################################################################


# LÍNEA 173
#######################                 BOTONES: POMODORO                        ####################################################
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
    start.place(x=30, y=0+36)

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
    pause.place(x=30, y=80+72)

    returnBut()
    #####################################################################################################################################

    ### LÍNEA 211
    #####################################################################################################################################
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
        startB.place(x=30, y=0+36)

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
        pauseB.place(x=30, y=80+72)
        returnBut()
#####################################################################################################################################


gui.mainloop()
