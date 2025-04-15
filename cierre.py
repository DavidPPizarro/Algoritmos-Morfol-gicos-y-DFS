import cv2
import numpy as np

imagen = cv2.imread('C:/Users/Lenovo/Documents/Projects/opmorf/papers/pavement.jpg', cv2.IMREAD_GRAYSCALE)

kernel = np.ones((3,3), np.uint8)

cierre = cv2.morphologyEx(imagen, cv2.MORPH_CLOSE, kernel)
cv2.imwrite('cierre.png', cierre)
cv2.imshow('Original', imagen)
cv2.imshow('Cierre', cierre)

cv2.waitKey(0)
cv2.destroyAllWindows()
