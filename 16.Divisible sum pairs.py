q = list(map(int, input().split()))
n = q[0]
m = q[1]
myList = list(map(int, input().split()))
c = 0
for i in range(n):
    for j in range(n):
        if(i != j and i < j and (myList[i]+myList[j]) % m == 0):
            c += 1

print(c)
