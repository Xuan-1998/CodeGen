from collections import defaultdict

def min_squares(n, m):
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    memo = defaultdict(int)

    def dfs(i, j):
        if i < 0 or j < 0:
            return float('inf')
        if i == 0 and j == 0:
            return 0
        if (i, j) in memo:
            return memo[(i, j)]

        res = float('inf')
        for s in range(1, min(i, j) + 1):
            res = min(res, 1 + dfs(max(0, i - s), max(0, j - s)))
        dp[i][j] = res
        memo[(i, j)] = res
        return res

    return dfs(n, m)

n, m = map(int, input().split())
print(min_squares(n, m))
