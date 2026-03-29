import sys; sys.setrecursionlimit(10000)
from functools import lru_cache
from itertools import permutations

def count_ways(n):
    @lru_cache(None)
    def dp(i, j):
        if i > j:
            return 0
        if i == 0:
            return 1
        ways = 0
        for k in range(i-1, -1, -1):
            ways += dp(k, j-1)
        return ways

    res = 0
    for p in permutations(range(1, n+1)):
        cur_p = list(p)
        i = 0
        j = n
        while i < j:
            if cur_p[i] <= cur_p[j]:
                i += 1
            else:
                j -= 1
        res += dp(n-1, n-1 - i) * (i != 0)

    return int(res % (10**9+7))

n = int(input())
print(count_ways(n))
