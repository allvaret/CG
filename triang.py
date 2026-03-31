import pygame
import sys
from main import desenha_reta_bresenham
# Inicialização padrão conforme Aula 03


def triangulo(a, b, c, x_Centro, y_Centro):
    if a == b and b == c:
        print("triangulo retangulo")
        desenha_reta_bresenham(tela, )


pygame.init()
LARGURA, ALTURA = 640, 480
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Cg - Transformações básicas")

# Cores
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
BRANCO = (255, 255, 255)
LARANJA = (255, 165, 0)

tela.fill(PRETO)
pygame.display.flip()

# Loop Principal
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False


pygame.quit()
sys.exit()

