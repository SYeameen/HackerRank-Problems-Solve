values = int(input())
myList = list(map(int, input().split()))

myList.sort()


def birthdayCakeCandles(candles):
    candles = 0
    final = myList[len(myList)-1]
    for i in myList:
        if i == final:
            candles += 1
    return candles


result = birthdayCakeCandles(values)
print(result)
