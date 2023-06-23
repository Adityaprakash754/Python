# find best of two test average mark sout of three - Lab 1
marks = []

print("Enter test1, test2,test3 marks: ")
n1,n2,n3 = int(input()),int(input()),int(input())

marks.append(n1)
marks.insert(1,n2)
marks.insert(2,n3)

marks.sort()

print("Average value = ",(marks[1]+marks[2])/2)

