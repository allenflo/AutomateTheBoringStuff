#This program will let you input a year and check to see if it's a leap year

year = int(input("Please enter a year: "))



if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
           print("Leap Year") 
        else:
            print("NOT a Leap Year")
    else:
        print("Leap Year")


else:
   print("NOT a Leap Year")


