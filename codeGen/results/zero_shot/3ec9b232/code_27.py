import sys
from functools import lru_cache

@lru_cache(None)
def permute(M):
    n = len(M)
    if n == 1:
        return [M]
    perms = []
    for i in range(n):
        m = M[i]
        remaining = M[:i] + M[i+1:]
        for p in permute(remaining):
            perms.append([m] + p)
    return perms

@lru_cache(None)
def count_permutations(M, target):
    if len(M) == 0:
        return 1
    n = len(M[0])
    res = 0
    for i in range(n):
        new_target = M[:i] + [x + (1 if x < target[i] else 0) for x in M[i]] + M[i+1:]
        res += count_permutations(new_target, sorted(target))
    return res % (10**9 + 7)

n = int(sys.stdin.readline().strip())
M = list(map(int, sys.stdin.readline().split()))
print(count_permutations(M, M) % (10**9 + 7))
