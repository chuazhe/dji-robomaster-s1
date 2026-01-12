import pygame
import sys
import time


pygame.init()

WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Cute Cartoon Character with Speech')


char_x, char_y = 100, 100
char_size = 60



message = "Hello!"
show_bubble = False
bubble_text = ""
bubble_timer = 0



running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print(f"Show bubble: {message}")
                bubble_text = message
                show_bubble = True
                bubble_timer = pygame.time.get_ticks()
            if event.key == pygame.K_s:
                print("Show bubble: Sleep")
                bubble_text = "Sleep"
                show_bubble = True
                bubble_timer = pygame.time.get_ticks()
                pygame.display.flip()
                pygame.time.wait(2000)
                bubble_text = "Awake!"
                bubble_timer = pygame.time.get_ticks()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        char_x -= 5
    if keys[pygame.K_RIGHT]:
        char_x += 5
    if keys[pygame.K_UP]:
        char_y -= 5
    if keys[pygame.K_DOWN]:
        char_y += 5


    screen.fill((220, 240, 255))
    
    center = (char_x + char_size // 2, char_y + char_size // 2)
    
    pygame.draw.ellipse(screen, (255, 230, 200), (char_x, char_y, char_size, char_size))
    
    pygame.draw.ellipse(screen, (255, 230, 200), (char_x + 10, char_y - 40, 15, 40))
    pygame.draw.ellipse(screen, (255, 230, 200), (char_x + char_size - 25, char_y - 40, 15, 40))
    
    pygame.draw.ellipse(screen, (0, 0, 0), (char_x + 18, char_y + 20, 8, 12))
    pygame.draw.ellipse(screen, (0, 0, 0), (char_x + char_size - 26, char_y + 20, 8, 12))
    
    pygame.draw.ellipse(screen, (255, 150, 150), (char_x + char_size // 2 - 5, char_y + 35, 10, 7))
    
    pygame.draw.arc(screen, (0, 0, 0), (char_x + 18, char_y + 30, 24, 18), 3.5, 5.8, 2)

    
    if show_bubble:
        
        if pygame.time.get_ticks() - bubble_timer < 2000:
            font = pygame.font.SysFont(None, 28)
            text_surf = font.render(bubble_text, True, (0, 0, 0))
            bubble_width = text_surf.get_width() + 20
            bubble_height = text_surf.get_height() + 20
            bubble_x = char_x + char_size + 10
            bubble_y = char_y - 10
            pygame.draw.rect(screen, (255, 255, 255), (bubble_x, bubble_y, bubble_width, bubble_height), border_radius=10)
            pygame.draw.rect(screen, (0, 0, 0), (bubble_x, bubble_y, bubble_width, bubble_height), 2, border_radius=10)
            screen.blit(text_surf, (bubble_x + 10, bubble_y + 10))
            
            pygame.draw.polygon(screen, (255, 255, 255), [
                (bubble_x, bubble_y + bubble_height // 2),
                (bubble_x - 12, bubble_y + bubble_height // 2 + 8),
                (bubble_x, bubble_y + bubble_height // 2 + 16)
            ])
            pygame.draw.polygon(screen, (0, 0, 0), [
                (bubble_x, bubble_y + bubble_height // 2),
                (bubble_x - 12, bubble_y + bubble_height // 2 + 8),
                (bubble_x, bubble_y + bubble_height // 2 + 16)
            ], 2)
        else:
            show_bubble = False

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
