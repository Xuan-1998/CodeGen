MOD = 998244353
N = int(input())
d = list(map(int, input().split()))
if d[0] != 1 or d.count(0) > 1:
    print(0)
else:
    dp = [[[0]*(N+1) for _ in range(N+1)] for _ in range(N+1)]
    dp[1][0][1] = 1
    for i in range(2, N+1):
        for j in range(i):
            for k in range(1, i+1):
                if j > 0:
                    dp[i][j][k] = dp[i-1][j-1][k-1]
                if j < i-1:
                    dp[i][j][k] = (dp[i][j][k] + dp[i-1][j+1][k] + dp[i-1][j][k]*(j+1)) % MOD
    ans = 0
    for i in range(1, N+1):
        ans = (ans + dp[N][0][i]*i) % MOD
    print(ans)

