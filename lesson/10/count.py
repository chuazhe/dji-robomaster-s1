import os

folder = "output_files"  # Change this to your target folder
count = 0

for filename in os.listdir(folder):
    if "apple" in filename:
        count += 1

print(f"Number of files starting with 'apple': {count}")
