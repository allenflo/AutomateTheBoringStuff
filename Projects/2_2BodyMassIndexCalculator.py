#Body Mass Index Calculator




weight = input("Please enter your weight in kg: ")
height = input("Please enter your height in  meters: ")

bmi = float(weight) / (float(height) * float(height))
finalbmi = int(bmi)

print("Your BMI is " + str(finalbmi))



