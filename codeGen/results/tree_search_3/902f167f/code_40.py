from collections import defaultdict

def min_squares(n, m):
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    memo = defaultdict(dict)

    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        res = float('inf')
        for x in range(1, min(i, j) + 1):
            if i % x == 0 and j % x == 0:
                res = min(res, dfs(i // x, j // x) + 1)

        memo[(i, j)] = res
        return res

    return dfs(n, m)
