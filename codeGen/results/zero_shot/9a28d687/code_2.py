import sys

n = int(sys.stdin.readline())
costs = [int(x) for x in sys.stdin.readline().split()]
strings = [sys.stdin.readline().strip() for _ in range(n)]

dp = [[0] * 2 for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(2):
        dp[i][j] = dp[i - 1][j] + costs[i - 1]
        if j == 0:
            dp[i][j] += sum([len(s) for s in strings[:i]])

ans = float('inf')
for i in range(n, 0, -1):
    for j in range(2):
        if dp[i][j] < ans:
            ans = dp[i][j]

print(ans if ans != float('inf') else -1)
