import sys

s = input()

dp = [[False] * 2 for _ in range(len(s) + 1)]

for i in range(1, len(s) + 1):
    if s[i - 1] == 'A':
        dp[i][0] = True
        dp[i][1] = False
    elif s[i - 1] == 'B':
        dp[i][0] = False
        dp[i][1] = True

for i in range(2, len(s) + 1):
    for j in range(2):
        if (j == 0 and s[i - 1] == 'A' and dp[i - 1][1]) or (j == 1 and s[i - 1] == 'B' and dp[i - 1][0]):
            dp[i][j] = True

print("YES" if any(dp[-1][0] and dp[0][1] for _ in range(len(s) + 1)) else "NO")
