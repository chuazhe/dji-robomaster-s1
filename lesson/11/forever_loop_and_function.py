import pygame
import sys


pygame.init()


WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Forever Loop & Function Showcase')


BLUE = (0, 0, 255)
WHITE = (255, 255, 255)


def draw_moving_rect(x):
    pygame.draw.rect(screen, BLUE, (x, HEIGHT // 2 - 25, 50, 50))


rect_x = 0
speed = 2


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)
    draw_moving_rect(rect_x)
    rect_x += speed
    if rect_x > WIDTH:
        rect_x = -50  

    pygame.display.flip()
    pygame.time.delay(10)
