# Leap year or not
year = int(input("Enter year: "))


if(year%4 == 0):
    print("It is a leap year")
elif(year%400 == 0 & year%100 !=0):
    print("It is a leap year")
else:
    print("It is not a leap year")
