w = float(input("Enter your weight in kg: "))
h = float(input("Enter your height in cm: "))
bmi = w/(h/100)**2
print("Your BMI is ", bmi)
if bmi <= 18.4:
    print("You are Underweight.")
elif bmi <= 24.9:
    print("You are healthy.")
elif bmi <= 29.9:
    print("You are Overwight.")
elif bmi <= 34.9:
    print("You are Severely Overwight.")
elif bmi <= 39.9:
    print("You are Obese.")
else:
    print("You are Severly Obese")