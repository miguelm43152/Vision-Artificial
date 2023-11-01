import cv2
import numpy as np
imagen = cv2.imread("img.jpg")
m, n, c = imagen.shape
############################## Traslacion ##################################
dx, dy = 30, 50  
translation_matrix = np.float32([[1, 0, dx], [0, 1, dy]]) #Matriz de trasformacion
# [ 1 0 dx]
# [ 0 1 dy]
imagen_transladada = cv2.warpAffine(imagen, translation_matrix, (n, m))
# imagen de entrada, matriz de transformación (2x3), tamagno de imagen de salida
############################## Rotacion ##################################
angle = 30  
rotation_matrix = cv2.getRotationMatrix2D((n/2, m/2), angle, 1)
# matriz de rotacion: centro de rotacion de la imagen, angulo de rotacion en grados
# escala, valor de escala isotropica (ampliacion de imagen)

imagen_rotada = cv2.warpAffine(imagen, rotation_matrix, (n, m))
# imagen de entrada, matriz de transformación (2x3), tamagno de imagen de salida

############################## Escalado ##################################
imagen_escala = cv2.resize(imagen, (800,600) ,interpolation=cv2.INTER_LINEAR)
# imagen de entrada, nuevo tamagno de la imagen de salida, metodo de interpolacion
################# Recortando una imagen ###################################
x1, y1, x2, y2 = 100, 100, 300, 300
imagen_recortada = imagen[y1:y2, x1:x2]

# Guarda las transformaciones creadas en archivos nuevos
cv2.imwrite("imagen_transladada.jpg", imagen_transladada)
cv2.imwrite("imagen_rotada.jpg", imagen_rotada)
cv2.imwrite("imagen_escala.jpg", imagen_escala)
cv2.imwrite("imagen_recortada.jpg", imagen_recortada)

# muestra los resultados de las transformaciones
cv2.imshow("Imagen original", imagen)
cv2.imshow("Imagen Transladada", imagen_transladada)
cv2.imshow("Imagen Rotada", imagen_rotada)
cv2.imshow("Imagen Escala", imagen_escala)
cv2.imshow("Imagen Recortada", imagen_recortada)
cv2.waitKey(0)
cv2.destroyAllWindows()
