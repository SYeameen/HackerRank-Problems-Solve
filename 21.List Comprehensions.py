x = int(input())
y = int(input())
z = int(input())
n = int(input())

allComprehances = []
finalList = []


def generateList(x, y, z):
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                instanceList = []
                instanceList.append(i)
                instanceList.append(j)
                instanceList.append(k)
                allComprehances.append(instanceList)


def checkValid(allComprehances):
    for arr in allComprehances:
        total = 0
        for i in arr:
            total += i
        if(total != n):
            finalList.append(arr)


generateList(x, y, z)
checkValid(allComprehances)
print(finalList)
