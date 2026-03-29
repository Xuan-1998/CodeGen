import sys

n, m, h = map(int, input().split())
s = list(map(int, input().split()))

dp = [[0.0 for _ in range(sum(s) + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][0] = 1.0

for i in range(h, m + 1):
    for j in range(min(i + h - 1, n), -1, -1):
        if j >= i:
            dp[j][i] += dp[j - i][i - 1] * (s[i - 1] / (n - j + 1))
        else:
            dp[j][i] = max(dp[j][i], dp[j][i - 1])

ans = 0.0
for i in range(sum(s), n, -1):
    if sum(s) < i:
        break
    ans += dp[i][sum(s)]

print(ans)
