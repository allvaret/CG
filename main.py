import pygame
import sys

# Inicialização padrão conforme Aula 03
pygame.init()
LARGURA, ALTURA = 640, 480
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Aula 03 - Algoritmo de Bresenham (Retas)")

# Cores
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
BRANCO = (255, 255, 255)
LARANJA = (255, 165, 0)


def desenha_reta_bresenham(tela, x1, y1, x2, y2, cor):
    """
    Implementação do Algoritmo de Bresenham para o primeiro octante.
    Utiliza apenas aritmética inteira (objetivo da aula).
    """

    if x1 > x2:
        dx = x1 - x2
        x = x2
    else:
        dx = x2 - x1
        x = x1

    if y1 > y2:
        dy = y1 - y2
        y = y2
    else:
        dy = y2 - y1
        y = y1

    # Variável de decisão inicial (P)
    p = 2 * dy - dx


    # Plota o ponto inicial
    tela.set_at((x, y), cor)

    f_x = x
    while x < (dx + f_x):
        x += 1
        if p < 0:
            # Caso P < 0: pixel Leste (E)
            p = p + 2 * dy
        else:
            # Caso P >= 0: pixel Nordeste (NE)
            y += 1
            p = p + 2 * dy - 2 * dx

        tela.set_at((x, y), cor)


# Loop Principal
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Note que dx > dy para funcionar nesta versão simplificada (1º octante)
    desenha_reta_bresenham(tela, 15, 15,600 ,480 , VERDE)
    pygame.display.flip()

pygame.quit()
sys.exit()