# largest of 3 nos
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if(a>b & a>c):
    print("a is largest:",a)
elif(b>a & b>c):
    print("b is largest:",b)
else:
    print("c is largest:",c)
