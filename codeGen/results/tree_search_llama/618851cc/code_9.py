import sys

n = int(sys.stdin.readline())
A = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
B = set(map(int, sys.stdin.readline().split()))

union_ab = A.union(B)
sorted_union = sorted(list(union_ab))

for i in range(len(sorted_union)):
    if (i > 0 and sorted_union[i] != sorted_union[i-1]) or \
       (i == len(sorted_union) - 1):
        a = sorted_union[i]
        b = next(x for x in B if x + a not in union_ab)
        print(f"{a} {b}")
