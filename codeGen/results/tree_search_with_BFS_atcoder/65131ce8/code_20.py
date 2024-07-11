MOD = 998244353
N = int(input())
d = list(map(int, input().split()))
d = [0] + d
if d[1] != 1 or d[0] != 0:
    print(0)
    exit()
child = [0] * (N + 1)
for i in range(2, N + 1):
    if d[i] == 0:
        child[i - 1] += 1
    else:
        child[i] += 1
dp = [[[0] * 2 for _ in range(N + 1)] for _ in range(N + 1)]
dp[1][1][1] = 1
for i in range(2, N + 1):
    for j in range(i, N + 1):
        for k in range(child[i] + 1):
            if j - k < 0:
                continue
            dp[i][j][0] = (dp[i][j][0] + dp[i - 1][j - k][0] * dp[i][k][1]) % MOD
            dp[i][j][1] = (dp[i][j][1] + dp[i - 1][j - k][1] * dp[i][k][1]) % MOD
        dp[i][j][1] = (dp[i][j][1] + dp[i - 1][j - 1][0]) % MOD
print(sum(dp[N][N]) % MOD)

