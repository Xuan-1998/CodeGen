[,
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    dp = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        if 2*i <= n:
            dp[i][j] = min((1 + dp[i-1][min(j, 2*i%n)]) if j>0 else 1,
                            (i==n//2) * n if j==m-1 else 0)
        else:
            dp[i][j] = 1
    print((dp[-1][-1]) % (10**8+7))
