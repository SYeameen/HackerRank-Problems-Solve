test = int(input())

for k in range(test):
    n = int(input())
    sum = int(1)
    for i in range(n+1):
        if(i == 0):
            sum = 1
        elif(i % 2 == 0):
            sum += 1
        else:
            sum = (sum*2)

    print(sum)
