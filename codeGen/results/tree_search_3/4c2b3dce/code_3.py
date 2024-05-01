import sys

n = int(input())
s = input()

dp = [[False, False] for _ in range(n + 1)]

for i in range(n):
    if s[i] == 'A':
        dp[i + 1][0] = True
        dp[i + 1][1] = dp[i][1]
    elif s[i] == 'B' and not dp[i][1]:
        dp[i + 1][0] = False
        dp[i + 1][1] = True
    else:
        dp[i + 1][0] = dp[i][0]
        dp[i + 1][1] = dp[i][1]

print("YES" if dp[n][1] else "NO")
