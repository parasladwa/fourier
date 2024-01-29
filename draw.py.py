import pygame
import math
import time
import numpy as np
import matplotlib as plt
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

pygame.QUIT
print(locations)


