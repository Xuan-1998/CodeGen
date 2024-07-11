MOD = 998244353
N, M = map(int, input().split())
dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
power = [[0 for _ in range(max(N, M)+1)] for _ in range(max(N, M)+1)]
for i in range(max(N, M)+1):
    power[i][0] = 1
    for j in range(1, max(N, M)+1):
        power[i][j] = power[i][j-1] * 2 % MOD

dp[1][1] = 2
for i in range(1, N+1):
    for j in range(1, M+1):
        if i == 1 and j == 1:
            continue
        dp[i][j] = (dp[i-1][j] * power[j][2] + dp[i][j-1] * power[i][2]) % MOD

print(dp[N][M])

