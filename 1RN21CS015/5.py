''' Student grade point calculation
A 90:100
B 80-90
C 70-80
D 60-70
E < 60
'''
marks = int(input("Enter your marks: "))


if(marks >= 90):
    print("Your grade is A")
elif(marks >= 80 and marks < 90):
    print("Your grade is B")
elif(marks >= 70 and marks < 80):
    print("Your grade is C")
elif(marks >= 60 and marks < 70):
    print("Your grade is D")
else:
    print("Your grade is E")
