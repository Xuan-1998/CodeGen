MOD = 998244353
N = int(input())
A = list(map(int, input().split()))

# Initialize DP table
dp = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]
dp[0][0][0] = 1

# DP transition
for i in range(N):
    new_dp = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]
    for j in range(i + 1):
        for k in range(j + 1):
            # New element appears exactly once
            if j + 1 <= A[i]:
                new_dp[j + 1][k + 1] += dp[j][k] * (A[i] - k)
                new_dp[j + 1][k + 1] %= MOD
            # New element appears more than once
            if k <= j and j + 1 <= A[i]:
                new_dp[j + 1][k] += dp[j][k] * k
                new_dp[j + 1][k] %= MOD
            # Existing element appears exactly once
            new_dp[j][k] += dp[j][k] * (j - k + 1)
            new_dp[j][k] %= MOD
            # Existing element appears more than once
            if k <= j:
                new_dp[j][k + 1] += dp[j][k] * (j - k)
                new_dp[j][k + 1] %= MOD
    dp = new_dp

# Final answer
ans = 0
for j in range(1, N + 1):
    for k in range(j + 1):
        ans += dp[j][k]
        ans %= MOD

print(ans)

