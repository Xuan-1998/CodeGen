import sys

mod = 998244353

n = int(sys.stdin.readline())

dp = [[0] * (10 + n) for _ in range(2*n+1)]

cum_sum = [0] * (n + 1)

for i in range(n, -1, -1):
    cum_sum[i] = cum_sum[i-1]
    if i < n:
        for j in range(min(i+1, n), 0, -1):
            cum_sum[j] += dp[i][j-1]

# Initialize base case
dp[0][1] = 1

for i in range(2*n+1):
    for j in range(2, min(i+1, n)+1):
        if (i + 1) % j == 0:
            dp[i][j] += dp[i-j][j-1]
        else:
            dp[i][j] += 1

result = []
for i in range(1, n+1):
    total_blocks = cum_sum[n] - cum_sum[n-i]
    result.append((total_blocks % mod) if total_blocks > 0 else 0)

print(' '.join(map(str, result)))
