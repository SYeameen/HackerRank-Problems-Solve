n = list(map(int, input().split()))
x1 = n[0]
v1 = n[1]
x2 = n[2]
v2 = n[3]


count = 0
flag = False
if(x1 < x2 and v1 < v2) or v1 == v2:
    pass
else:
    while x1 < x2:

        x1 = x1+v1
        x2 = x2+v2
        count = count+1
        if x1 == x2:
            flag = True

if(flag):
    print("YES")
else:
    print("NO")
