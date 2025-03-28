import cv2
import numpy as np

imagen = cv2.imread('imagen.jpg', cv2.IMREAD_GRAYSCALE)

kernel = np.ones((5,5), np.uint8)

cierre = cv2.morphologyEx(imagen, cv2.MORPH_CLOSE, kernel)

cv2.imshow('Original', imagen)
cv2.imshow('Cierre', cierre)

cv2.waitKey(0)
cv2.destroyAllWindows()
