from art import logo
from random import randint

print(logo)
number = randint(1, 100)

#Into Wording
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
# print(f"Pssst, the correct answer is {number}")
difficulty = input("Choose a difficulty.  Type 'easy' or 'hard': ")

#Set Difficulty
if difficulty == "easy":
    tries = 10
else:
    tries = 5

while tries > 0:
    print(f"You have {tries} attempts remaining to guess the number")
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You got it!  The answer was {number}")
        exit()
    else:
        if guess < number:
            print("Too Low")
        else:
            print("Too High")
        print("Guess again.")
    tries -= 1
print(f"You are all out of tries.  The number was {number}")









