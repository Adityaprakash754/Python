# file handeling
'''
#Read 

file = open('file.txt','r')
print(file.read())
file.close()


with open('file.txt','r') as file:
    print(file.read())

#Write

with open('file.txt','w') as file:
    file.write(input("Enter sth to the file: "))

#Append

with open('file.txt','a') as file:
    file.write(input("Append sth to the file: "))

#Moving file pointer to a locn
    
with open('file.txt','r+') as file:
    file.seek(6)
    file.write(input("Append sth to the file: "))

'''

import re

f = open('file.txt','r')
for line in f:
    matches = re.findall('\d{10}$',line)
    for match in matches:
        print(match)
    matches = re.findall('[0-9a-zA-Z._]+@gmail.com',line)
    for match in matches:
        print(match) 
