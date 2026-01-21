import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("While-Else Example")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Window closed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("ESC pressed, exiting loop early.")
                break
    else:
        # This else runs if the while loop wasn't broken by ESC
        screen.fill((0, 128, 255))
        pygame.display.flip()
        continue
    break
else:
    print("Window closed normally (not with ESC).")

pygame.quit()
sys.exit()
