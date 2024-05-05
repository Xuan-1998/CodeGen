def min_operations(p):
    n = len(p)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 0

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if p[i] * p[i+1] * p[j] > 0:
                dp[i][j] = float('inf')
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + p[i] * p[k+1] * p[j])
            else:
                dp[i][j] = 0

    return str(dp[0][n-1])

p = list(map(int, input().split()))
print(min_operations(p))
