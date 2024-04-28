import sys

# Read input from stdin
s = input().strip()

dp = [[False] * (len(s) + 1) for _ in range(len(s) + 1)]

for i in range(len(s)):
    for j in range(i, len(s)):
        if s[i] == 'A' and s[j] == 'B':
            dp[i][j] = True
        elif s[i] == 'B' and s[j] == 'A':
            dp[i][j] = True

for i in range(len(s) + 1):
    for j in range(i, len(s) + 1):
        if not dp[i - 1][j - 1] or (dp[i - 1][j - 1] and s[i - 1] != 'A' and s[j - 1] != 'B'):
            dp[i][j] = True

print("YES" if any(any(dp) for _ in range(len(s))) else "NO")
