# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true

n = int(input())
s = set(map(int, input().split()))

for i in range(int(input())):
    comm = input().split()
    if comm[0] == 'pop':
        s.pop()
    elif comm[0] == 'remove':
        s.remove(int(comm[1]))
    elif comm[0] == 'discard':
        s.discard(int(comm[1]))

print(sum(s))