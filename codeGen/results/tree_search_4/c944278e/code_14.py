import sys
from collections import defaultdict

n = int(sys.stdin.readline())
dp = [[-1 for _ in range(2**n)] for _ in range(n+1)]

for i in range(n+1):
    dp[i][0] = 1

for i in range(1, n+1):
    for j in range(2**i):
        if j % 2 == 0:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = sum(dp[i-1][k] for k in range(2**i) if (j ^ k) < j)

winning_teams = [i for i in range(2**n) if dp[n][i] >= 0]

print("\n".join(map(str, winning_teams)))
