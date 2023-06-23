# pallindrome or not - Lab 2

# Method 1
'''
n = int(input("Enter the number: "))

num = n
num2 = 0
while(num):
    rem = num%10
    num//= 10

    num2 = (num2*10) + rem

if(num2 == n):
    print("It is a pallindrome")
else:
    print("It is not a pallindrome")
     
'''

#Method 2
n = input("Enter the number: ")
num = n[::-1]

if(n == num):
    print("It is a pallindrome")
else:
    print("It is not a pallindrome")

for i in range(10):
    if str_val.count(str(i)) > 0:
        print(str(i),"appears", str_val.count(str(i)), "times");




        
    
