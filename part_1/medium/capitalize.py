# https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys
import string

# Complete the solve function below.
def solve(s):
    # return string.capwords(s," ") or
    a_string = s.split(' ')
    var = " ".join((word.capitalize()) for word in a_string)
    return var


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


# If sep is not specified a different splitting algorithm is applied: runs of consecutive whitespace are regarded as a
# single separator, and the result will contain no empty strings at the start or end if the string has leading or trailing whitespace.
#
# >>> '   1   2   3   '.split()
# ['1', '2', '3']

# If you give split an explicit separator of ' ', as he does, then it will include the empty strings between the spaces
# in the resulting list, which will be join()ed together with spaces, preserving the original amount of trailing space after each word.



# Witchcraft from hackerrank-python

# import string
#
# def solve(s):
#     return string.capwords(s," ")
