import sys

n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().strip()))

dp = [[0] * (2**n) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(2**n):
        if s[i - 1] == (j >> (n - i)):
            # Team j is winning in this phase
            dp[i][j] = dp[i - 1][j]
        else:
            # Team j is not winning in this phase
            dp[i][j] = sum(dp[i - 1][k] for k in range(2**n) if (k & ((2**i) - 1)) == 0)

winners = [i for i, count in enumerate(dp[-1]) if count > 0]
print(*winners)
