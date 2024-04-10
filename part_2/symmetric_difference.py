mcount = int(input().strip())
mset = set(map(int, input().split()))

mcount = int(input().strip())
nset = set(map(int, input().split()))

sd = mset.symmetric_difference(nset)
mylist = sorted(sd)

print(*mylist, sep="\n")
