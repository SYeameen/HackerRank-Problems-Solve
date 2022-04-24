value = int(input())


def stairCase(value):
    for i in range(value):
        print(" "*(value-(i+1)), end="")
        print("#"*(i+1))


stairCase(value)
