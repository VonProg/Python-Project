# Even or Odd Checker

number = int(input("Enter a number: "))

if number == 0:
    print("That's zero!")
elif number < 0:
    print("Please enter a positive number.")
elif number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
