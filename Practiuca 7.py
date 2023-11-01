# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 19:34:23 2023

@author: Javier
"""

import cv2
import numpy as np

imagen = cv2.imread("img.png")
m, n, c = imagen.shape

dx, dy = 30, 50  
translation_matrix = np.float32([[1, 0, dx], [0, 1, dy]])
imagen_transladada = cv2.warpAffine(imagen, translation_matrix, (n, m))

angle = 30  
rotation_matrix = cv2.getRotationMatrix2D((n/2, m/2), angle, 1)
imagen_rotada = cv2.warpAffine(imagen, rotation_matrix, (n, m))

scale_factor_x, scale_factor_y = 1.5, 1.5
imagen_escala = cv2.resize(imagen, None, fx=scale_factor_x, fy=scale_factor_y, interpolation=cv2.INTER_LINEAR)

x1, y1, x2, y2 = 100, 100, 300, 300
imagen_recortada = imagen[y1:y2, x1:x2]

cv2.imwrite("imagen_transladada.jpg", imagen_transladada)
cv2.imwrite("imagen_rotada.jpg", imagen_rotada)
cv2.imwrite("imagen_escala.jpg", imagen_escala)
cv2.imwrite("imagen_recortada.jpg", imagen_recortada)

cv2.imshow("Imagen Transladada", imagen_transladada)
cv2.imshow("Imagen Rotada", imagen_rotada)
cv2.imshow("Imagen Escala", imagen_escala)
cv2.imshow("Imagen Recortada", imagen_recortada)

cv2.waitKey(0)
cv2.destroyAllWindows()