import pandas as pd
import random
import time

def create_random_dataframe(num_rows):
    data = []
    for i in range(num_rows):
        value1 = random.randint(1, 100)
        value2 = random.randint(1, 100)
        data.append({'A': value1, 'B': value2})
        print(f"Row {i+1}: A={value1}, B={value2}")
        time.sleep(0.5)  
    df = pd.DataFrame(data)
    print("DataFrame created:")
    print(df)
    return df

num_rows = int(input("How many rows do you want in the DataFrame? "))
created = 0

while True:
    print(f"Creating DataFrame with {num_rows} rows...")
    df = create_random_dataframe(num_rows)
    created += 1
    time.sleep(1)
    if created >= 2:
        print("Created DataFrame twice!")
        break
    else:
        print("Creating again...")

index = 0
while index < num_rows:
    print(f"Index: {index}")
    index += 1
    if index > 3 and (index < num_rows or not(index == 5)):
        print(f"Special condition at index {index}")
else:
    print("Finished while-else loop.")


if not df.empty:
    if (df['A'].mean() > 50 and df['B'].mean() > 50) or (df['A'].max() > 90):
        print("High values detected in DataFrame!")
    else:
        print("Values are moderate.")
else:
    print("DataFrame is empty.")
