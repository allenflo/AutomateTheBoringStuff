import art
import random


print(art.logo)
number = random.randint(1, 101)

#Into Wording
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"Pssst, the correct answer is {number}")
difficulty = input("Choose a difficulty.  Type 'easy' or 'hard':")

if difficulty == "easy":
    tries = 10
else:
    tries = 5

while tries > 0:
    print(f"You have {number} attempts remaining to guess the number")
    guess = input(int("Make a guess:"))
    if guess == number:
        print(f"You got it!  The answer was {number}")
    else:
        if guess < number:
            print("Too Low")
        else:
            print("Too High")
    print("Guess again.")
    tries -= 1








