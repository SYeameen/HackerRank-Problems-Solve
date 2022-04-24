n = int(input())

myList = list(map(int, input().split()))
birthDay = list(map(int, input().split()))
sum = 0
c = 0
for i in range(n-(birthDay[1]-1)):
    sum = 0
    for j in range(i, i+birthDay[1]):
        sum += myList[j]
    if(sum == birthDay[0]):
        c += 1

print(c)
