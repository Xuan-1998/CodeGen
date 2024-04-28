import sys

MOD = int(1e9) + 7
a, b = map(int, input().split())
dp = [[0] * (len(bin(a)) - 2) for _ in range(len(bin(b)) - 2)]

for i in range(len(bin(a)) - 2):
    for j in range(len(bin(b)) - 2):
        if i == 0:
            dp[i][j] = ((a >> j) & 1) * (b >> j)
        else:
            dp[i][j] = (dp[i-1][0] if j == 0 else dp[i-1][j]) + ((a >> i) & 1) * (b >> (i - 1))
print((sum(sum(row) for row in dp)) % MOD)
