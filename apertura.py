import cv2
import numpy as np

imagen = cv2.imread('imagen.jpg', cv2.IMREAD_GRAYSCALE)

kernel = np.ones((5,5), np.uint8)

apertura = cv2.morphologyEx(imagen, cv2.MORPH_OPEN, kernel)

cv2.imshow('Original', imagen)
cv2.imshow('Apertura', apertura)

cv2.waitKey(0)
cv2.destroyAllWindows()
