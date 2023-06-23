# Python Lists

L1 = ["a","b","c","d"]
L2 = [True, "a", 5, 4.9]
print(L1)
print(type(L2))
print(type(L2[0]))
print(type(L2[1]))
print(L1[::])
print(L1[:3])
print(L1[1:])
print(L1[0:3:2])
print(L1[::-1])
#**********************************
L1[1] = False
print(L1)

L1 [1:2] = 100,90
print(L1)

L1.append("cherry")
print(L1)

L1.insert(2,"banana")
print(L1)

print(L1.pop()) #default last index / mention the index

L1.remove("a")
print(L1)

del L1[2]
print(L1)

'''
L1.clear() # it clears all elements of the list
print(L1)

del L1 # deletes the list
print(L1)
'''
#**********************************
L3 = L1 + L2
print(L3)

L4 = L1 * 2
print(L4)

#**********************************
# if conditions
'''
if(condition):
    Statement
else:
    Statement


#********************#

if(condition):
    Statement
elif(condition):
    Statement
else:
    Statement
'''








