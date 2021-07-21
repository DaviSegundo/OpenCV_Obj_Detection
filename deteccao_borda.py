import cv2

imagem_borda = cv2.imread("test5.jpg")
cv2.imshow("Imagem Normal", imagem_borda)

imagem_borda_cinza = cv2.cvtColor(imagem_borda, cv2.COLOR_BGR2GRAY)
cv2.imshow("Imagem Cinza", imagem_borda_cinza)

limiar_inferior = 30
limiar_superior = 90

matriz_kernel = 3

imagem_borda_deteccao = cv2.Canny(imagem_borda_cinza, limiar_inferior, limiar_superior, matriz_kernel)
cv2.imshow("Imagem Deteccao", imagem_borda_deteccao)

cv2.waitKey(0)
cv2.destroyAllWindows()




