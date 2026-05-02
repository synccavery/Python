height = float(input("Enter you height in cm: "))
weight = float(input("Enter you weight in kg: "))

bmi = weight/ (height/100)**2
bmi = round(bmi,2)
print(f"Your BMI is {bmi}")

if bmi<= 18.4:
    print("You are underweight")
elif bmi<= 24.9:
    print("You are healthy")
elif bmi<= 29.9:
    print("You are overweight")
elif bmi<= 24.9:
    print("You are healthy")
elif bmi<= 39.9:
    print("You are obese")
else:
    print("You are severly obese")
