#Generates your love score by asking your name and then cointing how many times
#the letters for TRUE LOVE occur in the names and then will tell you your love score
#and what it means.

print("Welcome to the Love Calculator")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combinedName = name1 + name2

combinedName = combinedName.lower()

print(combinedName)

t = combinedName.count("t")
r = combinedName.count("r")
u = combinedName.count("u")
e = combinedName.count("e")

true = t + r + u + e

l = combinedName.count("l")
o = combinedName.count("o")
v = combinedName.count("v")
ee = combinedName.count("e")

love = l + o + v + ee

score = str(true) + str(love)
score = int(score)

if score <10 or score>90:
    print(f"Your score is {score}, you go together like coke and mentos.")

elif score>40 and score<50:
    print(f"Your score is {score}, you are alright together")

else:
    print(f"Your score is {score}")



#I don't think the game rules were correct.  double digits are higly likely when combining the names





