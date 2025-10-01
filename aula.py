import cv2
# Carregar imagem
img = cv2.imread("vasco.jpeg")
cv2.imshow("Gigante da Colina", img)
# Espera até pressionar uma tecla
cv2.waitKey(0)
cv2.destroyAllWindows()
