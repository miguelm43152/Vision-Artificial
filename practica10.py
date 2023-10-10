#Practica10
#Miguel Ángel Mendoza Hernández
# Registro: 20110144
# Grupo: 6E

import cv2
cap = cv2.VideoCapture(0)

while True:

    ret,frame = cap.read()
    imagen = cv2.Canny( frame,100,200)
    cv2.imshow("video",frame)
    if (cv2.waitKey(1) == ord('q') ):
        break

cap.release()
cv2.destroyAllWindows()
