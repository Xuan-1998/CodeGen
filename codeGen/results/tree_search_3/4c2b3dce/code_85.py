import sys

s = input().strip()

dp = [[False, False] for _ in range(len(s) + 1)]

for i in range(len(s)):
    if s[i] == 'A':
        dp[i + 1][0] = True
    elif s[i] == 'B':
        dp[i + 1][1] = (dp[i][0] and s[i - 1] == 'B') or (dp[i][1] and s[i - 1] == 'A')

if dp[-1][0]:
    print("YES")
else:
    print("NO")
