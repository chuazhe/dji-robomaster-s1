import pyautogui
import random
import time



def move_mouse_randomly(num_moves):
    screen_width, screen_height = pyautogui.size()
    for i in range(num_moves):
        x = random.randint(0, screen_width - 1)
        y = random.randint(0, screen_height - 1)
        print(f"Move {i+1}: Moving mouse to ({x}, {y})")
        pyautogui.moveTo(x, y, duration=0.5)
        time.sleep(0.5)  

num_moves = int(input("How many mouse moves do you want? "))
moved = 0

while True:
    print(f"Moving mouse {num_moves} times...")
    move_mouse_randomly(num_moves)
    moved += 1
    time.sleep(1)
    if moved >= 2:
        print("Moved mouse twice!")
        break
    else:
        print("Moving again...")

index = 0
while index < num_moves:
    print(f"Index: {index}")
    index += 1
    if index > 3 and (index < num_moves or not(index == 5)):
        print(f"Special condition at index {index}")
else:
    print("Finished while-else loop.")

if num_moves > 0:
    rand_index = random.randint(0, num_moves-1)
    if (rand_index % 2 == 0 and num_moves > 5) or (rand_index == num_moves-1):
        print(f"Random index {rand_index} meets special condition!")
    else:
        print("Random index is ordinary.")
else:
    print("No moves requested.")
