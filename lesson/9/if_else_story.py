import pygame
import sys
import random

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('If-Else Story Quiz')

font = pygame.font.SysFont(None, 32)
big_font = pygame.font.SysFont(None, 28, bold=True)
clock = pygame.time.Clock()


questions = [
    ("You see a fork in the road. If you go left, you find a river. If you go right, you find a mountain. If direction == 'left': print('River') else: print('Mountain')", "River"),
    ("You have 5 apples. If you eat more than 3, you feel full. If apples_eaten > 3: print('Full') else: print('Hungry')", "Full"),
    ("A dragon blocks your path. If you have a sword, you fight. If not, you run. If has_sword: print('Fight') else: print('Run')", "Fight"),
    ("You find a locked door. If you have a key, you open it. If not, you search for another way. If has_key: print('Open') else: print('Search')", "Open"),
    ("It starts to rain. If you have an umbrella, you stay dry. If not, you get wet. If has_umbrella: print('Dry') else: print('Wet')", "Dry"),
    ("You meet a wise old man. If you ask for advice, he helps you. If not, you continue alone. If ask_advice: print('Helped') else: print('Alone')", "Helped"),
    ("You find a treasure chest. If you open it, you get gold. If not, you walk away. If open_chest: print('Gold') else: print('Nothing')", "Gold"),
    ("You are tired. If you rest, you recover energy. If not, you feel weak. If rest: print('Recovered') else: print('Weak')", "Recovered"),
    ("You see a bridge. If you cross it, you reach a village. If not, you stay in the forest. If cross_bridge: print('Village') else: print('Forest')", "Village"),
    ("You hear a noise at night. If you investigate, you find a lost puppy. If not, you miss it. If investigate: print('Puppy') else: print('Missed')", "Puppy"),
    ("You are hungry. If you cook food, you eat well. If not, you stay hungry. If cook_food: print('Eat') else: print('Hungry')", "Eat"),
    ("You see a boat. If you board it, you sail to an island. If not, you stay on shore. If board_boat: print('Island') else: print('Shore')", "Island"),
    ("You find a map. If you read it, you find treasure. If not, you get lost. If read_map: print('Treasure') else: print('Lost')", "Treasure"),
    ("You are cold. If you light a fire, you get warm. If not, you shiver. If light_fire: print('Warm') else: print('Shiver')", "Warm"),
    ("You see a cave. If you enter, you find shelter. If not, you stay outside. If enter_cave: print('Shelter') else: print('Outside')", "Shelter"),
]
random.shuffle(questions)

score = 0
current = 0
show_result = False
result_text = ""


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
            user_input = ''
            if event.key == pygame.K_r:
                user_input = "River"
            elif event.key == pygame.K_m:
                user_input = "Mountain"
            elif event.key == pygame.K_f:
                user_input = "Full"
            elif event.key == pygame.K_h:
                user_input = "Hungry"
            elif event.key == pygame.K_g:
                user_input = "Gold"
            elif event.key == pygame.K_n:
                user_input = "Nothing"
            elif event.key == pygame.K_o:
                user_input = "Open"
            elif event.key == pygame.K_s:
                user_input = "Search"
            elif event.key == pygame.K_d:
                user_input = "Dry"
            elif event.key == pygame.K_w:
                user_input = "Wet"
            elif event.key == pygame.K_v:
                user_input = "Village"
            elif event.key == pygame.K_f:
                user_input = "Forest"
            elif event.key == pygame.K_p:
                user_input = "Puppy"
            elif event.key == pygame.K_l:
                user_input = "Lost"
            elif event.key == pygame.K_t:
                user_input = "Treasure"
            elif event.key == pygame.K_e:
                user_input = "Eat"
            elif event.key == pygame.K_i:
                user_input = "Island"
            elif event.key == pygame.K_b:
                user_input = "Shore"
            elif event.key == pygame.K_a:
                user_input = "Alone"
            elif event.key == pygame.K_c:
                user_input = "Shelter"
            elif event.key == pygame.K_u:
                user_input = "Shiver"
            elif event.key == pygame.K_k:
                user_input = "Weak"
            elif event.key == pygame.K_y:
                user_input = "Helped"
            elif event.key == pygame.K_r:
                user_input = "Recovered"
            elif event.key == pygame.K_f:
                user_input = "Fight"
            elif event.key == pygame.K_u:
                user_input = "Run"
            elif event.key == pygame.K_o:
                user_input = "Outside"
            if user_input:
                correct = questions[current][1]
                if user_input == correct:
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
        # Wrap question text for better readability
        import textwrap
        qtext = f"Q{current+1}: {questions[current][0]}"
        wrapped = textwrap.wrap(qtext, width=60)
        y = 80
        for line in wrapped:
            qsurf = big_font.render(line, True, (0,0,0))
            screen.blit(qsurf, (30, y))
            y += 36
        hint = font.render("Type the answer's first letter (see story)", True, (80,80,80))
        screen.blit(hint, (30, y + 10))
        score_surf = font.render(f"Score: {score}", True, (0, 100, 0))
        screen.blit(score_surf, (30, 30))
        if show_result:
            res = font.render(result_text, True, (0,0,200) if 'Correct' in result_text else (200,0,0))
            screen.blit(res, (30, y + 50))
    else:
        done = font.render(f"Quiz Over! Final Score: {score}/{len(questions)}", True, (0,0,0))
        screen.blit(done, (30, 120))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
