n = int(input())
myList = list(map(int, input().split()))

myList.sort()
count = []
for i in range(5):
    count.append(0)
c = 0
index = 0
for i in range(len(myList)-1):
    if(myList[i] == myList[i+1]):
        c += 1
    else:
        count[myList[i]-1] = c
        c = 0
count[4] = c
max = count[0]
for i in range(5):
    if(count[i] > max):
        index = i
        max = count[i]


print(index+1)
