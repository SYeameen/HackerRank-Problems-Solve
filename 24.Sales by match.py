n = int(input())
arr = list(map(int, input().split()))

arr.sort()
c = 0
total = 0

for i in range(len(arr)-1):

    if arr[i] == arr[i+1]:
        c += 1
    else:
        if((c+1) % 2 == 0):
            total += (c+1)/2
        else:
            total += (c)/2
        c = 0
if((c+1) % 2 == 0):
    total += (c+1)/2
else:
    total += (c)/2
print(int(total))
