
def insertionSort(arr,n):
#    for i in arr:
#    works as for each loop
    for i in range (1,n):
        v = arr[i]
        j = i-1

        while j >= 0 and arr[j] > v:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = v


def main():
    arr = []
    n = int(input("Enter the no of elem of list "))

    for i in range(n):
        a = int(input())
        arr.append(a)
    
    insertionSort(arr,n)
    print(arr)


main()