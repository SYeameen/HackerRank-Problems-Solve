def minimumDistances(a):
    b = {}
    c = -1
    for i in range(0, len(a)):
        if a[i] in b:
            b[a[i]] = abs(b[a[i]]-i)
            if(c < b[a[i]] and c == -1):
                c = b[a[i]]
            elif(c > b[a[i]] and c != -1):
                c = b[a[i]]
        else:
            b.update({a[i]: i})
    return c


n = int(input())

a = list(map(int, input().rstrip().split()))

result = minimumDistances(a)

print(result)
