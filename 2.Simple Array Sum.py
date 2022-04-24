numbers = int(input(""))
myList = map(int, input("").split())


def simpleArraySum(ar):
    sum = 0
    for i in myList:
        sum += i
    return sum


result = simpleArraySum(myList)
print(result)
