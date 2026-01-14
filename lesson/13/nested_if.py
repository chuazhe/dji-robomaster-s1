import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Nested If Example (Easy)')

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


circle_x = WIDTH // 2
circle_y = HEIGHT // 2
radius = 40


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_pos = pygame.math.Vector2(mouse_x, mouse_y)
    circle_pos = pygame.math.Vector2(circle_x, circle_y)
    if mouse_pos.distance_to(circle_pos) < radius:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            color = RED  
        else:
            color = GREEN  
    else:
        color = BLUE   

    screen.fill(WHITE)
    pygame.draw.circle(screen, color, (circle_x, circle_y), radius)
    pygame.display.flip()
