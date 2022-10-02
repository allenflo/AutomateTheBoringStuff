# This program will allow you to enter a number and the system will tell you
# whether it is even or odd
print("Welcome to the Even/Odd calculator.")
number = int(input("Please type a number"))
answer = number % 2

if answer == 0:
    print(f"{number} is a EVEN number")

else:
    print(f"{number} is an ODD number")

