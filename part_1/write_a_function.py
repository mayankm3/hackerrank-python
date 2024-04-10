# https://www.hackerrank.com/challenges/write-a-function?isFullScreen=true

def is_leap(year):
    leap = False

    if year % 400 == 0: #If you write year//400 then it gives you quotient and not remainder!
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

    return leap

year = int(input())
print(is_leap(year))


#hackerrank-python witchcraft
# leap =  year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
# If the remainder of year % 4 is 0, it is a candidate for leap year.
# 2000
# 1 and (1 or 0) = 1 and 1 = 1
#
# 2020
# 1 and (0 or 1) = 1 and 1 = 1
#
# 1900
# 1 and (0 or 0) = 1 and 0 = 0
