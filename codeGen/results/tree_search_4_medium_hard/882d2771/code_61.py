import sys

t = int(input())
l, r = map(int, input().split())

dp = [0] * (r - l + 1)
for i in range(1, r - l + 1):
    dp[i] = float('inf')

for i in range(l, r + 1):
    for j in range(i):
        dp[i] = min(dp[i], dp[j] + 1)

result = t * (dp[r] - dp[l]) % (10**9 + 7)
print(result)
