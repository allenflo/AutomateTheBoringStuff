from game_data import data
from art import logo, vs
import random

#Pull Number of items out of database
total_items = (len(data))
#Assign random choices to A and B
choice_a = random.randint(1, total_items)
choice_b = random.randint(1, total_items)
#Check to make sure choices are not equal or pick new choice
while choice_b == choice_a:
    choice_b = random.randint(1, total_items)

print(logo)
print(f"Compare A:{data[choice_a]['name']}, a {data[choice_a]['description']}, from {data[choice_a]['country']}")
print(vs)
print(f"Compare B:{data[choice_b]['name']}, a {data[choice_b]['description']}, from {data[choice_b]['country']}")





# print(logo)
# print(data[0]['name'])


# print(vs)
# print("test")
