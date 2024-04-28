import sys

a = int(input(), 2)
b = int(input(), 2)

mod = 10**9 + 7
dp = [[0] * (20) for _ in range(20)]

for i in range(20):
    dp[i][0] = a ^ (1 << i)

result = 0
for bit in range(19, -1, -1):
    result += dp[bit][b & ((1 << bit) - 1)]
    result %= mod

print(result)
