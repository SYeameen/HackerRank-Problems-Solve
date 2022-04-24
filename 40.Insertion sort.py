def printarr(arr):
    for i in range(0, len(arr)):
        print(arr[i], end=" ")
    print()


def insertionSort2(n, arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        printarr(arr)


n = int(input())

arr = list(map(int, input().split()))

insertionSort2(n, arr)
