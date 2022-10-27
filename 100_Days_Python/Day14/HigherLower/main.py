from art import logo, vs
from game_data import data
import random
from replit import clear


def format_data(account):
  """ Format Account Data into printable format """
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return (f"{account_name}, a {account_descr}, from {account_country}")

def check_answer(guess, a_followers, b_followers):
  """Take the user guess and follower counts and returns if they got it right"""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

#Display Art
print(logo)
score=0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue == True:
# Generate a random account from the game data.
  account_a = account_b
  account_b = random.choice(data)
  while account_a == account_b:
    account_b = random.choice(data)

  
    
  #Display starting choices
  print(f"Compare A: {format_data(account_a)}.")
  print(vs)
  print(f"Against B: {format_data(account_b)}.")

  #Ask for user guess
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()

  #Check if user is correct
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]

  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  
  
  
  if is_correct:
    clear()
    score += 1
    print(logo)
    print(f"You're right!  Current score: {score}.")
    
  else:
    clear()
    game_should_continue = False
    print(logo)
    print(f"Sorry, that's wrong.  Final Score {score}")



    
