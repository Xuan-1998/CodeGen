import sys
from collections import deque

n = int(input())
s = input()

dp = [[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    dp[i][i] = True  # A single character is always a valid substring

for length in range(2, n+1):
    for i in range(n-length+1):
        j = i + length - 1
        if s[i] == 'A' and s[j] == 'B':
            dp[i][j] = (dp[i+1][j-1] or dp[i+1][j]) and (dp[i][j-1] or dp[i])
        elif s[i] == 'B' and s[j] == 'A':
            dp[i][j] = (dp[i+1][j-1] or dp[i+1][j]) and (dp[i][j-1] or dp[i])
        else:
            dp[i][j] = dp[i][j-1]

if dp[0][n-1]:
    print("YES")
else:
    print("NO")

