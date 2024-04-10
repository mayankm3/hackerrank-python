# https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true

from cmath import phase


def pc():
    complex_num = complex(input())
    print(abs(complex_num))     # abs doesn't come from cmath module
    print(phase(complex_num))


if __name__ == '__main__':
    pc()



# complex() function can be used in python to convert the input as a complex number.
# cmath.phase(x) Returns the phase of x, as a float.
# The modulus (absolute value) of a complex number can be computed using the built-in abs() function.

# >>>z = complex('5-9j')
# >>>print(z)
# (5-9j)