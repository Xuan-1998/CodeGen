===BEGIN SOLUTION===
from sys import stdin

s = stdin.readline().strip()
n = len(s)

# Initialize the DP table with all False values
dp = [[False] * (n + 1) for _ in range(n + 1)]

# dp[i][j] represents whether the substring from index i to j contains both "AB" and "BA"
for i in range(n):
    if s[i] == 'A':
        dp[i][i+2] = True
    elif s[i] == 'B':
        dp[i][i+1] = True

# Transition relationships:
for i in range(1, n + 1):
    for j in range(i + 1):
        if (s[j-1] == 'A' and s[j] == 'B'):
            dp[j][j+i-2] = dp[j-1][i+1]
        elif (s[j-1] == 'B' and s[j] == 'A'):
            dp[j][j+i-2] = dp[j-1][i+1]

# Print the result
result = "YES" if dp[0][n-1] else "NO"
print(result)
===END SOLUTION===
