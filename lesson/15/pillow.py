from PIL import Image, ImageDraw
import random
import time



def create_image_with_rectangles(num_rects):
    img = Image.new('RGB', (400, 400), color='white')
    draw = ImageDraw.Draw(img)
    for i in range(num_rects):
        x1 = random.randint(0, 300)
        y1 = random.randint(0, 300)
        x2 = x1 + random.randint(20, 100)
        y2 = y1 + random.randint(20, 100)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        draw.rectangle([x1, y1, x2, y2], fill=color)
        print(f"Rectangle {i + 1}: ({x1},{y1}) to ({x2},{y2}), color={color}")
        time.sleep(0.5)  
    img.show()
    return img


num_rects = int(input("How many rectangles do you want to draw? "))
created = 0

while True:
    print(f"Creating image with {num_rects} rectangles...")
    img = create_image_with_rectangles(num_rects)
    created += 1
    time.sleep(1)
    if created >= 2:
        print("Created image twice!")
        break
    else:
        print("Creating again...")

index = 0
while index < num_rects:
    print(f"Index: {index}")
    index += 1
    if index > 3 and (index < num_rects or not (index == 5)):
        print(f"Special condition at index {index}")
else:
    print("Finished while-else loop.")


if img:
    colors = img.getcolors(maxcolors=10000)
    if colors and (len(colors) > 10 and colors[0][1] != (255, 255, 255)) or (colors and colors[-1][0] > 1):
        print("Image has a variety of colors!")
    else:
        print("Image is mostly one color.")
else:
    print("No image created.")
