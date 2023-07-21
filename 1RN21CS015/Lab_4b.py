user_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100}

def romDec(input):
    res = 0
    for i in input:
        res += user_dict[i]

    print(res)

input = input("Enter the roman no ")
romDec(input)