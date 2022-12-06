import cv2
from gaze_tracking import GazeTracking
import time
from playsound import playsound

def workingTime(time1,newTime,attention,timeLeft):
   
   #todo esto se define en la primera iteracion SOLAMENTE
    _, frame = webcam.read()
    gaze.refresh(frame)
    located= gaze.pupils_located

    preLoop=time.time()
    while located == False:
        noPupilTime=time.time()
        if (noPupilTime-preLoop) > 10:
            #Aqui lanzamos la alerta de tiempo sin ver la pantalla
            playsound(attention)
            print("pon atencion!")
            break
        _, frame = webcam.read()
        gaze.refresh(frame)
        located= gaze.pupils_located
        if located == True:
            break

    if (times-newTime)> 1200:
        if timeLeft == 0:
            print("solo quedan 5 minutos, tu puedes!")
            #aqui se muestra una notificacion de que "solo quedan 5 minutos mas! Tu puedes!"


#Breaktime es un contador de descanso, sea largo o corto
def breakTime(shortTime,longTime): #hay que ver como incorporar los ciclos
    
    print("Time for a short break!")
    time1=time.time()
    time2=time.time()
    while (time2-time1)<shortTime:
        time2=time.time()
    print("Time for work again!")
    print("Time for a long break!")
    while(time2-time1)<longTime:
        time2=time.time()
#falta arreglar la funcion de calibracion

def calibration():
    gaze=GazeTracking()
    webcam = cv2.VideoCapture(0)

    while True:
    # We get a new frame from the webcam
        _, frame = webcam.read()

        # We send this frame to GazeTracking to analyze it
        gaze.refresh(frame)


        if gaze.is_blinking():
            text = "Blinking"
        elif gaze.is_right():
            text = "Looking right"
        elif gaze.is_left():
            text = "Looking left"
        elif gaze.is_center():
            text = "Looking center"
        else:
            text="Not Detected"

        exit='Press ESC to exit'

        cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
        cv2.putText(frame, exit, (0, 400), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

        left_pupil = gaze.pupil_left_coords()
        right_pupil = gaze.pupil_right_coords()
        cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
        cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

        cv2.imshow("Demo", frame)

        if cv2.waitKey(1)==27:
            break
    webcam.release()
    cv2.destroyAllWindows()

#def soundSelect():
#definir los sonidos como variables globales