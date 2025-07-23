print("=== Python Calculator ===")

# Show the menu
print("Select an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Floor Division (//)")
print("6. Modulus (%)")
print("7. Exponentiation (**)\n")

# Get the user's choice
choice = input("Enter the number of your choice (1-7): ")

# Ask for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform the operation
if choice == "1":
    result = num1 + num2
    operator = "+"
elif choice == "2":
    result = num1 - num2
    operator = "-"
elif choice == "3":
    result = num1 * num2
    operator = "*"
elif choice == "4":
    if num2 != 0:
        result = num1 / num2
        operator = "/"
    else:
        result = "Error! Division by zero."
        operator = "/"
elif choice == "5":
    if num2 != 0:
        result = num1 // num2
        operator = "//"
    else:
        result = "Error! Division by zero."
        operator = "//"
elif choice == "6":
    result = num1 % num2
    operator = "%"
elif choice == "7":
    result = num1 ** num2
    operator = "**"
else:
    result = "Invalid operation selected."
    operator = "?"

# Result
print("\n=== Result ===")
if isinstance(result, str):
    print(result)
else:
    print(f"{num1} {operator} {num2} = {result}")
