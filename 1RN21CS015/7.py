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

num1 =[]
for j in n:
    num1.append(j)
    
num1.sort()
count = 1

for i in range(len(num1) -1):
    if(num1[i] == num1[i+1]):
        count+=1
    else:
        print(num1[i-1],":",count)
        count = 1




        
    
