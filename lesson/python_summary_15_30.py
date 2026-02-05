# Create a list of the first five positive integers and print it
first_five = [1, 2, 3, 4, 5]
print("2)", first_five)

# Add "orange" to the end of the list
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print("3)", fruits)

# Access the third element in the list
numbers = [10, 20, 30, 40, 50]
third_element = numbers[2]
print("4)", third_element)

# Find the length of a list
sample_list = [1, 2, 3, 4, 5]
length = len(sample_list)
print("5)", length)

# Remove the element "banana" from the list
fruits2 = ["apple", "banana", "cherry"]
fruits2.remove("banana")
print("6)", fruits2)

# Create a new list with only the odd numbers
numbers2 = [2, 5, 8, 3, 7]
odds = [x for x in numbers2 if x % 2 != 0]
print("7)", odds)

# Check if 10 exists in the list
a = [5, 10, 15, 20]
exists = 10 in a
print("8)", exists)

# Change "green" to "yellow" in the list
colors = ["red", "green", "blue"]
colors[1] = "yellow"
print("9)", colors)
