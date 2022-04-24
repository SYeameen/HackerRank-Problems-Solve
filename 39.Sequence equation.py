buffer = int(input())
temp = list(map(int, input().split()))
arr = []
arr.append(-1)
for i in range(buffer):
    arr.append(temp[i])
for i in range(1, buffer+1):
    for j in range(1, buffer+1):
        t = arr[j]
        if(arr[t] == i):
            print(j)
            break
