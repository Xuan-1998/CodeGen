===BEGIN CODE===
import sys

n, k = map(int, input().split())
s = input()

dp = [[[] for _ in range(k+1)] for _ in range(n+1)]

for i in range(n+1):
    dp[i][0] = [''] * (i+1)
    
for i in range(1, n+1):
    for j in range(min(i, k)+1):
        if s[i-1] <= s[j-1]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = (dp[i-1][j-1] + [s[i-1]])[:j+1]

print(''.join(dp[n][k]))
===END CODE===
