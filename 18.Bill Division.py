index = list(map(int, input().split()))

myList = list(map(int, input().split()))

total = int(input())
sum = 0
for i in range(index[0]):
    if i != index[1]:
        sum += myList[i]

dividePart = sum/2
if dividePart < total:
    print(int(total-dividePart))
else:
    print('Bon Appetit')
