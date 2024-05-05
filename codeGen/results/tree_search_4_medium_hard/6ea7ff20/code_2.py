def mergeable(p):
    n = len(p) // 2
    dp = [[False] * (n + 1) for _ in range(n + 1)]
    memo = [[False] * (n + 1) for _ in range(n + 1)]

    def dfs(i, j):
        if memo[i][j]:
            return False

        if i == 0:
            return True

        if p[i - 1] > p[j]:
            dp[i][j] = any(dfs(i - 1, k) for k in range(j))
        elif p[i - 1] < p[j]:
            dp[i][j] = any(dfs(i - 1, l) for l in range(k + 1, j + 1))
        else:
            dp[i][j] = False

        memo[i][j] = True
        return dp[i][j]

    return "YES" if dfs(n, n) else "NO"

while True:
    n = int(input())
    p = list(map(int, input().split()))
    print(mergeable(p))
