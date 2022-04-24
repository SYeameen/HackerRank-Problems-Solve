n = int(input())

queries = []

for i in range(n):
    data = []
    data = list(map(int, input().split()))
    queries.append(data)

for i in range(n):
    a = queries[i][0]
    b = queries[i][1]
    c = queries[i][2]
    if(abs(c-a) > abs(c-b)):
        print("Cat B")
    elif(abs(c-a) < abs(c-b)):
        print("Cat A")
    else:
        print('Mouse C')
