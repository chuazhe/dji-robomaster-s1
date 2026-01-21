import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Nested If Example")

running = True
color = (0, 128, 255)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN):
                if event.key == pygame.K_LEFT:
                    color = (255, 0, 0)  # Red for left
                elif event.key == pygame.K_RIGHT:
                    color = (0, 255, 0)  # Green for right
                else:
                    color = (0, 128, 255)  # Blue for up/down

    screen.fill(color)
    pygame.display.flip()

pygame.quit()
sys.exit()
