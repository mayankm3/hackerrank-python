# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=true

from collections import namedtuple

n = int(input())
columns = input().split()

total = 0
Student = namedtuple('Student', columns)

for _ in range(n):
    detail = Student(*input().split())
    total += int(detail.MARKS)

print(total/n)









