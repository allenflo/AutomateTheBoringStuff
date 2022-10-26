from game_data import data
from art import logo, vs
import random


score = 0






#Display Art
print(logo)

# Pull Number of items out of database
total_items = (len(data))

# Assign random choices to A and B
choice_a = random.randint(1, total_items)
choice_b = random.randint(1, total_items)
# Check to make sure choices are not equal or pick new choice
while choice_b == choice_a:
    choice_b = random.randint(1, total_items)

print(f"Compare A:{data[choice_a]['name']}, a {data[choice_a]['description']}, from {data[choice_a]['country']}")
print(vs)
print(f"Against B:{data[choice_b]['name']}, a {data[choice_b]['description']}, from {data[choice_b]['country']}")

# Player Choice
player_choice = input("Who has more followers?  Type 'A' or 'B': ")
player_choice = player_choice.upper()

# Get Followers
followers_a = data[choice_a]['follower_count']
followers_b = data[choice_b]['follower_count']

# Check for winner
winner = ""
if followers_a > followers_b:
    winner = "A"

elif followers_b > followers_a:
    winner = "B"
    choice_a = choice_b


if player_choice == winner:
    print(logo)
    score += 1
    print(f"You're right!!!  Current score: {score}")
else:
    print(logo)
    print(f"Sorry, that's wrong.  Final score: {score}")
