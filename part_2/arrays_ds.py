#!/bin/python3

import math
import os
import random
import re
import sys

def reverseArray(a):
    my_list = []
    arr_size = -1 * len(a)

    i = -1

    while i >= arr_size:
        print(i)
        my_list.append(a[i])
        i -= 1

    return my_list


if __name__ == '__main__':
    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    print(*res)
