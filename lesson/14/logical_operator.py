import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Logical Operator Example")

running = True
color = (0, 128, 255)

while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if keys[pygame.K_LEFT] and keys[pygame.K_UP]:
        color = (255, 255, 0)
    elif keys[pygame.K_LEFT] or keys[pygame.K_UP]:
        color = (0, 255, 0)
    else:
        color = (0, 128, 255)

    screen.fill(color)
    pygame.display.flip()

pygame.quit()
sys.exit()
