# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 20:12:52 2023

@author: Javier
"""

import cv2
import numpy as np

img = cv2.imread("img.png")

x = cv2.Sobel(img, cv2.CV_16S, 1, 0)
y = cv2.Sobel(img, cv2.CV_16S, 0, 1)

absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)

dst = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

cv2.imshow("Gradiente en X (absX)", absX)
cv2.imshow("Gradiente en Y (absY)", absY)
cv2.imshow("Resultado", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
