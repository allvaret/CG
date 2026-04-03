import pygame
import sys
import threading
import queue
import math
from bresenham import desenha_reta_bresenham

pygame.init()
LARGURA, ALTURA = 640, 480
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Cg - Transformações básicas")

# Cores
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
BRANCO = (255, 255, 255)

fila = queue.Queue()


def armazena_pontos():
    print('Insira as coordenadas das vértices do polígono a ser desenhado:')
    print('Formato: x1 y1 x2 y2 ...')

    valores = list(map(int, input().split()))

    if len(valores) % 3 != 0:
        raise ValueError("Número ímpar de coordenadas. Cada ponto precisa de x e y.")

    pontos = [[valores[i], valores[i + 1]] for i in range(0, len(valores), 2)]

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
        [pontos[0], pontos[1]],
        [pontos[1], pontos[2]],
        [pontos[2], pontos[0]],
    ]
    for (x1, y1), (x2, y2) in arestas:
        desenha_reta_bresenham(tela, x1, y1, x2, y2, cor)

    return arestas


def translacao(vet_deslocamento:list, pontos:list[list[int]]):
    novos_nos = []
    for x,y in pontos:
        novo_x = x + vet_deslocamento[0]
        novo_y = y + vet_deslocamento[1]

        novos_nos.append([novo_x, novo_y])

    return novos_nos


def escala(n_escala:float, pontos:list[list[int]],):
    novos_nos = []
    centro = []
    c_x, c_y = 0, 0
    for x, y in pontos:
        c_x += x
        c_y += y
    c_x, c_y = c_x // 3, c_y // 3

    centro.append([c_x, c_y])

    centro_x = centro[0][0]
    centro_y = centro[0][1]

    for x, y in pontos:
        x_l = centro_x + (x - centro_x) * n_escala
        y_l = centro_y + (y - centro_y) * n_escala
        novos_nos.append([int(x_l), int(y_l)])
        print(novos_nos)
    return novos_nos


def rotacao(n_rotacao, pontos:list):
    novos_nos = []
    centro = []
    c_x, c_y = 0, 0
    dx, dy = 0, 0

    for x, y in pontos:
        c_x += x
        c_y += y
    c_x, c_y = c_x // 3, c_y // 3
    centro.append([c_x, c_y])

    centro_x = centro[0][0]
    centro_y = centro[0][1]

    x_l, y_l = 0, 0
    for x, y in pontos:
        dx = x - centro_x
        dy = y - centro_y

        x_l = centro_x + dx * math.cos(math.radians(n_rotacao)) - dy * math.sin(math.radians(n_rotacao))
        y_l = centro_y + dx * math.sin(math.radians(n_rotacao)) + dy * math.cos(math.radians(n_rotacao))
        x_l = int(x_l)
        y_l = int(y_l)
        novos_nos.append([x_l, y_l])
        print(novos_nos)
    return novos_nos


def thread_entrada(fila):
    """Roda em paralelo — coleta input do terminal e envia para a fila."""
    while True:
        print("\nTransformações disponíveis:\n"
              "1 - Translação\n"
              "2 - Escala\n"
              "3 - Rotação")
        transformacao = input("Escolha: ").strip()

        if transformacao == "1":
            valores = list(map(int, input("Vetor de deslocamento (x y): ").split()))
            fila.put(("translacao", valores))

        elif transformacao == "2":
            n = float(input("Escalar (0.1 a 0.99 reduz, '-' inverte): "))
            fila.put(("escala", n))

        elif transformacao == "3":
            n = int(input("Graus de rotação: "))
            fila.put(("rotacao", n))

        else:
            print("Valor inválido, tente novamente.")


# --- Inicialização ---
pontos = armazena_pontos()
tela.fill(PRETO)
desenha_triangulo(tela, pontos, VERDE)
pygame.display.flip()

# Dispara a thread de input como daemon (encerra junto com o programa)
t = threading.Thread(target=thread_entrada, args=(fila,), daemon=True)
t.start()

# --- Loop principal ---
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Verifica se chegou alguma transformação na fila
    if not fila.empty():
        transformacao, valores = fila.get()

        if transformacao == "translacao":
            pontos = translacao(valores, pontos)
        elif transformacao == "escala":
            pontos = escala(valores, pontos)
        elif transformacao == "rotacao":
            pontos = rotacao(valores, pontos)

        tela.fill(PRETO)
        desenha_triangulo(tela, pontos, VERDE)
        pygame.display.flip()

    pygame.time.wait(16)  # ~60fps, evita uso desnecessário de CPU

pygame.quit()
sys.exit()