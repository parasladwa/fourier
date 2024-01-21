import pygame
import time
import math

pygame.init()

WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))

run = True
angle = 0

while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    
    
    
    screen.fill((0, 0, 0))
    clock_center = (250, 250)
    hour_hand_length = 100
    
    angle += 0.01  # Adjust the speed of rotation
    end_point = (
        clock_center[0] + hour_hand_length * math.cos(angle),
        clock_center[1] + hour_hand_length * math.sin(angle)
    )

    # Draw the hour hand
    pygame.draw.line(screen, 'white', clock_center, end_point, 5)

    pygame.display.update()
    pygame.time.delay(100)
    
    
    
        

 
pygame.QUIT 


