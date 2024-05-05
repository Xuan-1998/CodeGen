import sys

n, k = map(int, input().split())
s = input()

dp = [False] * (k + 1)
dp[0] = True

for j in range(1, k + 1):
    if dp[j - 1]:
        dp[j] = any(s[i] <= s[-1] for i in range(max(0, j - 2), n))
    elif j >= 2:
        dp[j] = dp[j - 2]

if dp[k]:
    print(s[:k])
else:
    print("N/A")
