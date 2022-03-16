import cv2
import glob
import time
from detector_vehiculos import DetectorVehiculos
#from ipcamara import ipcamara


#ipcamara() 
def contador_vehiculos():
    carpeta_vehiculos_contador = 0
    dv = DetectorVehiculos() #Se carga el objeto de la clase vehicle detector y se almacena en la carpeta dv.

    carpeta_img = glob.glob("imagenes/*.jpg") #Se rutean las imágenes apuntado a una carpeta. Se define la carpeta y formato de imagen.
    #carpeta_img = glob.glob("imagen_ejemplo/*.jpg") #para el ejemplo

    #Variable que representa la cantidad de vehiculos total en todas las imagenes analizadas que se asigna con un valor inical cero que se va a actualizar con el codigo de la linea 22

    for directorio_img in carpeta_img:
        print("Directorio Imagen", directorio_img) #se imprime el valor deliterador como un string
        img = cv2.imread(directorio_img) 

        caja_vehiculos = dv.detectar_vehiculos(img)
        contador_vehiculos = len(caja_vehiculos)

        # se actualiza el total de vehiculos
        carpeta_vehiculos_contador += contador_vehiculos

        for caja in caja_vehiculos:
            x, y, w, h = caja #valor del interador se asigna a variables de una letra

            cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3) #formato de la marca del vehiculo detectado en la imagen.
            font = cv2.FONT_ITALIC
            cv2.putText(img, "Vehiculos: " + str(contador_vehiculos), (20, 55), font, 2, (0, 0, 0), 3) #formato del texto que aparece en la imagen.

        #cv2.imshow("Vehiculos", img) #para el ejemplo
        cv2.waitKey(1000)

    return carpeta_vehiculos_contador


#contador_vehiculos()