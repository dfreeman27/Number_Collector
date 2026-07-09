

try:
        number1 = float(input("Enter a number: "))
        number2 = float(input("Enter another number: "))
        number3 = float(input("Enter a third number: "))
except ValueError:
        print("Please enter valid numbers.")
else:
        total = number1 + number2 + number3
        print(f"The sum of the numbers is: {total}")
        print(f"The average of the numbers is: {total / 3}")





