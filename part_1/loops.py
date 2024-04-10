# https://www.hackerrank.com/challenges/python-loops?isFullScreen=true

if __name__ == '__main__':
    n = int(input())

    if 1 <= n <= 20:
        square = [i**2 for i in range(n)];
        for num in square:
            print(num)

#hackerrank-python witchcraft
# [print(i ** 2) for i in range(n)]