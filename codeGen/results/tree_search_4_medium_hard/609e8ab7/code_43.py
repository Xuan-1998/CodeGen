import sys
from collections import defaultdict

def adjust_values(n, parent, l, r):
    dp = [float('inf')] * n
    dp[0] = 0  # root node has no operations needed

    memo = defaultdict(lambda: float('inf'))
    memo[0] = 0

    def dfs(i):
        if dp[i] != float('inf'):
            return dp[i]
        
        if l[i] <= r[i]:
            dp[i] = 0
        else:
            max_diff = (r[i] - l[i])
            min_ops = float('inf')
            
            for j in range(i):
                diff = max(0, r[j] - l[j]) + dfs(j)
                if diff < min_ops:
                    min_ops = diff
            
            dp[i] = min(min_ops, max_diff)

        return dp[i]

    total_ops = 0
    for i in range(n-1, -1, -1):
        total_ops += dfs(i)

    return total_ops

T = int(input())
for _ in range(T):
    n = int(input())
    parent = list(map(int, input().split()))
    l = [int(x) for x in input().split()]
    r = [int(x) for x in input().split()]

    print(adjust_values(n, parent, l, r))
