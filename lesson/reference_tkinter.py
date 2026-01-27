import tkinter as tk
from tkinter import messagebox

def on_click(shape):
    if shape == "Rectangle":
        print("Rectangle Action")
    elif shape == "Square":
        print("Square Action")
    else:
        print("Circle Action")

root = tk.Tk()
root.title("Shape Buttons")
root.geometry("400x200")

canvas = tk.Canvas(root, width=400, height=200)
canvas.pack()




rect_btn = tk.Button(root, text="Rectangle", command=lambda: on_click("Rectangle"))
canvas.create_rectangle(30, 40, 130, 100, fill="lightblue", outline="black")
canvas.create_window(80, 70, window=rect_btn)


square_x = 190
square_y = 40
square_size = 60
canvas.create_rectangle(square_x, square_y, square_x+square_size, square_y+square_size, fill="pink", outline="black")
square_btn = tk.Button(root, text="Square", command=lambda: on_click("Square"))
canvas.create_window(square_x+square_size//2, square_y+square_size//2, window=square_btn)


circle_cx = 320
circle_cy = 70
circle_r = 35
circle_btn = tk.Button(root, text="Circle", command=lambda: on_click("Circle"))
canvas.create_oval(circle_cx-circle_r, circle_cy-circle_r, circle_cx+circle_r, circle_cy+circle_r, fill="yellow", outline="black")
canvas.create_window(circle_cx, circle_cy, window=circle_btn)

root.mainloop()
