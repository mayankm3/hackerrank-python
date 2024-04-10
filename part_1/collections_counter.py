# https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true

from collections import Counter


def joota():
    num_of_shoe = int(input())
    shoe_sizes = Counter(map(int, input().split()))
    num_of_customers = int(input())

    earnings = 0

    for _ in range(num_of_customers):
        size, price = map(int, input().split())
        if shoe_sizes[size]:    # Counter objects have a dictionary interface except that they return a zero count for
                                # missing items instead of raising a KeyError. If shoes[size] is 0 this will evaluate to False
            earnings += price
            shoe_sizes[size] -= 1   # or shoe_sizes.subtract(Counter([size]))

    print(earnings)


if __name__ == '__main__':
    joota()



# My solution a month later

# paisa = 0
#
# for num in range(num_of_customers):
#     size, price = map(int, input().split())
#     if size in a.keys():
#         b = Counter({size:1})
#         a = a-b
#         paisa += price
#
# print(paisa)
