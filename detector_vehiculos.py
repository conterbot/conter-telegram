import cv2
import numpy as np

class DetectorVehiculos: #crea clase detector de vehículo

    def __init__(self): # se crea el objeto detector de vehículos
        # Carga la Network
        net = cv2.dnn.readNet("dnn_model/yolov4.weights", "dnn_model/yolov4.cfg") #dnn.readNet es un metodo de cv2 es un metodo de cv2 que acepta dos parametros, y se pasa un archivo .weight que es muy pesado, que tiene la red
        self.modelo = cv2.dnn_DetectionModel(net)
        self.modelo.setInputParams(size=(832,832), scale=1 / 255) # setear los Parametros de los inputs a analizar para que la imagen que se va a analizar se pueda matchear con los parametros del entrenamieto en net.

        self.clases_permitidas = [2, 3, 5, 6, 7] #crea una lista con las clases correspondientes solo a vehiculos. El numero correspondiente a vehiculos se determino en yolov4.


    def detectar_vehiculos(self, img): # se define el método de detección de vehículos.
        # Deteccion de Objetos
        caja_vehiculos = []
        ids, probabilidades, cajas = self.modelo.detect(img, nmsThreshold=0.4)
        for id, probabilidad, caja in zip(ids, probabilidades, cajas):  #iteracion de los tres numeros que vienem del detector al analizar la imagen.
            if probabilidad < 0.5:
                # condicional de la iteración que evalua el score y hace que continue a la siguiente condicion (descarta) si el valor es bajo.
                continue

            if id in self.clases_permitidas:
                #condicional que evaluar en base a si el id de la clase está en la lista de clases permitidas. 
                caja_vehiculos.append(caja) #y si está en la lista de clases permitidas agregar a la lista caja de vehiculos el valor de cajas que serían la cantidad de marcadores de autos que encontró en la imagen 

        return caja_vehiculos #retornar el valor de marcadores de autos

