import cv2
import numpy as np

img = cv2.imread("img.jpg")

gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#convierte la imagen de entrada en escala de grises

x = cv2.Sobel(gris, cv2.CV_16S, 1, 0)
#toma la imagen en escala de grises y la convierte a short 16 bits, luego hace la primer derivada en X
y = cv2.Sobel(gris, cv2.CV_16S, 0, 1)
#toma la imagen en escala de grises y la convierte a short 16 bits, luego hace la primer derivada en Y

absX = cv2.convertScaleAbs(x)
#calcula el valor absoluto y convierte el resultado en 8 bit
#absX = np.absolute( x)
#absX = absX * 0.5
#absX = absX.astype( np.uint8)

absY = cv2.convertScaleAbs(y)

#dst = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
#la expresion anterior calcula la suma de absX y de absY con pesos. Puede ser reemplazada
# por la siguiente suma
dst = absX*0.5 + absY*0.5
dst = dst.astype( np.uint8 )

# Guarda resultados en imagenes
cv2.imwrite( "Gradiente X.jpg", absX )
cv2.imwrite( "Gradiente Y.jpg", absY )
cv2.imwrite( "Resultado.jpg", dst )

# Imprime resultados
cv2.imshow("Gradiente en X (absX)", absX)
cv2.imshow("Gradiente en Y (absY)", absY)
cv2.imshow("Resultado", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
