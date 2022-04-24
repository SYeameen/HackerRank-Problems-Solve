numbers = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
           14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty'}
words = ["o' clock", "minute past ", "minutes past ", "quarter past ",
         "half past ", "minutes to ", "quarter to ", "minute to "]


def hour(h):
    return numbers[h]


def timeInWords(h, m):
    sting = ""
    if(m == 00):
        return hour(h)+" "+words[0]
    if(m == 60):
        return hour(h+1)+" "+words[0]
    if(m == 1):
        return numbers[1]+" "+words[1]+hour(h)
    if(m == 59):
        return numbers[m-(m % 10)]+" "+numbers[m % 10]+" "+words[7]+hour(h+1)
    if(m == 15):
        return words[3]+hour(h)
    if(m == 30):
        return words[4]+hour(h)
    if(m == 45):
        return words[6]+hour(h+1)
    if(m < 30):
        if(m > 20):
            return numbers[m-(m % 10)]+" "+numbers[m % 10]+" "+words[2]+hour(h)
        else:
            return numbers[m]+" "+words[2]+hour(h)
    if(m > 30):
        m = 60-m
        if(m > 20):
            return numbers[m-(m % 10)]+" "+numbers[m % 10]+" "+words[5]+hour(h+1)
        else:
            return numbers[m]+" "+words[5]+hour(h+1)


h = int(input())

m = int(input())

result = timeInWords(h, m)
print(result)
