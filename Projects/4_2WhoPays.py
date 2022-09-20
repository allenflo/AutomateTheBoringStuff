#This program will let user enter names to a list and then one will be randomly chosen

import random

names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")

print(names)

totalNames = ((len(names)) - 1)
luckyNumber = random.randint(0, totalNames)

print(f"{luckyNumber}")

print(f"{names[luckyNumber]} will pay the bill today")

