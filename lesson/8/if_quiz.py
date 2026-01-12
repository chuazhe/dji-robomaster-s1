import pygame
import sys

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 700, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('If-Else Quiz Game')

font = pygame.font.SysFont(None, 32)
clock = pygame.time.Clock()

# Simple if-else questions
questions = [
    ("if 3 > 2: print('A') else: print('B')", "A"),
    ("if 5 == 10: print('X') else: print('Y')", "Y"),
    ("if 7 < 1: print('Yes') else: print('No')", "No"),
    ("if 2 != 2: print('True') else: print('False')", "False"),
    ("if 4 >= 4: print('OK') else: print('Not OK')", "OK"),
    ("if 10 <= 5: print('Low') else: print('High')", "High"),
    ("if 0: print('Zero') else: print('Nonzero')", "Nonzero"),
    ("if 1: print('Yes') else: print('No')", "Yes"),
    ("if 8 % 2 == 0: print('Even') else: print('Odd')", "Even"),
    ("if 9 % 2 == 0: print('Even') else: print('Odd')", "Odd"),
    ("if True: print('T') else: print('F')", "T"),
    ("if False: print('T') else: print('F')", "F"),
    ("if 3 == 3 and 2 == 2: print('Yes') else: print('No')", "Yes"),
    ("if 3 == 3 or 2 == 3: print('Yes') else: print('No')", "Yes"),
    ("if not 0: print('A') else: print('B')", "A"),
    ("if not 1: print('A') else: print('B')", "B"),
    ("if 2 > 1 and 3 < 4: print('Good') else: print('Bad')", "Good"),
    ("if 2 > 3 or 3 < 2: print('No') else: print('Yes')", "Yes"),
    ("if 5 == 5 and 0: print('A') else: print('B')", "B"),
    ("if 0 or 1: print('A') else: print('B')", "A"),
    ("if 0 and 1: print('A') else: print('B')", "B"),
    ("if 10 > 5 and 2 == 2: print('Win') else: print('Lose')", "Win"),
    ("if 10 < 5 or 2 != 2: print('Win') else: print('Lose')", "Lose"),
    ("if 3 > 2 and 1 > 2: print('A') else: print('B')", "B"),
    ("if 3 > 2 or 1 > 2: print('A') else: print('B')", "A"),
    ("if not (2 > 1): print('X') else: print('Y')", "Y"),
    ("if not (2 < 1): print('X') else: print('Y')", "X"),
    ("if 2 == 2 and not 0: print('Yes') else: print('No')", "Yes"),
    ("if 2 == 2 and not 1: print('Yes') else: print('No')", "No"),
]

score = 0
current = 0
show_result = False
result_text = ""

# Load sounds
try:
    pass_sound = pygame.mixer.Sound("pass.mp3")
except Exception:
    pass_sound = None
try:
    fail_sound = pygame.mixer.Sound("fail.mp3")
except Exception:
    fail_sound = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and not show_result:
            if event.key == pygame.K_a:
                answer = "A"
            elif event.key == pygame.K_b:
                answer = "B"
            elif event.key == pygame.K_x:
                answer = "X"
            elif event.key == pygame.K_y:
                answer = "Y"
            elif event.key == pygame.K_n:
                answer = "No"
            elif event.key == pygame.K_t:
                answer = "True"
            elif event.key == pygame.K_f:
                answer = "False"
            elif event.key == pygame.K_o:
                answer = "OK"
            elif event.key == pygame.K_s:
                answer = "Not OK"
            else:
                answer = ""
            if answer:
                correct = questions[current][1]
                if answer == correct:
                    score += 1
                    result_text = "Correct!"
                    if pass_sound:
                        pass_sound.play()
                else:
                    result_text = f"Wrong! Answer: {correct}"
                    if fail_sound:
                        fail_sound.play()
                show_result = True
                result_timer = pygame.time.get_ticks()

    if show_result and pygame.time.get_ticks() - result_timer > 1500:
        show_result = False
        current += 1
        if current >= len(questions):
            running = False

    screen.fill((240, 240, 255))
    if current < len(questions):
        qsurf = font.render(f"Q{current+1}: {questions[current][0]}", True, (0,0,0))
        screen.blit(qsurf, (30, 80))
        hint = font.render("Type your answer key (A/B/X/Y/N/T/F/O/S)", True, (80,80,80))
        screen.blit(hint, (30, 120))
        score_surf = font.render(f"Score: {score}", True, (0, 100, 0))
        screen.blit(score_surf, (30, 30))
        if show_result:
            res = font.render(result_text, True, (0,0,200) if 'Correct' in result_text else (200,0,0))
            screen.blit(res, (30, 170))
    else:
        done = font.render(f"Quiz Over! Final Score: {score}/{len(questions)}", True, (0,0,0))
        screen.blit(done, (30, 120))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
