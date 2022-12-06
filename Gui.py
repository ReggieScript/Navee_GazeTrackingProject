from tkinter import *
from newSession import NSMenu

backgnd='#15133C'

#configuracion de la ventana

gui = Tk()  

gui.configure(bg=backgnd)

newSesPic = PhotoImage(file=r'C:\Users\reegi\GazeTracking\Botones\newsession.png') 
setPic = PhotoImage(file=r'C:\Users\reegi\GazeTracking\Botones\settings.png')
exitPic = PhotoImage(file=r'C:\Users\reegi\GazeTracking\Botones\exit.png')

icon=PhotoImage(file=r'C:\Users\reegi\GazeTracking\icon.png')
logo = PhotoImage(file='Logo.png')

gui.title('Navee: Focus Software')
gui.iconphoto(False,icon)
gui_width = 640
gui_height = 300


# get the screen dimension
screen_width = gui.winfo_screenwidth()
screen_height = gui.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - gui_width / 2)
center_y = int(screen_height/2 - gui_height / 2)

# set the position of the gui to the center of the screen
gui.geometry(f'{gui_width}x{gui_height}+{center_x}+{center_y}')

gui.resizable(0,0)

#palette

def clear_frame(): #limpia la ventana de los widgets
    gui.destroy()

def newSes():
    clear_frame()
    NSMenu.newSesMenu()
    
def settings():
    clear_frame()

def pomodoro():
    clear_frame()


def mainMenu():

    #Boton para iniciar una nueva sesion

        newSesBut = Button(gui,
                        command=newSes,
                        fg=backgnd,
                        bg=backgnd,
                        activeforeground=backgnd,
                        activebackground=backgnd,
                        state=ACTIVE,
                        image=newSesPic,
                        relief=RAISED)
        #button.pack(side=LEFT)
        newSesBut.place(x=0, y=10)


        #boton para los settings

        setBut = Button(gui,
                        command=settings,
                        fg=backgnd,
                        bg=backgnd,
                        activeforeground=backgnd,
                        activebackground=backgnd,
                        state=ACTIVE,
                        image=setPic,
                        compound='bottom')
        #button2.pack(side=LEFT))
        setBut.place(x=0, y=100)

        #boton para salir

        exitBut = Button(gui,
                        command=lambda:gui.quit(),
                        fg=backgnd,
                        bg=backgnd,
                        activeforeground=backgnd,
                        activebackground=backgnd,
                        state=ACTIVE,
                        image=exitPic,
                        compound='bottom')
        exitBut.place(x=0, y=200)

mainMenu()

gui.mainloop()