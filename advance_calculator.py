print("=== Advance Calculator ===")

# Defines function for each operators
def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return "Error! Division by zero." if y == 0 else x / y
def floor_divide(x, y): return "Error! Division by zero." if y == 0 else x // y
def modulus(x, y): return x % y
def exponentiate(x, y): return x ** y

# Main Calculator Loop
def calculator():
    while True:
        print("\nSelect operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Floor Division (//)")
        print("6. Modulus (%)")
        print("7. Exponentiation (**)")
        print("8. Exit")

        choice = input("Enter choice (1-8): ")

        if choice == '8':
            print("Goodbye!")
            break

        if choice in ('1', '2', '3', '4', '5', '6', '7'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numbers.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':
                print(f"{num1} // {num2} = {floor_divide(num1, num2)}")
            elif choice == '6':
                print(f"{num1} % {num2} = {modulus(num1, num2)}")
            elif choice == '7':
                print(f"{num1} ** {num2} = {exponentiate(num1, num2)}")
        else:
            print("Invalid Input! Please choose a number from 1 to 8.")


calculator()
