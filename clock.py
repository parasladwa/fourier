import pygame
import math

pygame.init()

WIDTH = 500
HEIGHT = 500

screen = pygame.display.set_mode((WIDTH, HEIGHT))

run = True
clock = pygame.time.Clock()

clicked = False
locations = []

def generateEquation(points):
    n = 2
    x, y = 0, 0
    s = 3

    for m in range(len(points) - 1, -1, -1):
        points[m] = (points[m][0] - 250, 250 - points[m][1])
        points.append(points[m])

    xt = yt = ""
    M = len(points)
    r = []
    for k in range(-n, n + 1):
        cx = cy = 0
        for m in range(M):
            cx += math.cos(2 * math.pi * k * m / M) * points[m][0] - math.sin(2 * math.pi * k * m / M) * points[m][1]
            cy += math.cos(2 * math.pi * k * m / M) * points[m][1] + math.sin(2 * math.pi * k * m / M) * points[m][0]

        if k != -n:
            xt += " + "
            yt += " + "

        xt += f"{cx / M} * cos({k * math.pi} * t)"
        yt += f"{cy / M} * sin({k * math.pi} * t)"
        r.append((cx / M, cy / M))

    eq = f"({x} + {s} * ({xt}), {y} + {s} * ({yt}))".replace(" + -", " - ").replace(" - -", " + ")
    return eq, r

while run:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True

        if event.type == pygame.MOUSEBUTTONUP:
            clicked = False

        if event.type == pygame.QUIT:
            run = False

        if clicked:
            pygame.draw.circle(screen, 'white', event.pos, 2)
            locations.append(event.pos)

    # Draw the Fourier series curve in real-time
    if len(locations) > 1:
        t_max = 2 * math.pi
        dt = 0.01
        t_values = [i * dt for i in range(int(t_max / dt))]
        points = []

        for t in t_values:
            x, y = 0, 0
            for k, (a, b) in enumerate(generateEquation(locations)[1]):
                x += a * math.cos(k * t)
                y += b * math.sin(k * t)
            points.append((int(x) + WIDTH // 2, HEIGHT // 2 - int(y)))

        # Draw the Fourier series curve
        pygame.draw.lines(screen, 'red', False, points, 2)
        pygame.display.update()

    clock.tick(30)  # Limit frames per second

    pygame.display.flip()

# Wait for user to close the window
waiting = True
while waiting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            waiting = False

pygame.quit()
