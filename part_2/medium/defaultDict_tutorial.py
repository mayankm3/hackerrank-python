# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true
#Difficult

from collections import defaultdict


def search(n, m):
    my_dict = defaultdict(list)

    list1 = [input() for _ in range(n)]
    list2 = [input() for _ in range(m)]

    for i in range(n):
        my_dict[list1[i]].append(i+1)   #if same key then value are appended in list. See notes.

    for j in list2:
        if j in my_dict:
            print(*my_dict[j])
        else:
            print(-1)


if __name__ == '__main__':
    n, m = map(int, input().split())
    search(n, m)


# Can you explain this line?? print(*d[i])?
# It will unpack the items of list d[i], and by default items of list are seprated by a single space. Ex:
# 
# a=[1,2,3,4,5]
# print(*a)
# output - 1 2 3 4 5

