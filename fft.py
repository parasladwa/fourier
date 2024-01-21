import pygame
import math

pygame.init()

WIDTH = 800
HEIGHT = 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sine and Cosine Waves Plot")

run = True

# Set up variables for the sine and cosine waves
amplitude = 100
frequency = 0.01  # Adjust the frequency to control the number of oscillations
x_offset = 0

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((0, 0, 0))  # Fill the screen with a black background

    # Plot the sine wave
    sine_points = []
    for x in range(WIDTH):
        y = int(HEIGHT / 4 + amplitude * math.sin(frequency * (x + x_offset)))
        sine_points.append((x, y))

    pygame.draw.lines(screen, 'white', False, sine_points, 2)

    # Plot the cosine wave
    cosine_points = []
    for x in range(WIDTH):
        y = int(3 * HEIGHT / 4 + amplitude * math.cos(frequency * (x + x_offset)))
        cosine_points.append((x, y))

    pygame.draw.lines(screen, 'red', False, cosine_points, 2)

    pygame.display.update()

    x_offset += 1  # Adjust the x_offset for animation
    pygame.time.delay(10)  # Add a small delay to control the speed of the animation

# Quit Pygame
pygame.quit()
