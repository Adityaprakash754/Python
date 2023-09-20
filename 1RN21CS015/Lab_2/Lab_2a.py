def fib(n):
    if n == 1:
        return 0
    elif n ==2:
        return 1
    # elif n <= 0:
    #     print("Invalid index position.")
    #     exit(0)
    else:
        return fib(n-1)+fib(n-2)

n = int(input("Enter the no: "))
if n<1:
    raise ValueError("Invalid index position.")
print(fib(n))
