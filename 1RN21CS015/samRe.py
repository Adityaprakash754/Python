import re

# S = "Man","Woman","Main"
# S = "Man"
S = "Hello RNSIT Man 123"
# R = "^M.n$"
R = 'Man'
result = re.match(R,S)

if(result):
    print("Successful",result)
else:
    print("UnSuccessful",result)

#*********************************************************#

S = "Hello RNSIT Man 123"
# R = '\s'
# R = "[A - Z]"
R = "[a - e]"
''' looks only for first letter
R = '\s*'
if we use * then it will check for whole string for multiple occurances
'''
result = re.match(R,S)

if(result):
    print("Successful",result)
else:
    print("UnSuccessful",result)
