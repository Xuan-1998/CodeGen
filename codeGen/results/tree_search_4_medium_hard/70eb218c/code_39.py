import sys

def min_operations(n, x):
    memo = {}

    def dfs(s):
        if len(s) == n:
            return 0
        if s in memo:
            return memo[s]
        res = float('inf')
        for d in '012':
            new_s = s + d
            res = min(res, 1 + dfs(new_s))
        memo[s] = res
        return res

    return dfs(str(x)) if len(str(x)) < n else -1

n, x = map(int, input().split())
print(min_operations(n, x))
