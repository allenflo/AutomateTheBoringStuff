from coffeeMachine import MENU, resources
import random

def check_resources():



#Prompt user 'What would you like? (espresso/latte/cappaccino:'
user_choice = input("What would you like? (espresso/latte/cappaccino): ")

if user_choice == "espresso":
    print(user_choice)
elif user_choice == "latte":
     print(user_choice)
elif user_choice == "cappaccino":
    print(user_choice)
elif user_choice == "report":
    print(resources)
elif user_choice == "off":
    exit()
else:
    print("end")


#TODO Off will end execution of the program

#TODO Print Report that shows values

#TODO Check resources when user chooses a drink

#TODO Process Coins....

#TODO Check transaction successfull....