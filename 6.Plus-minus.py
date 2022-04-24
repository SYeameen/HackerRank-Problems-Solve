value = int(input(""))
positiveValue = 0
negetiveValue = 0
zero = 0


def plusMinus(arr):
    global positiveValue, negetiveValue, zero
    for i in range(value):
        if(theList[i] < 0):
            negetiveValue += 1
        elif(theList[i] > 0):
            positiveValue += 1
        else:
            zero += 1
    print('%.6f' % (positiveValue/value))
    print('%.6f' % (negetiveValue/value))
    print('%.6f' % (zero/value))


theList = list(map(int, input("").split()))
plusMinus(theList)
