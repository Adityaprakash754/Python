user_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100}

def romDec(input):
    n = len(input)
    res = 0
    for i in range (n-1):
        if user_dict[input[i]] < user_dict[input[i+1]]:
            res -= user_dict[input[i]]
        else:
            res += user_dict[input[i]]

    res += user_dict[input[i+1]]

    print(res)

input = input("Enter the roman no ")
romDec(input) 
