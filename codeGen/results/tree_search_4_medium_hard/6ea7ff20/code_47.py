def mergeable(p):
    n = len(p) // 2
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    memo = {}

    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == j or p[i] > p[j]:
            return 1
        if i == 0 and j == n - 1:
            return 1 if p[i] < p[j] else 0
        res = float('inf')
        for k in range(i + 1, j):
            res = min(res, dfs(i, k) + dfs(k, j))
        memo[(i, j)] = res
        return res

    for i in range(n):
        if p[i] < p[n - i - 1]:
            dp[i][n - i - 1] = 1 + dfs(i, n - i - 1)
        else:
            dp[i][n - i - 1] = dfs(i, n - i - 1)

    for i in range(n):
        if all(p[k] < p[n - i - 1] for k in range(i)):
            return "YES"
    return "NO"

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    print(mergeable(p))
