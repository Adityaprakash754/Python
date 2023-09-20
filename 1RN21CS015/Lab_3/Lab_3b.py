def cmp(str1, str2):
    c = 0
    n = min(len(str1),len(str2))

    for i in range (n):
        if str1[i] == str2[i]:
            c += 1     
    return c

def main():
    str1 = input("Enter the sentence 1 ")
    str2 = input("Enter the sentence 2 ")

    m = max(len(str1),len(str2))
    matchCount = cmp(str1, str2)

    print("Similarity percentage is: ",matchCount/m*100)

main()
