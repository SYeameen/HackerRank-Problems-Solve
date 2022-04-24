alpha = list(map(int, input().split()))

word = input()
aux = []
for i in range(len(word)):
    index = ord(word[i])-97
    aux.append(alpha[index])

max = aux[0]

for i in range(len(aux)):
    if(max < aux[i]):
        max = aux[i]

print(max*len(word))
