mport random
import time

# 1) Random number guessing game (1-30)
secret = random.randint(1, 30)
while True:
    guess = input("Guess a number between 1 and 30: ")
    if not guess.isdigit() or not (1 <= int(guess) <= 30):
        print("Invalid guess")
        continue
    guess = int(guess)
    if guess == secret:
        print("You got it!")
        break

# 2) Five random numbers between 10 and 99
nums = [random.randint(10, 99) for _ in range(5)]
print("Random numbers:", nums)
if all(n % 2 == 0 for n in nums):
    print("All even")
elif any(n % 7 == 0 for n in nums):
    print("Lucky seven!")
else:
    print("Try again")

# 3) Wait for user input between 2 and 6 seconds
num = input("Enter a number from 2 to 6: ")
if num.isdigit() and 2 <= int(num) <= 6:
    print("Processing...")
    time.sleep(int(num))
    print("Finished")
else:
    print("Error: out of range")

# 4) Guessing game with hints (1-50)
secret = random.randint(1, 50)
while True:
    guess = input("Guess a number between 1 and 50: ")
    if not guess.isdigit() or not (1 <= int(guess) <= 50):
        print("Guess out of bounds")
        continue
    guess = int(guess)
    if guess == secret:
        print("Congratulations!")
        break
    elif abs(guess - secret) <= 5:
        print("Very close")
    elif abs(guess - secret) > 20:
        print("Way off")

# 5) Quiz game with while-else (1-25, 5 attempts)
secret = random.randint(1, 25)
attempts = 0
while attempts < 5:
    guess = input("Guess a number between 1 and 25: ")
    if not guess.isdigit() or not (1 <= int(guess) <= 25):
        print("Out of range")
        continue
    guess = int(guess)
    attempts += 1
    if guess == secret:
        print("Correct, you win!")
        break
    elif guess > secret:
        print("Lower")
    else:
        print("Higher")
else:
    print("Better luck next time!")

# 6) Create a list of the numbers 1 to 5 and print it
numbers = [1, 2, 3, 4, 5]
print(numbers)

# 7) Add the number 10 to the end of a list
numbers.append(10)
print(numbers)

# 8) Print the first element of a list
print(numbers[0])

# 9) Change the value of the second element in a list to 100
numbers[1] = 100
print(numbers)

# 10) Remove the last element from the list
numbers.pop()
print(numbers)
