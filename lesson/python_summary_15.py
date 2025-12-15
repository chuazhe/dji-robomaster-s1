# Print "Welcome!" and a random number between 1 and 10.
import random
print("Welcome!")
print(random.randint(1, 10))

# Store "Python" in a variable, print its length, and print "Short" if the length is less than 6, else print "Long".
word = "Python"
print(len(word))
if len(word) < 6:
    print("Short")
else:
    print("Long")

# Print "Start", then print numbers from 1 to 5 using a while loop, then print "End".
print("Start")
i = 1
while i <= 5:
    print(i)
    i += 1
print("End")

# Print "Counting down...", then use a while loop to print 3, 2, 1, then print "Blast off!" using while-else.
print("Counting down...")
n = 3
while n > 0:
    print(n)
    n -= 1
else:
    print("Blast off!")

# Print "Checking number...", store a random number between -10 and 10 in x, and use nested if to print "Positive", "Negative", or "Zero".
import random
print("Checking number...")
x = random.randint(-10, 10)
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")

# Print "Loop forever!", then print numbers from 1 to 3 in a forever loop and break after 3.
print("Loop forever!")
i = 1
while True:
    print(i)
    if i == 3:
        break
    i += 1
    
# Print "Logical test:", store two random numbers between 1 and 10 in a and b, and print "Both even" if both are even, else print "At least one is odd".
import random
print("Logical test:")
a = random.randint(1, 10)
b = random.randint(1, 10)
if a % 2 == 0 and b % 2 == 0:
    print("Both even")
else:
    print("At least one is odd")

# Print "OR test:", store three random numbers between 1 and 10 in x, y, z, and print "At least one is greater than 8" if any is greater than 8, else print "None greater than 8".
import random
print("OR test:")
x = random.randint(1, 10)
y = random.randint(1, 10)
z = random.randint(1, 10)
if x > 8 or y > 8 or z > 8:
    print("At least one is greater than 8")
else:
    print("None greater than 8")

# Print "NOT test:", store a random number between 1 and 10 in n, and print "Not 5" if n is not 5, else print "Is 5".
import random
print("NOT test:")
n = random.randint(1, 10)
if n != 5:
    print("Not 5")
else:
    print("Is 5")

# Print "Waiting test:", store a random number between 1 and 3 in t, print "Wait for t seconds...", wait t seconds, then print "Done".
import random, time
t = random.randint(1, 3)
print("Wait for", t, "seconds...")
time.sleep(t)
print("Done")

#  You are simulating a guessing game. Generate a random number between 1 and 20. Let the user guess until they get it right. If the guess is too high, print "Too high". If too low, print "Too low". When correct, print "Correct!" and exit.
import random
secret = random.randint(1, 20)
while True:
    guess = int(input("Guess the number (1-20): "))
    if guess == secret:
        print("Correct!")
        break
    elif guess > secret:
        print("Too high")
    else:
        print("Too low")

#  You are simulating a countdown timer. Ask the user for a number. Print "Countdown:", then print numbers from that number down to 1, each with a 1-second pause. When finished, print "Done!" using while-else.
import time
n = int(input("Enter countdown start: "))
print("Countdown:")
while n > 0:
    print(n)
    time.sleep(1)
    n -= 1
else:
    print("Done!")

# You are creating a login system with a forever loop. Ask the user for a username and password. If the username is not empty and the password is at least 8 characters and does not contain the username, print "Login successful" and exit. Otherwise, print "Login failed" and ask again. If the user types "exit" as the username, break the loop and print "Exited".
while True:
    username = input("Enter username: ")
    if username == "exit":
        print("Exited")
        break
    password = input("Enter password: ")
    if username and len(password) >= 8 and not username in password:
        print("Login successful")
        break
    else:
        print("Login failed")

# Ask the user for two numbers. If both numbers are negative, print "Both negative". Otherwise, print "At least one is negative or no negative".
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a < 0 and b < 0:
    print("Both negative")
else:
    print("At least one is negative or no negative")

# Ask the user for two numbers. If either number is zero, print "At least one is zero". Otherwise, print "Neither is zero".
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a == 0 or b == 0:
    print("At least one is zero")
else:
    print("Neither is zero")

# Ask the user for a number. If the number is not zero and is divisible by 3, print "Non-zero and divisible by 3". Otherwise, print "Does not meet criteria".
n = int(input("Enter a number: "))
if n != 0 and n % 3 == 0:
    print("Non-zero and divisible by 3")
else:
    print("Does not meet criteria")

# Ask the user for their age and country. If the age is at least 18 and (the country is "USA" or the country is "Canada"), print "Eligible for North America program". Otherwise, print "Not eligible".
age = int(input("Enter your age: "))
country = input("Enter your country: ")
if age >= 18 and (country == "USA" or country == "Canada"):
    print("Eligible for North America program")
else:
    print("Not eligible")

# Ask the user for three numbers. If all numbers are positive and at least one is greater than 100 or all numbers are even, print "Special set". Otherwise, print "Ordinary set"
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if (a > 0 and b > 0 and c > 0 and (a > 100 or b > 100 or c > 100)) or (a % 2 == 0 and b % 2 == 0 and c % 2 == 0):
    print("Special set")
else:
    print("Ordinary set")

# You are running a quiz game. Generate a random number between 1 and 50. Let the user guess until they get it right. If the guess is too high, print "Too high". If too low, print "Too low". When correct, print "You win!" and exit. If the user guesses wrong 5 times, print "Game over!" using while-else.
import random
secret = random.randint(1, 50)
attempts = 0
while attempts < 5:
    guess = int(input("Guess the number (1-50): "))
    attempts += 1
    if guess == secret:
        print("You win!")
        break
    elif guess > secret:
        print("Too high")
    else:
        print("Too low")
else:
    print("Game over!")

# You are running a treasure hunt game. Generate a random number between 1 and 100 as the treasure location. Let the user guess until they find the treasure. If the guess is within 5 of the treasure, print "Very close!". If the guess is exactly correct, print "You found the treasure!" and exit. If the guess is more than 20 away, print "Far away". Otherwise, print "Getting closer". If the user fails after 10 attempts, print "Game over!" using while-else.
import random
treasure = random.randint(1, 100)
attempts = 0
while attempts < 10:
    guess = int(input("Guess the treasure location (1-100): "))
    attempts += 1
    if guess == treasure:
        print("You found the treasure!")
        break
    elif abs(guess - treasure) <= 5:
        print("Very close!")
    elif abs(guess - treasure) > 20:
        print("Far away")
    else:
        print("Getting closer")
else:
    print("Game over!")
