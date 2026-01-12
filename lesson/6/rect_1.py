import pygame
import sys


pygame.init()


WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pygame Input Example')


rect_size = 50
rect_x = WIDTH // 2 - rect_size // 2
rect_y = HEIGHT // 2 - rect_size // 2
rect_colors = [(0, 128, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (255, 0, 255)]
rect_color_index = 0
rect_color = rect_colors[rect_color_index]

speed = 5
score = 0
running = True

while running:
    for event in pygame.event.get():
        # If event type is pygame quit, then set running to false
        if event.type == pygame.QUIT:
            running = False
        # If event type is pygame key down
        if event.type == pygame.KEYDOWN:
            # If event type is pygame keyboard space key
            if event.key == pygame.K_SPACE:
                rect_color_index = (rect_color_index + 1) % len(rect_colors)
                rect_color = rect_colors[rect_color_index]

    keys = pygame.key.get_pressed()
    moved = False

    if keys[pygame.K_LEFT]:
        rect_x -= speed
        moved = True
    if keys[pygame.K_RIGHT]:
        rect_x += speed
        moved = True
    if keys[pygame.K_UP]:
        rect_y -= speed
        moved = True
    if keys[pygame.K_DOWN]:
        rect_y += speed
        moved = True

    if moved:
        score += 1

    
    rect_x = max(0, min(WIDTH - rect_size, rect_x))
    rect_y = max(0, min(HEIGHT - rect_size, rect_y))

    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_size, rect_size))

    
    font = pygame.font.SysFont(None, 36)
    score_surf = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_surf, (10, 10))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
