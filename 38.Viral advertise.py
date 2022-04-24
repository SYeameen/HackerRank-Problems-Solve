n = int(input())

shared = int(5)
likes = int(0)
cumulative = int(0)

for i in range(n):
    likes = shared//2
    cumulative += likes
    shared = likes*3

print(cumulative)
