# find best of two test average mark sout of three - Lab 1

#Method 1
marks = []

print("Enter test1, test2,test3 marks: ")
n1,n2,n3 = int(input()),int(input()),int(input())

marks.append(n1)
marks.insert(1,n2)
marks.insert(2,n3)

marks.sort()

print("Average value = ",(marks[1]+marks[2])/2)

#*******************************************************

#Method 2
print("Enter test1, test2,test3 marks: ")
n1,n2,n3 = int(input()),int(input()),int(input())

if n1 <= n2 and n1 <= n3:
    avgMarks = (n2+n3)/2
elif n2 <= n1 and n2 <= n3:
    avgMarks = (n1+n3)/2
else:
    avgMarks = (n1+n2)/2
print("Average value = ",avgMarks)
