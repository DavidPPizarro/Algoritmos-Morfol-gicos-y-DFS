import cv2
import numpy as np

# Cargar imagen en escala de grises
imagen = cv2.imread('imagen.jpg', cv2.IMREAD_GRAYSCALE)

# Crear un kernel
kernel = np.ones((5,5), np.uint8)

erosion = cv2.erode(imagen, kernel, iterations=1)
dilatacion = cv2.dilate(erosion, kernel, iterations=1)

# Mostrar imágenes
cv2.imshow('Original', imagen)
cv2.imshow('Apertura 2', dilatacion)

cv2.waitKey(0)
cv2.destroyAllWindows()
