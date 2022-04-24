numbers = int(input(""))
myList = map(int, input("").split())


def veryBigSum(myList):
    sum = 0
    for i in myList:
        sum += i
    return sum


result = veryBigSum(myList)
print(result)
