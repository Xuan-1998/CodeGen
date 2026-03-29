===BEGIN CODE===
from collections import defaultdict
from functools import lru_cache

def solve():
    n = int(input())
    costs = list(map(int, input().split()))
    strings = [input() for _ in range(n)]
    
    @lru_cache(None)
    def dp(i, prev_str, rev):
        if i == n:
            return 0
        min_cost = float('inf')
        for c in costs[i]:
            new_prev_str = prev_str + (strings[i][::-1] if not rev else strings[i])
            if new_prev_str <= strings[i+1:]:
                min_cost = min(min_cost, dp(i+1, new_prev_str, not rev) + c)
        return min_cost
    
    print(dp(0, '', True))

solve()
