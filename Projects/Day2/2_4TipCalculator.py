#Tip calulator will
#Welcome You
#Ask for total bill amount
#Ask what percentage tip to give?
#Ask how may people to split the bill
#Tell how much each person should pay

print("Welcome to the Tip Calculator")

total = float(input("What was the total bill? $"))
percentTip = int(input("What percent of tip would you like to give? %"))
split = int(input("How many peole to split the bill? "))


#Calculate tip amount
tip = (percentTip / 100) * total
tip = round(tip, 2)


#Calulate total bill amount
totalBill = total + tip

#Split total bill
each = totalBill / split

#Round to 2 decimals

eachPay = round(each, 2)


#Printing totals with Fstrings allowing for formating to 2 decimals for currency.
print(f"The tip amount to add to the bill is {tip:.2f}")
print(f"The total bill including tip is: ${totalBill:.2f}")
print(f"Each of the {split} guests should pay:  ${eachPay:.2f}")