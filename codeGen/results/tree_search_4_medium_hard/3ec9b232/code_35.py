from collections import Counter
from functools import lru_cache

def mergeable_permutations():
    n = int(input())
    m = list(map(int, input().split()))
    
    @lru_cache(None)
    def dp(i, j):
        if i > j:
            return 1
        count_mi = Counter(m[:i+1]).get(m[i], 0)
        return (count_mi + 1) * dp(i-1, j)

    print(dp(n-1, n-1))
