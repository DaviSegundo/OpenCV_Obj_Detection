import cv2

# leitura do arq de img
imagem = cv2.imread("sac.png")

# estruturador das informacoes da deteccao de face
classificador = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# transformacao da imagem para escala de cor cinza -> Mais eficiente
imagemcinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

deteccoes = classificador.detectMultiScale(imagemcinza,
                                           scaleFactor=1.12,
                                           minNeighbors=4,
                                           minSize=(10, 10),
                                           maxSize=(400, 400))

'''
# matrizes com informacoes das posicoes das faces
print(deteccoes)

# numero de faces detectadas
print(len(deteccoes))
'''

""" 
for para construir as caixas de deteccoes 
x = eixo x de pixels da imagem
y = eixo y de pixels da imagem
l = largura de pixels para a direita que a caixa anda
a = altura de pixels para baixo que a caixa anda
"""
for(x, y, l, a) in deteccoes:
    cv2.rectangle(imagem, (x, y), (x+l, y+a), (255, 0, 255), 3)

# cria a janela de exibicao
cv2.imshow('Detector de Faces', imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()

