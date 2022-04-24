def apples_oranges(s, t, a, b, apples, oranges):
    noOfApples = 0
    noOfOranges = 0

    for i in range(len(apples)):
        if a+apples[i] >= s and a+apples[i] <= t:
            noOfApples += 1

    for i in range(len(oranges)):
        if b+oranges[i] >= s and b+oranges[i] <= t:
            noOfOranges += 1

    print(noOfApples)
    print(noOfOranges)


st = input().split()
s = int(st[0])
t = int(st[1])
ab = input().split()
a = int(ab[0])
b = int(ab[1])
mn = input().split()
m = int(mn[0])
n = int(mn[1])

apples = list(map(int, input().rstrip().split()))

oranges = list(map(int, input().rstrip().split()))

apples_oranges(s, t, a, b, apples, oranges)
