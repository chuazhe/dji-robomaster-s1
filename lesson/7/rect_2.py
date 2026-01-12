import pygame
import sys


pygame.init()


WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pygame Input Example')


rect_size = 50
score = 0
rect_x = WIDTH // 2 - rect_size // 2
rect_y = HEIGHT // 2 - rect_size // 2
rect_colors = [(0, 128, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (255, 0, 255)]
rect_color_index = 0
rect_color = rect_colors[rect_color_index]

speed = 5
import random


obstacle_size = 40
obstacle_color = (220, 50, 50)
obstacle_x = random.randint(100, WIDTH - 100)
obstacle_y = random.randint(100, HEIGHT - 100)
running = True

while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_SPACE:
                rect_color_index = (rect_color_index + 1) % len(rect_colors)
                rect_color = rect_colors[rect_color_index]
            
            if event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                speed = min(speed + 1, 20)
            
            if event.key == pygame.K_MINUS:
                speed = max(speed - 1, 1)

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

    
    char_rect = pygame.Rect(rect_x, rect_y, rect_size, rect_size)
    obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_size, obstacle_size)
    if char_rect.colliderect(obstacle_rect):
        
        rect_x = WIDTH // 2 - rect_size // 2
        rect_y = HEIGHT // 2 - rect_size // 2
        obstacle_x = random.randint(100, WIDTH - 100)
        obstacle_y = random.randint(100, HEIGHT - 100)

    if moved:
        score += 1

    
    rect_x = max(0, min(WIDTH - rect_size, rect_x))
    rect_y = max(0, min(HEIGHT - rect_size, rect_y))


    screen.fill((30, 30, 30))
    
    pygame.draw.rect(screen, obstacle_color, (obstacle_x, obstacle_y, obstacle_size, obstacle_size))
    
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_size, rect_size))

    

    font = pygame.font.SysFont(None, 36)
    speed_surf = font.render(f'Speed: {speed}', True, (0, 0, 0))
    screen.blit(speed_surf, (10, 10))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
