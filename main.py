number = 12
if number % 2 == 1:
    print("Odd")
else:
    print("Even")


# Improved BMI (Body Mass Index)
weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))
bmi = weight / (height ** 2)

if bmi < 18.5:
    status = "Underweight"
elif bmi < 25:
    status = "Normal"
elif bmi < 30:
    status = "Overweight"
elif bmi < 43: 
    status = "Obese"
else:
    status = "Obese Class III"

print(f'Your BMI is {round(bmi, 1)} "{status}"')



# operators: and, or, not
if height >= 100 and weight >= 100:
    print("Height and Weight are more or equal to 100")
elif height >= 100 or weight >= 100:
    print("Height or Weight is more or equal to 100")
if height < 100 and weight < 100: # using not for more/less comparisons is the same as flipping (e.g. ">=" flips to "<")
    print("Neither Height, nor Weight are more or equal to 100")
elif height < 100 or weight < 100:
    print("Height or Width is smaller than 100")