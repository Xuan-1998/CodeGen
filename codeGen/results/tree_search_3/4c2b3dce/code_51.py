import sys

s = input().strip()

n = len(s)

dp = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(i+1):
        if s[j:i+1].count('A') == s[j:i+1].count('B'):
            dp[i][j] = (s[j:i+1].find('AB') != -1 and s[j:i+1].find('BA') != -1)
        else:
            dp[i][j] = False

print("YES" if any(all(dp[i][j]) for i in range(n) for j in range(i+1)) else "NO")
