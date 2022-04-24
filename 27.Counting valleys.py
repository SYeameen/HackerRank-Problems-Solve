def countUpHill(str):
    c = int(0)
    flag = False
    final = int(0)
    for i in str:
        if i == 'D':
            c = c-1
        else:
            c += 1
        if c < 0:
            flag = True
        if flag and c == 0:
            final += 1
    return final


def countDownHill(str):
    # DDUU*DDUDUU*UD
    c = int(0)
    flag = False
    final = int(0)
    for i in str:
        if i == 'D':
            c = c-1  # -2
            # print(c)
        else:
            c += 1  # 0
            # print(c)
        if c < 0:
            flag = True
        if c > 0:
            flag = False
        if flag and c == 0:
            final += 1
    return final


""" 
\  /\    /\ 
 \/  \/\/ 
 """
n = int(input())
str = """  """
str = input()
result = int(0)
str1 = str

if str1[0:0] == 'U':
    result = countUpHill(str)
else:
    result = countDownHill(str)

print(result)
