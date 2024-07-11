N = int(input())
d = list(map(int, input().split()))
d = [0] + d  # 1-indexed

MOD = 998244353

# DP table
dp = [[0]*(N+1) for _ in range(N+1)]
dp[1][d[1]] = 1

# Prefix sum
prefix = [[0]*(N+1) for _ in range(N+1)]
prefix[1][d[1]] = 1

for i in range(2, N+1):
    for j in range(i, N+1):
        dp[i][j] = prefix[i-1][j-d[i]] % MOD
        prefix[i][j] = (prefix[i-1][j] + dp[i][j]) % MOD

answer = sum(dp[i][j] for i in range(1, N+1) for j in range(i, N+1)) % MOD
print(answer)

