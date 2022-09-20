#This program will allow you to order a pizza and select whether or not you want to add toppings

print("Welcome to Python Pizza!!!!!")
size = input("What size pizza would you like?   S, M, or L ")
pepperoni = input("Do you want pepperoni? Y or N ")
extraCheese = input("Do you want extra cheese? Y or N ")


bill = float(0)

if size == "S":
    bill = 15

elif size == "M":
    bill = 20

else:
    bill = 25

if pepperoni == "Y":
    if size == "S":
        bill += 2
    
    else:
        bill += 3

else:
    pass

if extraCheese == "Y":
    bill += 1

else:
    pass

print(f"Your final bill is:  ${bill:.2f}")





    



