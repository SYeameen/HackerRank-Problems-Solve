alice = 0
bob = 0

a = map(int, input("").split())
b = map(int, input("").split())


def compareTriplets(a, b):
    global alice, bob

    for i in range(len(a)):
        if(a[i] > b[i]):
            alice += 1
        elif(a[i] < b[i]):
            bob += 1


a = list(a)
b = list(b)
compareTriplets(a, b)
print(f"{alice} {bob}")
