# https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true

def print_formatted(number):
    for val in range(1, number+1):
        width = len(bin(number).replace("0b", ""))
        binary = bin(val).replace("0b", "")
        hexadecimal = format(val, 'X')
        octal = oct(val).replace("0o", "")
        print(str(val).rjust(width)+" "+octal.rjust(width)+" "+hexadecimal.rjust(width)+" "+binary.rjust(width))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


# Witchcraft from hackerrank-python discussions
# n = int(raw_input())
# width = len("{0:b}".format(n))
# for i in xrange(1,n+1):
#   print "{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width)


# Like witchcraft, a month later
# def print_formatted(number):
#     width = len("{0:b}".format(number))
#
#     for i in range(1, number+1):
#         print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))
