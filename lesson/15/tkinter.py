import tkinter as tk
import random
import time

def add_random_labels(num_labels):
    for i in range(num_labels):
        x = random.randint(0, 200)
        y = random.randint(0, 200)
        label = tk.Label(root, text=f"Label {i+1}: ({x}, {y})")
        label.place(x=x, y=y)
        print(f"Label {i+1}: ({x}, {y})")
        root.update()
        time.sleep(0.5)  

def forever_loop():
    global drawn
    while True:
        print(f"Adding {num_labels} labels...")
        add_random_labels(num_labels)
        drawn += 1
        time.sleep(1)
        if drawn >= 2:
            print("Added labels twice!")
            break
        else:
            print("Adding again...")

def while_else_demo():
    distance = 0
    while distance < num_labels:
        print(f"Distance: {distance}")
        distance += 1
        if distance > 3 and (distance < num_labels or not(distance == 5)):
            print(f"Special condition at distance {distance}")
    else:
        print("Finished while-else loop.")

root = tk.Tk()
root.geometry("400x400")

num_labels = int(input("How many labels do you want to add? "))
drawn = 0

forever_loop()
while_else_demo()

root.mainloop()
