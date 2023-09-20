def mergeSort(arr, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    mergeSort(arr,low,mid)
    mergeSort(arr,mid+1,high)
    simpleMerge(arr,low,mid,high)

def simpleMerge(arr,low,mid,high):
    i = low
    j = mid +1
    c = []

    while i <= mid and j <= high:
        if arr[i] < arr[j]:
            c.append(arr[i])
            i += 1
        
        else:
            c.append(arr[j])
            j += 1
    
    while i <= mid:
        c.append(arr[i])
        i += 1
    while j <= high:
        c.append(arr[j])
        j += 1


    for i in range(low, high + 1):
        arr[i] = c[i- low]


def main():
    arr = []
    n = int(input("Enter the no of elem of list "))

    for i in range(n):
        a = int(input())
        arr.append(a)
    
    mergeSort(arr,0,n-1)
    print(arr)


main()
