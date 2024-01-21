import pygame
import math
import time

pygame.init()

WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))

run = True


clicked = False
locations = []

while run:
    
    for event in pygame.event.get():
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event)
            print(event.pos)
            clicked = True

        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False
            run = False
            
        if event.type == pygame.QUIT:
            run = False
            
        if clicked:
            pygame.draw.circle(screen, 'white', event.pos, 2)
            locations.append(event.pos)
        
        pygame.display.update()




def generateEquation(points):
    n = 2
    x, y = 0, 0
    s= 3

    for m in range(len(points) - 1, -1, -1):
        points[m] = (points[m][0] - 250, 250 - points[m][1])
        points.append(points[m])

    xt = yt = ""
    M = len(points)
    r = []
    for k in range(-n, n + 1):
        cx = cy = 0
        for m in range(M):
            cx += math.cos(2 * math.pi * k * m / M) * points[m][0] + math.sin(2 * math.pi * k * m / M) * points[m][1]
            cy += math.cos(2 * math.pi * k * m / M) * points[m][1] - math.sin(2 * math.pi * k * m / M) * points[m][0]

        if k != -n:
            xt += " + "
            yt += " + "

        xt += f"{cx / M} cos({k * math.pi}t) - {cy / M} sin({k * math.pi}t)"
        yt += f"{cx / M} sin({k * math.pi}t) + {cy / M} cos({k * math.pi}t)"
        r.append((cx / M, cy / M))

    eq = f"({x} + {s}({xt}), {y} + {s}({yt}))".replace(" + -", " - ").replace(" - -", " + ")
    return eq, r







