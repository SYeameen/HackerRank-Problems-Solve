theList = list(map(int, input().split()))
sumOfArray = []
for j in range(len(theList)):
    sum = 0
    for i in range(len(theList)):
        if(j+1 != i+1):
            sum += theList[i]
    sumOfArray.append(sum)


sumOfArray.sort()
a = sumOfArray[0]
b = sumOfArray[len(sumOfArray)-1]
print(f"{a} {b}")
