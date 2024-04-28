from itertools import chain, combinations
n = int(input())
arr = list(map(int, input().split()))
s = set()
for r in range(1, n+1):
    for c in combinations(arr, r):
        s.add(sum(c))
print(' '.join(map(str, sorted(list(s)))))
