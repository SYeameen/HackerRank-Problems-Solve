n = input()

if(n[len(n)-2:len(n):1] == "PM"):
    military = n[2:len(n)-2:1]
    temp = n[0:2:1]
    if(int(temp) == 12):
        print(f"{temp}{military}")
    else:
        temp = int(temp)+12
        print(f"{temp}{military}")
else:
    military = n[0:len(n)-2:1]
    temp = n[0:2:1]
    if(int(temp)+12 == 24):
        print(f"00{n[2:len(n)-2:1]}")
    else:
        print(military)
