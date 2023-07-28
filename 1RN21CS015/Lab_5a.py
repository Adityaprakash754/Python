import re

def isPhoneNo(test):
    pattern = "\d{3}-\d{3}-\d{4}"

    result = re.findall(pattern,test)

    if(result):
        print("Found a phone no pattern")
    else:
        print("Couldn't find a pattern")

def isPhoneNo_Without_Re(test):
    list = test.split()

    for i in list:
        if(i.isalnum()):
            print("true",i)

def main():
    test = input("Enter the test string: ")

    isPhoneNo(test)
    isPhoneNo_Without_Re(test)
main()
