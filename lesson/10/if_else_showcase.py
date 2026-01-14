import pygame
import sys


pygame.init()


WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('If-Else Showcase')


RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)


circle_is_red = True


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                
                if circle_is_red:
                    circle_is_red = False
                else:
                    circle_is_red = True

    screen.fill(WHITE)
    
    if circle_is_red:
        color = RED
    else:
        color = GREEN
    pygame.draw.circle(screen, color, (WIDTH // 2, HEIGHT // 2), 50)

    pygame.display.flip()

pygame.quit()
sys.exit()
