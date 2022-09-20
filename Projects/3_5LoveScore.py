#Generates your love score by asking your name and then cointing how many times
#the letters for TRUE LOVE occur in the names and then will tell you your love score
#and what it means.

print("Welcome to the Love Calculator")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()

print(name1)
print(name2)

t = name1.count("t")
r = name1.count("r")
u = name1.count("u")
e = name1.count("e")

true = t + r + u + e

l = name2.count("l")
o = name2.count("o")
v = name2.count("v")
ee = name2.count("e")

love = l + o + v + ee

score = str(true) + str(love)
score = int(score)

if score <10 or score>90:
    print(f"Your score is {score}, you go together like coke and mentos.")

elif score>40 and score<50:
    print(f"Your score is {score}, you are alright together")

else:
    print(f"Your score is {score}")







