q = list(map(int, input().split()))
n = q[0]
m = q[1]
myList = list(map(int, input().split()))
max = m
for i in range(n):
    if myList[i] > max:
        max = myList[i]

if(max <= m):
    print(0)
else:
    print(max-m)
