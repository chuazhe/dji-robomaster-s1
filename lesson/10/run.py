import os
import random

names = ["apple", "orange", "strawberry"]
output_dir = "output_files"
os.makedirs(output_dir, exist_ok=True)

for i in range(1, 1001):
    name = random.choice(names)
    filename = f"{name}_{i}.txt"
    filepath = os.path.join(output_dir, filename)
    with open(filepath, "w") as f:
        f.write(f"This is file {filename}\n")
