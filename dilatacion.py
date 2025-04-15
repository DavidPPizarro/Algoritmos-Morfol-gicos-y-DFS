import cv2
import numpy as np

imagen = cv2.imread('C:/Users/Lenovo/Documents/Projects/opmorf/papers/pavement.jpg', cv2.IMREAD_GRAYSCALE)

kernel = np.ones((3,3), np.uint8)

dilatacion = cv2.dilate(imagen, kernel, iterations=1)

#delimited height and width
height, width = imagen.shape
cv2.rectangle(dilatacion, (0, 0), (width, height), (0, 0, 0), 1)
cv2.imshow('Original', imagen)
cv2.imshow('Dilatacion', dilatacion)

cv2.waitKey(0)
cv2.destroyAllWindows()
