import sys
from collections import defaultdict

# Read input
t = input()
n = int(input())
s = [input() for _ in range(n)]

dp = [[0] * (len(t) + 1) for _ in range(len(t) + 1)]
mem = [[None] * (len(t) + 1) for _ in range(len(t) + 1)]

# Initialize dp
for i in range(len(t)):
    if t[i] not in [s[j][0] for j in range(n)]:
        dp[i][i+1] = 0
    else:
        dp[i][i+1] = 1

# Fill up the dp table
for length in range(2, len(t) + 1):
    for i in range(len(t) - length + 1):
        j = i + length
        if t[i:j+1] not in [s[j][0] for j in range(n)]:
            dp[i][j] = dp[i][j-1]
        else:
            dp[i][j] = min(dp[i][j-1], dp[i+length][j]) + 1

# Print the answer
if dp[0][-1] == -1:
    print(-1)
else:
    m = dp[0][-1]
    for i in range(m):
        p, w = max(((dp[k][k+m-1], k) for k in range(len(t)-m+1)), key=lambda x: (x[0], x[1]-i))
        print(p, w)
