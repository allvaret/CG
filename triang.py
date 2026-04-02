import pygame
import sys
from main import desenha_reta_bresenham

pygame.init()
LARGURA, ALTURA = 640, 480
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Cg - Transformações básicas")

def armazena_pontos():
    print('Insira as coordenadas das vértices do polígono a ser desenhado:')
    print('Formato: x1 y1 x2 y2 ...')

    valores = list(map(int, input().split()))

    if len(valores) % 3 != 0:
        raise ValueError("Número ímpar de coordenadas. Cada ponto precisa de x e y.")

    pontos = [[valores[i], valores[i+1]] for i in range(0, len(valores), 2)]

    return pontos


def desenha_triangulo(tela, pontos, cor):
    """
    Recebe lista de 3 pontos [[x1,y1], [x2,y2], [x3,y3]]
    e desenha as 3 arestas do triângulo.
    """
    if len(pontos) != 3:
        raise ValueError("Um triângulo precisa de exatamente 3 vértices.")
    print(pontos)
    # Define os 3 pares de arestas explicitamente
    # Aresta 1: ponto 0 → ponto 1
    # Aresta 2: ponto 1 → ponto 2
    # Aresta 3: ponto 2 → ponto 0  ← fecha o triângulo
    arestas = [
        (pontos[0], pontos[1]),
        (pontos[1], pontos[2]),
        (pontos[2], pontos[0]),
    ]

    for (x1, y1), (x2, y2) in arestas:
        desenha_reta_bresenham(tela, x1, y1, x2, y2, cor)


# Cores
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
BRANCO = (255, 255, 255)
LARANJA = (255, 165, 0)

# Teste
desenha_triangulo(tela, armazena_pontos(), VERDE)

pygame.display.flip()

# Loop Principal
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False


pygame.quit()
sys.exit()

