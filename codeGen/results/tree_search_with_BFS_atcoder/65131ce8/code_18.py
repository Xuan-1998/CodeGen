def solve():
    N = int(input())
    d = list(map(int, input().split()))
    MOD = 998244353

    dp = [[[0, 0] for _ in range(N+1)] for _ in range(N+1)]
    dp[0][0][0] = 1

    for i in range(1, N+1):
        dp[i][0][0] = 1
        dp[i][1][1] = 1
    
    for i in range(1, N):
        for j in range(i+1):
            for k in range(j+1):
                dp[i+1][j+1][0] = (dp[i+1][j+1][0] + dp[i][j][0]*dp[i][k][1]) % MOD
                dp[i+1][j+1][1] = (dp[i+1][j+1][1] + dp[i][j][0]*dp[i][k][1]) % MOD
                if k >= d[i]:
                    dp[i+1][j+1][1] = (dp[i+1][j+1][1] + dp[i][j][1]*dp[i][k][1]) % MOD

    ans = 0
    for j in range(1, N+1):
        ans = (ans + dp[N][j][1]) % MOD
    
    print(ans)

solve()

