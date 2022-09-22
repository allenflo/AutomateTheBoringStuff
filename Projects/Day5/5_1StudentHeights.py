# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

sum = 0
number = 0

for total in student_heights:
    sum += total
    number += 1
     
print(sum)

print(number)

average = round(sum / number)

print(f"The average score is {average}")

