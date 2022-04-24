test_case = int(input())

for t in range(test_case):
    data = list(map(int, input().split()))
    attandance = list(map(int, input().split()))
    threshHold = data[1]
    n = len(attandance)
    c = int(0)
    for i in range(n):
        if(attandance[i] <= 0):
            c += 1
    if(c >= threshHold):
        print('NO')
    else:
        print('YES')
