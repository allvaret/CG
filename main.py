import pygame

def desenha_reta_bresenham(tela, x1, y1, x2, y2, cor):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    # Define direção do passo em x e y
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1

    x, y = x1, y1

    # Caso dominante em X
    if dx >= dy:
        p = 2 * dy - dx
        for _ in range(dx + 1):
            tela.set_at((x, y), cor)
            x += sx
            if p >= 0:
                y += sy
                p += 2 * dy - 2 * dx
            else:
                p += 2 * dy

    # Caso dominante em Y (troca os papéis de x e y)
    else:
        p = 2 * dx - dy
        for _ in range(dy + 1):
            tela.set_at((x, y), cor)
            y += sy
            if p >= 0:
                x += sx
                p += 2 * dx - 2 * dy
            else:
                p += 2 * dx

    pygame.display.flip()
