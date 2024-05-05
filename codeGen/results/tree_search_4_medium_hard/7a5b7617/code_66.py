T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
    for i in range(1, N+1):
        dp[i][0] = 1
        for j in range(1, M+1):
            if j <= M:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % 1000000000
    print(dp[N][M])
