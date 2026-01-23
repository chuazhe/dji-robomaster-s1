import turtle
import time
import random


def draw_square(size):
    colors = ['red', 'green', 'blue', 'yellow', 'purple']
    color = random.choice(colors)
    turtle.color(color)
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)


num_squares = int(input("How many squares do you want to draw? "))


drawn = 0


while True:
    
    size = random.randint(20, 100)
    print(f"Drawing square of size {size}")
    draw_square(size)
    drawn += 1
    time.sleep(1)  

    
    if drawn >= num_squares:
        print("All squares drawn!")
        break
    else:
        print(f"{num_squares - drawn} squares left.")


distance = 0
while distance < 200:
    turtle.forward(20)
    distance += 20
    
    if distance > 100 and (distance < 180 or not(distance == 160)):
        print(f"Distance is now {distance}, special condition met!")
else:
    print("Turtle reached the edge.")

turtle.done()
