#Swap

a = int(input("a: "))
b = int(input("b: "))

c = a
a = b
b = c

print(f"a = {a}")
print(f"b = {b}")

a = a+b
b = a-b
a = a-b


print(f"a = {a}")
print(f"b = {b}")
