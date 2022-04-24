buffer = list(map(int, input().split()))
arr = list(map(int, input().split()))
n = buffer[0]
ans = 0
i = 0
while i < n - 1:
    if i + 2 >= n or arr[i + 2] == 1:   # Not possible to make a jump of size 2
        i = i + 1
        ans = ans + 1
    else:
        i = i + 2
        ans = ans + 1
print(ans)
