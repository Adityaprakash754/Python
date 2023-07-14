def main():
    string = input("Enter the sentence ")

    x = string.split()

    count = 0
    l = 0
    u = 0
    for i in string:
        if i.isdigit():
            count += 1
        elif i.islower():
            l += 1
        elif i.isupper():
            u += 1
    print("The no of words are: ",len(x))
    print("The no of digits are: ",count)
    print("The no of lower case letter are: ",l)
    print("The no of upper case letter are: ",u)

main()

