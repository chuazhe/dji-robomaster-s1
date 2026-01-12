import pygame
import random
import sys

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, rect)

pygame.init()

WIDTH, HEIGHT = 500, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Random Number Generator")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 200)


font = pygame.font.SysFont(None, 72)
small_font = pygame.font.SysFont(None, 28)
clock = pygame.time.Clock()
number = 0
min_val = 1
max_val = 100

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                number = random.randint(min_val, max_val)

    range_text = f"Range: {min_val} to {max_val}"
    draw_text(range_text, small_font, BLACK, WIDTH // 2, 40)

    draw_text(str(number), font, BLUE, WIDTH // 2, HEIGHT // 2)
    draw_text("Press SPACE for new number", small_font, BLACK, WIDTH // 2, HEIGHT - 40)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
