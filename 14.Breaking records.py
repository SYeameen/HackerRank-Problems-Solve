n = int(input())


def breakingRecords(myList):
    myList = list(map(int, input().split()))
    min = myList[0]
    max = myList[0]
    c1 = 0
    c2 = 0
    for i in range(len(myList)):
        if myList[i] > max:
            c1 += 1
            max = myList[i]
        if myList[i] < min:
            c2 += 1
            min = myList[i]

    print(f"{c1} {c2}")


breakingRecords(n)
