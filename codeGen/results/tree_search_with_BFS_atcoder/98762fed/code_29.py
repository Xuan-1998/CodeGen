N, M = map(int, input().split())
MOD = 998244353

# Precompute the power of 2 modulo MOD
pow2 = [1]
for _ in range(N * M):
    pow2.append(pow2[-1] * 2 % MOD)

# Initialize the DP array
dp = [[[0] * (M + 1) for _ in range(M + 1)] for _ in range(N + 1)]
dp[0][0][0] = 1

# Fill the DP array
for i in range(N + 1):
    for j in range(M + 1):
        for k in range(j + 1):
            if i > 0:
                for l in range(k + 1):
                    dp[i][j][k] = (dp[i][j][k] + dp[i - 1][j][l] * pow2[k - l + (M - j) * (N - i + 1)]) % MOD
            if j > 0:
                for l in range(k):
                    dp[i][j][k] = (dp[i][j][k] + dp[i][j - 1][l] * pow2[k - l + (N - i) * (M - j)]) % MOD

# Calculate the final answer
answer = sum(dp[N][M][k] for k in range(M + 1)) % MOD
print(answer)

