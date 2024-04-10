# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list?isFullScreen=true

if __name__ == '__main__':
    n = int(input())    # Almost useless line. Perhaps just to specify.
    arr = map(int, input().split())

    listArr = list(arr)
    listArr.sort(reverse=True)  # Don't assign to a variable because sort doesn't return anything. It permanently sorts.

    for a in listArr:
        for b in listArr:
            if b < a:
                print(b)
                break
        break


# hackerrank-python solution
# n = int(input())
# arr = list(map(int, input().split()))
# print(max([x for x in arr if x!=max(arr)]))
