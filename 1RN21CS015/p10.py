# Simple Calculator 
# Method 1
def fun(arg,a,b):
    aditya = {
        '+': a+b,
        '-': a-b,
        '*': a*b,
        '/': a/b,
    }
    return aditya.get(arg)

a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = input("Enter operation to be performed: ")[0]

print(fun(c,a,b))

#******************************************************
# Method 2
a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = input("Enter operation to be performed: ")[0]

if(c == '+'):
    d = a+b
elif(c == '-'):
    d = a-b
elif(c == '*'):
    d = a*b
elif(c == '/'):
    d = a/b
else:
    print("Invalid operator")
    exit()

print(d)
