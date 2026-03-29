import sys

n = int(input())
s = input()

dp = [0] * (n + 1)
for i in range(2, n + 1):
    dp[i] = 0
    for j in range(i):
        dp[i] = max(dp[i], dp[j] | (int(s[i-1]) << (i-j)))
print(bin(max(dp))[2:])
