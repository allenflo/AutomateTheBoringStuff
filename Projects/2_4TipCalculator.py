#Tip calulator will
#Welcome You
#Ask for total bill amount
#Ask what percentage tip to give?
#Ask how may people to split the bill
#Tell how much each person should pay

print("Welcome to the Tip Calculator")

print("Wecome to the tip calculator")
total = input("What was the total bill? $")
percentTip = input("What percent of tip would you like to give? %")
split = input("How many peole to split the bill? ")


#Calculate tip amount
tip = (int(percentTip) / 100) * float(total)


#Calulate total bill amount
totalBill = total + float(tip)

#Split total bill
each = totalBill / int(split)

#Round to 2 decimals

eachPay = float(round(each, 2))

print(f"Each person should pay:  ${eachPay}")