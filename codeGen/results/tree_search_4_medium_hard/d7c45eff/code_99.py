import sys

n, k = map(int, input().split())
s = input()

dp = [[False] * (k + 1) for _ in range(n + 1)]

dp[0][0] = True

for i in range(1, n + 1):
    for j in range(min(i, k) + 1):
        if j < k:
            dp[i][j] = any(dp[i-1][j-1] and (s[j-1] <= s[-1]) or dp[i-1][j], end="")
        elif j == k:
            dp[i][k] = s[:i].count(s[-1]) >= k
        if dp[i][j]:
            break
    else:
        continue

if not dp[n][k]:
    print("Not Found")
else:
    print(s[:k])
