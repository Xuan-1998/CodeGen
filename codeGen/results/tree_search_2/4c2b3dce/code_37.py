import sys

s = input().strip()
n = len(s)

dp = [False for _ in range(n+1)]

for i in range(1, n+1):
    if s[i-1] == 'A':
        dp[i] = not dp[i-1]
    else:
        dp[i] = dp[i-1]

print('YES' if any(dp[i:i+2]) and all(dp[:i] or dp[i:]) for i in range(n)) or print('NO')
