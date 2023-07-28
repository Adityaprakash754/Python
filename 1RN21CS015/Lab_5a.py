import re

def isPhoneNo(test):
    pattern = "\d{3}-\d{3}-\d{4}"

    result = re.findall(pattern,test)

    if result:
        print("Found a phone no pattern")
    else:
        print("Couldn't find a pattern")

def isPhoneNo_Without_Re(test):
    list = test.split('-')
    count = 0
    for i in list:
        if(i.isdigit()):
            count += len(i)
    
    if count == 10:
         print("Found a phone no pattern")
    else:
        print("Couldn't find a pattern") 

def main():
    test = input("Enter the test string: ")

    isPhoneNo(test)
    isPhoneNo_Without_Re(test)
main()
