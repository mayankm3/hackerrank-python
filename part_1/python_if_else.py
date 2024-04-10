# https://www.hackerrank.com/challenges/py-if-else?isFullScreen=true
#Easy

if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 == 0 and 2 <= n <= 5:
        print("Not Weird")
    if n % 2 == 0 and 6 <= n <= 20:
        print("Weird")
    if n % 2 == 0 and n > 20:
        print("Not Weird")
    if n % 2 != 0:
        print("Weird")


#Solution 4 months later
# if __name__ == '__main__':
#     n = int(input().strip())
#
#     if (n % 2 != 0):
#         print("Weird")
#     elif (2 <= n <= 5):
#         print("Not Weird")
#     elif (6 <= n <= 20):
#         print("Weird")
#     else:
#         print("Not Weird")