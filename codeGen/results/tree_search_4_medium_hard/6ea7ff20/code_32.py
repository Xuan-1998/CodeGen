def mergeable(p):
    n = len(p) // 2
    dp = [[False] * (n + 1) for _ in range(n + 1)]

    def dfs(i, j):
        if i >= n:
            return p[:i].empty or p[i:].empty
        if dp[i][j]:
            return True
        if i == n and j == 0:
            return p.empty or [0] * (n - len(p)) + list(range(len(p) - n))
        if i < n and j == 0:
            return False
        if i > j:
            dp[i][j] = dfs(i, j)
            return dp[i][j]
        if p[i] <= p[j]:
            dp[i][j] = dfs(i + 1, j) or dfs(i, j - 1)
            return dp[i][j]
        if p[i] > p[j]:
            dp[i][j] = dfs(i, j - 1) or dfs(i + 1, j)
            return dp[i][j]

    return "YES" if dfs(0, n) else "NO"


import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    print("YES" if mergeable(p) else "NO")
