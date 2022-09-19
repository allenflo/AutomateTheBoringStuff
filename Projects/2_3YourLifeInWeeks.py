# This program will tell you how many weeks you have left to live 
# assuming a 90 uear life span

age = input("What is your current age? ")
yearsLeft = 90 - int(age)
daysLeft = 365 * int(yearsLeft)
weeksLeft = yearsLeft * 52
monthsLeft = yearsLeft * 12

print(f"You have {yearsLeft} years left to live")
print(f"You have {monthsLeft} months left to live")
print(f"You have {weeksLeft} weeks left to live")
print(f"You have {daysLeft} days left to live")


