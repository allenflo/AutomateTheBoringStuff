# This game asks for your name and then challenges you to guess a random number 
# The Number is randomly generated between 1 and 20


import random





print('Hello.  What is your name?')
name = input()

print('Well, ' + name + '. I am thinking of a number between 1 and 20.')
secretnumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print("Take a guess.")
    guess = int(input())

    if guess < secretnumber:
        print("Your number is too low")

    elif guess > secretnumber:
        print("Your number is too high")

    else:
        break #This condition is for a correct guess

if guess == secretnumber:
    print ("Good Job, " + name + " You guessed the number in " +str(guessesTaken) + " Frankguesses")

else:
    print("Nope.  The number I was thinking of was " + str(secretnumber))










