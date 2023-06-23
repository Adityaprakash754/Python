# Leap year or not
year = int(input("Enter year: "))


if((Year % 400 == 0) or (Year % 100 != 0) and (Year % 4 == 0)):
    print("It is a leap year")
else:
    print("It is not a leap year")
