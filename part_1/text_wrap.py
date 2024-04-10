# https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true

import textwrap

def wrap(string, max_width):
    ans = textwrap.fill(string, max_width)
    return ans

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# The textwrap module provides function fill()
#
# The fill() function wraps a single paragraph in text and returns a single newline-separated string containing the wrapped paragraph.
#
# my_str = "Python is an interpreted, high-level and general-purpose programming language."
# resultant = textwrap.fill(my_str, width=30)
# print(resultant)
#
# Python is an interpreted,
# high-level and general-purpose
# programming language.