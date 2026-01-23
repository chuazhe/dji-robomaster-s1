import matplotlib.pyplot as plt
import time
import random

def plot_random_points(num_points):
    x = []
    y = []
    for i in range(num_points):
        x_val = random.randint(0, 100)
        y_val = random.randint(0, 100)
        x.append(x_val)
        y.append(y_val)
        print(f"Point {i+1}: ({x_val}, {y_val})")
        time.sleep(0.5)  
    plt.scatter(x, y)
    plt.title(f"{num_points} Random Points")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

num_points = int(input("How many points do you want to plot? "))

drawn = 0

while True:
    print(f"Plotting {num_points} points...")
    plot_random_points(num_points)
    drawn += 1
    time.sleep(1)
    if drawn >= 2:
        print("Plotted twice!")
        break
    else:
        print("Plotting again...")

distance = 0
while distance < num_points:
    print(f"Distance: {distance}")
    distance += 1
    if distance > 3 and (distance < num_points or not(distance == 5)):
        print(f"Special condition at distance {distance}")
else:
    print("Finished while-else loop.")
