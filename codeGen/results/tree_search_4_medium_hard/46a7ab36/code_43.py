code = []

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    dp = [[1] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        if 2 * i <= n:
            for j in range(min(m, 2 * i), -1, -1):
                dp[i][j] = sum(dp[k][j-1] for k in range(max(i, n-i), min(2*i, n-1)) if 2*k<=n)
        else:
            for j in range(m, -1, -1):
                dp[i][j] = (dp[2*i % n][j-1]) * n
        dp[i][m] *= n
    
    print(dp[-1][-1]%10**9+7)

