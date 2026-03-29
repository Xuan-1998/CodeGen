import sys

k = int(input())
s = input()

dp = [False] * (k + 1)
dp[0] = True

for i in range(1, k + 1):
    if s[i - 1] <= s[-1]:
        dp[i] = dp[i - 1]
    else:
        dp[i] = dp[i - 2] or dp[i - 1]

if dp[k]:
    print(s)
else:
    print(s[:-1])
