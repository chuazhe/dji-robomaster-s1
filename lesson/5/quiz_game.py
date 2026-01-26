import pygame
import sys
import random

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
pygame.mixer.init()

pass_sound = pygame.mixer.Sound('pass.mp3')
fail_sound = pygame.mixer.Sound('fail.mp3')
pass_sound.set_volume(0.3)
fail_sound.set_volume(0.3)

WIDTH, HEIGHT = 1024, 640
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 120, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

FONT = pygame.font.SysFont('arial', 28)
SMALL_FONT = pygame.font.SysFont('arial', 22)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Variable Type Quiz')


questions = [
    ("Which of these is an integer?", ["42", '"hello"', '3.14', 'True'], 0),
    ("Which of these is a string?", ['42', '3.14', 'True', '"hello"'], 3),
    ("Which of these is a float?", ['42', '3.14', '"3.14"', 'True'], 1),
    ("Which of these is a boolean?", ['42', '3.14', 'True', '"False"'], 2),
    ("Which of these is NOT a string?", ['"42"', '"hello"', '3.14', '"True"'], 2),
    ("Which of these is a float?", ['3', '3.0', '"3.0"', 'False'], 1),
    ("Which of these is a string?", ['True', '3.14', '"Python"', '42'], 2),
    ("Which of these is a boolean?", ['"True"', 'False', '0', '1'], 1),
    ("Which of these is an integer?", ['3.14', '"42"', '42', 'False'], 2),
    ("Which of these is a string?", ['"123"', '123', '12.3', 'True'], 0),
    ("Which of these is a float?", ['"3.14"', '3.14', '3', 'False'], 1),
    ("Which of these is a boolean?", ['"False"', '0', 'True', '"0"'], 2),
    ("Which of these is an integer?", ['"0"', '0', '0.0', 'False'], 1),
    ("Which of these is NOT a float?", ['3.0', '0.0', '"3.0"', '2.5'], 2),
    ("Which of these is a string?", ['"False"', 'False', '0', '0.0'], 0),
    ("Which of these is a boolean?", ['1', '0', 'False', '"True"'], 2),
    ("Which of these is NOT an integer?", ['42', '0', '3.14', '-1'], 2),
    ("Which variable name is valid in Python?", ['my-var', 'my_var', '2var', 'var!'], 1),
    ("Which variable name is invalid in Python?", ['_var', 'var2', 'var$', 'var_2'], 2),
    ("Which of these is a good variable name for storing age?", ['a', 'num', 'age', '1age'], 2),
    ("Which is a good variable name for storing temperature?", ['t', 'temp', 'temperature', '1temperature'], 2),
    ("Which is a good variable name for storing a student name?", ['student', 'studentName', 'name', '1student'], 1),
    ("Which is a good variable name for storing total price?", ['total', 'price', 'total_price', '1price'], 2),
    ("Which variable name is invalid in Python?", ['myVar', 'var_1', 'var-1', '_var'], 2),
    ("Which variable name follows Python naming conventions?", ['MyVar', 'my_var', 'my-var', 'myVar!'], 1),
    ("Which of these variable names is not allowed?", ['_myvar', 'my var', 'myvar2', 'var_'], 1),
    ("Which variable name is invalid in Python?", ['var$', 'var_2', 'varTwo', '_2var'], 0),
    ("What is the length of the string 'Python'?", ['5', '6', '7', '0'], 1),
    ("What is the length of the string 'a_p_p_l_e'?", ['8', '9', '10', '11'], 1),
    ("What is the length of the string 'orange '?", ['6', '7', '8', '9'], 1),
]

random.shuffle(questions)

score = 0
q_index = 0
selected = -1
show_result = False
sound_played = False

clock = pygame.time.Clock()

while True:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not show_result:
            mx, my = pygame.mouse.get_pos()
            for i in range(4):
                rect_width = WIDTH * 0.39
                rect_height = HEIGHT * 0.078
                rect_x = (WIDTH - rect_width) // 2
                rect_y = int(HEIGHT * 0.1875 + i * (HEIGHT * 0.09375))
                if rect_x < mx < rect_x + rect_width and rect_y < my < rect_y + rect_height:
                    selected = i
                    if selected == questions[q_index][2]:
                        score += 1
                    show_result = True
                    sound_played = False
        if event.type == pygame.KEYDOWN and show_result:
            if event.key == pygame.K_SPACE:
                q_index += 1
                selected = -1
                show_result = False
                sound_played = False
                if q_index >= len(questions):
                    q_index = 0
                    score = 0
                    random.shuffle(questions)

    question, options, answer = questions[q_index]
    text = FONT.render(question, True, BLACK)
    text_x = (WIDTH - text.get_width()) // 2
    screen.blit(text, (text_x, 40))

    for i, opt in enumerate(options):
        color = BLUE if i == selected else BLACK
        rect_x = (WIDTH - 400) // 2
        rect_y = 120 + i*60
        pygame.draw.rect(screen, GREEN if show_result and i == answer else (RED if show_result and i == selected and i != answer else WHITE), (rect_x, rect_y, 400, 50))
        pygame.draw.rect(screen, BLACK, (rect_x, rect_y, 400, 50), 2)
        opt_text = SMALL_FONT.render(opt, True, color)
        opt_text_x = (WIDTH - opt_text.get_width()) // 2
        screen.blit(opt_text, (opt_text_x, rect_y + 15))

    if show_result:
        if not sound_played:
            if selected == answer:
                pass_sound.play()
            else:
                fail_sound.play()
            sound_played = True
        if selected == answer:
            result_text = FONT.render('Correct!', True, GREEN)
        else:
            result_text = FONT.render('Wrong!', True, RED)
        result_text_x = (WIDTH - result_text.get_width()) // 2
        screen.blit(result_text, (result_text_x, 420))
        next_text = SMALL_FONT.render('Press SPACE for next', True, BLACK)
        next_text_x = (WIDTH - next_text.get_width()) // 2
        screen.blit(next_text, (next_text_x, 390))
    else:
        info_text = SMALL_FONT.render(f'Score: {score}/{q_index}', True, BLACK)
        info_text_x = (WIDTH - info_text.get_width()) // 2
        screen.blit(info_text, (info_text_x, 10))

    pygame.display.flip()
    clock.tick(30)
