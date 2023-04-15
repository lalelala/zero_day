import math

height = int(input("What is your height in cm: "))
weight = int(input("What is your weight in kg: "))
bmi = math.ceil(weight/((height/100)**2))

print("Your BMI is" + bmi)

if bmi >= 35:
	print("You are exteremly obese")
elif bmi >= 34.9:
	print("You are obese")
elif bmi >= 29.9:
	print("You are over weight")
elif bmi >= 24.9:
	print("You are normal weight")
else:
	print("You are underweight")
