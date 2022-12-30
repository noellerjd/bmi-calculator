print("Welcome to the BMI Calculator.")

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

height_round = round(height,2)
weight_round = round(weight)
bmi = round(weight_round / (height_round * height_round))

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
