#Body Mass Index Calculator
#Version 2.0 will tell you the interperetation of their number

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



#Elif statements could cascade down without having to use and statements but....
#wanted to be more specific.

if finalbmi < 18.5:
    print("Your BMI indicates that you are Underweight")

elif finalbmi > 25 and finalbmi <30: 
    print("Your BMI indicates that you are Normal Weight")

elif finalbmi > 30 and finalbmi <35:
    print("Your BMI indicates that you are Overweight")

elif finalbmi > 35:
    print("Your BMI indicates that you are Obese")





    
