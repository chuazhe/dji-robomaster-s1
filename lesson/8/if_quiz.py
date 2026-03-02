import pygame
import sys
import random

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 700, 500    
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('If-Else Quiz Game')

font = pygame.font.SysFont(None, 32)
clock = pygame.time.Clock()

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
random.shuffle(questions)

score = 0
current = 0
show_result = False
result_text = ""

# Button rendering helper
def draw_button(text, rect, color, text_color=(0,0,0)):
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, (0,0,0), rect, 2)
    label = font.render(text, True, text_color)
    label_rect = label.get_rect(center=rect.center)
    screen.blit(label, label_rect)

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
        if event.type == pygame.MOUSEBUTTONDOWN and not show_result and current < len(questions):
            mouse_pos = pygame.mouse.get_pos()
            # Get answer options from question string
            qtext = questions[current][0]
            # Try to extract the two answer options from the question string
            import re
            match = re.findall(r"print\('([^']+)'\)", qtext)
            if len(match) == 2:
                opt1, opt2 = match
            else:
                # fallback: use correct answer and a dummy
                opt1 = questions[current][1]
                opt2 = "Other"
            btn1_rect = pygame.Rect(120, 260, 180, 60)
            btn2_rect = pygame.Rect(400, 260, 180, 60)
            if btn1_rect.collidepoint(mouse_pos):
                answer = opt1
            elif btn2_rect.collidepoint(mouse_pos):
                answer = opt2
            else:
                answer = ''
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
        # Draw answer buttons
        import re
        match = re.findall(r"print\('([^']+)'\)", questions[current][0])
        if len(match) == 2:
            opt1, opt2 = match
        else:
            opt1 = questions[current][1]
            opt2 = "Other"
        btn1_rect = pygame.Rect(120, 260, 180, 60)
        btn2_rect = pygame.Rect(400, 260, 180, 60)
        def draw_button(text, rect, color, text_color=(0,0,0)):
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, (0,0,0), rect, 2)
            label = font.render(text, True, text_color)
            label_rect = label.get_rect(center=rect.center)
            screen.blit(label, label_rect)
        draw_button(opt1, btn1_rect, (200,220,255))
        draw_button(opt2, btn2_rect, (200,220,255))
        hint = font.render("Click a button to answer", True, (80,80,80))
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
