# Easy: Print each element in the list
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

# Easy: Create a list of the first 5 even numbers using a for loop
evens = []
for i in range(2, 12, 2):
    evens.append(i)
print(evens)

# Easy: Print each fruit in uppercase
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit.upper())

# Medium: Create a new list containing the squares of numbers from 1 to 10
squares = []
for i in range(1, 11):
    squares.append(i * i)
print(squares)

# Medium: Find the sum of all elements in nums
nums = [3, 7, 2, 9, 4]
total = 0
for n in nums:
    total += n
print(total)

# Medium: Reverse a list without using reverse()
data = [10, 20, 30, 40]
reversed_data = []
for i in range(len(data)-1, -1, -1):
    reversed_data.append(data[i])
print(reversed_data)

# Hard: Create a new list containing only the words that start with a vowel
words = ['apple', 'banana', 'orange', 'grape', 'umbrella']
vowels = ['a', 'e', 'i', 'o', 'u']
result = []
for word in words:
    if word[0].lower() in vowels:
        result.append(word)
print(result)

# Hard: Flatten a nested list
nested = [[1, 2], [3, 4], [5, 6]]
flat = []
for sublist in nested:
    for item in sublist:
        flat.append(item)
print(flat)
