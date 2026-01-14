import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('If-Else Showcase')

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Initial state
circle_is_red = True

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # If-else statement to toggle color
                if circle_is_red:
                    circle_is_red = False
                else:
                    circle_is_red = True

    screen.fill(WHITE)
    # If-else to choose color
    if circle_is_red:
        color = RED
    else:
        color = GREEN
    pygame.draw.circle(screen, color, (WIDTH // 2, HEIGHT // 2), 50)

    pygame.display.flip()

pygame.quit()
sys.exit()
