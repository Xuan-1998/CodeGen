MOD = int(1e9) + 7

n, m = map(int, input().split())
a = int(input(), 2)
b = int(input(), 2)

dp = [[0] * (m.bit_length() + 1) for _ in range(n.bit_length() + 1)]

for i in range(1, n.bit_length() + 1):
    for j in range(min(i, m.bit_length()) + 1):
        if j == 0:
            dp[i][j] = (dp[i-1][0] + ((a >> i) & 1)) % MOD
        else:
            dp[i][j] = (dp[i-1][j//2] + ((a >> i) & 1) * ((b >> (i-1)) & 1)) % MOD

print(sum(dp[-1]) % MOD)
