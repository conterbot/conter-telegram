import cv2
import numpy as np

import os
from datetime import datetime

def ipcamara():
# Definimos el directorio en el cual se van a guardar las imagenes
    directorio = r'C:\Users\Usuario\Desktop\conter_bot\imagenes'
    
    # definimos una variable i para asignar un nombre unico a cada imagen
    i = 1

    # Abre la ipcamara
    video = cv2.VideoCapture('rtsp://192.168.1.108:554/')
    #video.set(cv2.CAP_PROP_FPS, 1)
    
    # Ret es un boleano que retorna si es que el frame esta disponible o no. 
    # img es un vector de matriz de imágenes capturado en función de los fotogramas por segundo predeterminados definidos explícita o implícitamente
    # El vdeo se lee mediante la funcion read(), se extrae y se retorna un frame(imagen)
    ret, img = video.read()

    # en caso de que no haya frames disponibles, se corta el flujo
    if ret == False:
        return print('Error') 

    # se le asigna un nombre a la imagen
    nombre_foto = 'foto'+str(i)+'.jpg' 

    # la funcion imwrite guarda la imagen al directorio especificado con el nombre asignado
    cv2.imwrite(os.path.join(directorio,nombre_foto),img)

    # se asigna una fuente a ser utilizada
    font = cv2.FONT_HERSHEY_PLAIN

    # se asigna un texto que aparecera en cada imagen con la fecha y hora de la toma
    cv2.putText(img, str(datetime.now()), (20, 40),
                font, 2, (255, 255, 255), 2, cv2.LINE_AA)

    # muestra el video
    #cv2.imshow('live video', img) 
    
    # close the camera
    video.release()
    
    # close open windows
    cv2.destroyAllWindows()
