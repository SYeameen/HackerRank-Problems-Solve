array2D = int(input(""))
arry = []
leftDiagonal = 0
rightDiagonal = 0

for i in range(array2D):
    arry.append(list(map(int, input().split())))


def diagonalDifference(arr):
    global leftDiagonal, rightDiagonal
    for i in range(len(arry)):
        for j in range(len(arry[i])):
            if(i == j):
                leftDiagonal += arry[i][j]
            if(i+j == array2D-1):
                rightDiagonal += arry[i][j]
    return abs(leftDiagonal-rightDiagonal)


print(diagonalDifference(arry))
