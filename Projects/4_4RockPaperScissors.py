#Rock paper scissors not exactly from the course but from scratch
import random

print("Welcome to Rock Paper Scissors")




playerChoice = input ("(1)Rock,  (2)Paper, or (3)Scissors :" )

#Computer Choice

computerChoice = random.randint(0,2)
print(f"The Computer Chooses {computerChoice}")



