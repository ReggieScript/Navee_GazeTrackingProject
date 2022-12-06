from tkinter import *
from Functions_Navee import funciones


#icon=PhotoImage(file=r'C:\Users\reegi\GazeTracking\icon.png')

backgnd='#15133C'


class NSMenu(object):

    def newSesMenu():
        newSes = Tk()
        newSes.configure(bg=backgnd)
        gui_width = 640
        gui_height = 300

        screen_width = newSes.winfo_screenwidth()
        screen_height = newSes.winfo_screenheight()

        # find the center point
        center_x = int(screen_width/2 - gui_width / 2)
        center_y = int(screen_height/2 - gui_height / 2)

        # set the position of the newSes to the center of the screen
        newSes.geometry(f'{gui_width}x{gui_height}+{center_x}+{center_y}')

        newSes.resizable(0,0)

        newSes.title('New Session')
        #newSes.iconphoto(False,icon)

        def clear_frame(): #limpia la ventana de los widgets
            newSes.destroy()

        def pomodoro():
            clear_frame()

        pomoBut = Button(newSes,
                        text= 'Pomodoro',
                        command= pomodoro(),
                        fg=backgnd,
                        bg=backgnd,
                        activeforeground=backgnd,
                        activebackground=backgnd,
                        state=ACTIVE,
                        compound='bottom')
        pomoBut.place(x=0, y=200)

        newSes.mainloop()
