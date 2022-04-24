n = list(map(int, input().split()))

noOfusb = list(map(int, input().split()))
noOfKeyboard = list(map(int, input().split()))

totalPrice = n[0]
max = 0
for i in range(n[1]):
    for j in range(n[2]):
        if(max < (noOfusb[i]+noOfKeyboard[j]) and noOfusb[i]+noOfKeyboard[j] <= totalPrice):
            max = noOfusb[i]+noOfKeyboard[j]


if(max != 0):
    print(max)
else:
    print(-1)
