#Body Mass Index Calculator

# Choose Metric or Imperial

units = input("Press 1 for Metric or Press 2 for Imperial: ")


# Metric
if int(units) == 1:
    weightkg = input("Please enter your weight in kg: ")
    heightkg = input("Please enter your height in  meters: ")
    bmi = float(weightkg) / (float(heightkg) ** 2)
    finalbmi = int(bmi)
    print("Your BMI is " + str(finalbmi))
    
#Imperial
else:
    weightlb = input("Please enter your weight in lbs: ")
    heightin = input("Please enter your height in inches: ")
    bmi = (float(weightlb) * 703) / (float(heightin) ** 2)
    finalbmi = int(bmi)
    print("Your BMI is " + str(finalbmi))
    