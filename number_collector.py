# Get the first number.
try:
    number1 = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Defaulting to 0.")
    number1 = 0

# Get the second number.
try:
    number2 = int(input("Enter another number: "))
except ValueError:
    print("Invalid input. Defaulting to 0.")
    number2 = 0

# Get the third number.
try:
    number3 = int(input("Enter a third number: "))
except ValueError:
    print("Invalid input. Defaulting to 0.")
    number3 = 0

# Calculate the sum and average.
total = number1 + number2 + number3
average = total / 3

# Display the results.
print(f"\nYour numbers: {number1}, {number2}, {number3}")
print(f"Sum: {total}")
print(f"Average: {average:.2f}")

# The Error Handling Mindset

# 1. # Snippet 1
# 2.print(“the answer is: “ + 42)
# 3.

# Prediction:Type Error
# Error:Type Error
# Fix:print(“the answer is: “ + str(42))


# 1.# Snippet 2
# 2.favorite = input(“Favorite number: “)
# 3.result = favorite + 10
# 4.print(result)
# 5.

# Prediction:Value Error
# Error:Type Error
# Fix:favorite = input(“Favorite number: “)
# result = int(favorite) + 10
# print(result)


# 1.# Snippet 3
# 2.print(“Hello World)
# 3.

# Prediction:Name Error
# Error:Syntax Error
# Fix:print(“Hello World”)

# 1.# Snippet 4
# 2.age = int(“twenty-five”)
# 3

# Prediction:Value Error
# Error:Value Error
# Fix:age = 25


# 1.# Snippet 5 
# 2.print(username)
# 3.

# Prediction:Name Error
# Error:Name Error
# Fix:age = username = Tim
# print(username)