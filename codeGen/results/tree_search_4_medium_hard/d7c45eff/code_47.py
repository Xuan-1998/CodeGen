import sys

n, k = map(int, input().split())
s = input()

dp = [False] * (k + 1)
dp[0] = True

for i in range(1, k + 1):
    if dp[i - 1]:
        if s[i - 1] == min(s[:i]):
            dp[i] = True
        else:
            dp[i] = dp[i - 1]

if dp[k]:
    result = s[:k]
else:
    result = s[:-1]

print(result)
