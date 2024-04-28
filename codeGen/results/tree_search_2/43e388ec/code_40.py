import sys

# Read input from stdin
a = int(input(), 2)
b = int(input(), 2)

n = 314159
mod = 10**9 + 7
dp = [[0] * 32 for _ in range(n + 1)]

for i in range(n + 1):
    if i == 0:
        dp[i][0] = 1
    else:
        prev = (a >> (i - 1)) & 1
        for j in range(31, -1, -1):
            dp[i][j] = (dp[i-1][j] if j >= prev else dp[i-1][j+prev-prev]) ^ ((b >> j) & 1)
            if j:
                dp[i][j] %= mod
        dp[i][0] = (a & 1) ^ ((b >> 30) & 1)

ans = sum(dp[i][-1] for i in range(n + 1)) % mod

# Print the answer to stdout
print(ans)
