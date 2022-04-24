def reverseInt(x):
    sum = int(0)
    while x != 0:
        sum = sum*10+(x % 10)
        x = x//10
    return sum


buffer = list(map(int, input().split()))

start = buffer[0]
end = buffer[1]
k = buffer[2]
days = int(0)
for i in range(start, end+1):
    temp = abs(i-reverseInt(i))
    if(temp % k == 0):
        days += 1

print(days)
