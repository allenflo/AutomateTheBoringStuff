#This program will simulate the flipping of a coin using randomization module


import random

print("1 is Heads.  0 is Tails")
flip = random.randint(0, 1)
print(f"The number is {flip}")
if flip == 1:
    print("Heads")
else:
    print("Tails")



