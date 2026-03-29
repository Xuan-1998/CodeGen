mod = 10**9 + 7

dp = [[[0 for _ in range(C+1)] for _ in range(N+M+1)] for _ in range(C+1)]
dp[0][j] = 1

for i in range(1, C+1):
    for j in range(min(i, N), M+1):
        dp[i][j] = (sum(dp[i-1][:j+1]) % mod) if i > 1 else 0
print(*[str(int(x)) for x in [dp[C][M]]], sep=' ')
