n, m = map(int, input().split())

int_array = list(map(int, input().split()))

set_a = set(map(int, input().split()))

set_b = set(map(int, input().split()))

# happiness = 0

# for i in int_array:
#     if i in set_a:
#         happiness += 1
#     if i in set_b:
#         happiness -= 1
#
# print(happiness)

# hackerrank-python witchcraft
print(sum((i in set_a) - (i in set_b) for i in int_array))

# To see witchcraft
# for i in int_array:
#     print(i in set_a)
#     print(i in set_b)
#     print()
