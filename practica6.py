#Practica 6
#Miguel Ángel Mendoza Hernández
# Registro: 20110144
# Grupo: 6E

import cv2
import numpy as np
import random

tamaño = (3,3)

class Imagen:
    
    def __init__(this,imagen):
        this.img = imagen
        n,m,c = imagen.shape
        this.n = n
        this.m = m
        this.c = c
        
    def mostrarImagen(this,titulo:str='',tiempo:int=0):
        cv2.imshow(titulo,this.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def normal(this):
        for x in range(this.n):
            for y in range(this.m):
                num = random.randint(0,100)
                if( num > 90 ):
                    for z in range(this.c):
                        num = 255*random.randint(0,1)
                        this.img[x,y,z] = num

    def salPimienta(this):
        for x in range(this.n):
            for y in range(this.m):
                num = random.randint(0,100)
                if( num > 90 ):
                    num = 255*random.randint(0,1)
                    for z in range(this.c):                
                        this.img[x,y,z] = num

    def blur(this):
        this.img = cv2.blur(this.img, (30,30))
    def mblur(this):
        this.img = cv2.medianBlur(this.img, 3)
    def gblur(this):
        this.img = cv2.GaussianBlur(this.img,(5,5),cv2.BORDER_DEFAULT)

imagen = Imagen( cv2.imread("Ladrillo.jpg") )
imagen.mostrarImagen("imagen original")

ruidoNormal = Imagen( imagen.img.copy() )
ruidoNormal.normal()
ruidoNormal.mostrarImagen("ruido normal")

n1 = Imagen( ruidoNormal.img.copy() )
n1.blur()
n1.mostrarImagen("Normal Filtrada1")

n2 = Imagen( ruidoNormal.img.copy() )
n2.mblur()
n2.mostrarImagen("Normal Filtrada2")

n3 = Imagen( ruidoNormal.img.copy() )
n3.gblur()
n3.mostrarImagen("Normal Filtrada3")

ruidoSP = Imagen( imagen.img.copy() )
ruidoSP.salPimienta()
ruidoSP.mostrarImagen("ruido sal pimienta")

sp1 = Imagen( ruidoSP.img.copy() )
sp1.blur()
sp1.mostrarImagen("Sal Pimienta Filtrada1")

sp2 = Imagen( ruidoSP.img.copy() )
sp2.mblur()
sp2.mostrarImagen("Sal Pimienta Filtrada2")

sp3 = Imagen( ruidoSP.img.copy() )
sp3.gblur()
sp3.mostrarImagen("Sal Pimienta Filtrada3")
