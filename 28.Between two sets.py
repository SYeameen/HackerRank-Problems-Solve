def isFactor(arr, target):
    c = 0
    for i in range(len(arr)):
        #print(f"{target} {arr[i]} {target%arr[i]}")
        if(target % arr[i] == 0):
            c += 1
    #print(f"len = {c} {len(arr)}")
    #print(" ")
    if(c == len(arr)):
        return True
    return False


def revIsFactor(arr, target):
    c = 0
    for i in range(len(arr)):
        #print(f"{target} {arr[i]} {arr[i]%target}")
        if(arr[i] % target == 0):
            c += 1
    #print(f"len = {c} {len(arr)}")
    #print(" ")
    if(c == len(arr)):
        return True
    return False


def countBetweenTwoSets(a, b):
    a.sort()
    b.sort()
    factorsofa = []
    c = 0
    for i in range(a[len(a)-1], b[len(b)-1]+1):
        if isFactor(a, i):
            factorsofa.append(i)
    # print("-----------------------------------")
    for i in range(len(factorsofa)):
        if(revIsFactor(b, factorsofa[i])):
            c += 1
    print(c)


def main():
    temp = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    countBetweenTwoSets(a, b)


main()
