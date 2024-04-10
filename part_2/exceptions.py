# https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true

a = int(input())

for i in range(a):
    try:
        b, c = map(int, input().split())
        print(b//c)
    except ZeroDivisionError as e:  #or except (ZeroDivisionError, ValueError) as e: print(f"Error Code: {e}")
        print(f"Error Code: {e}")
    except ValueError as e:
        print(f"Error Code: {e}")
