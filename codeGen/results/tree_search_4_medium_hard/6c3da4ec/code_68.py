import sys

n = int(input())
s = input()

dp = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(i):
        dp[i] = max(dp[i], dp[j] | (int(s[j:i], 2) & ((1 << (i - j)) - 1)))

print(bin(dp[-1])[2:])
