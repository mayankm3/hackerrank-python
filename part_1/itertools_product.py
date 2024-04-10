# https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true
from itertools import product

if __name__ == '__main__':
    list1, list2 = [], []

    list1 = [int(item) for item in input().split()]
    list2 = [int(item) for item in input().split()]

    print(*product(list1, list2))   # print(product(list1, list2)) will print <itertools.product object at 0x1026edd80>.
                                    # print(type(p)) will print <class 'itertools.product'>
                                    # itertools.product() returns an object of type itertools.product.
                                    # itertools.product is an iterator, so the contents is not output by print().


# hackerrank-python witchcraft
# from itertools import product
#
# a = map(int, input().split())
# b = map(int, input().split())
#
# print(*product(a, b))


# itertools.product() computes the cartesian product of input iterables.
# >>> print list(product([1,2,3],[3,4]))
# [(1, 3), (1, 4), (2, 3), (2, 4), (3, 3), (3, 4)]



# Let’s say we have a list: num_list = [1,2,3,4,5]

# And we define a function that takes in 5 arguments and returns their sum:
# def num_sum(num1,num2,num3,num4,num5):
#     return num1 + num2 + num3 + num4 + num5

# if we want to unpack num_list and pass in the 5 elements as separate arguments for the num_sum function,
# we could do so as follows: num_sum(*num_list)