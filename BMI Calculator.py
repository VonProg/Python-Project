# BMI Calculator

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.2f}")

# Optional: BMI Category
if bmi < 18.5:
    print("You're underweight.")
elif bmi < 24.9:
    print("You have a normal weight.")
elif bmi < 29.9:
    print("You're overweight.")
else:
    print("You're obese.")
