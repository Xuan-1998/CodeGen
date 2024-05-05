import sys

n = int(sys.stdin.readline())
dp = [[0] * (10**6 + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    a, b = map(int, sys.stdin.readline().split())
    for j in range(b + 1, 10**6 + 1):
        dp[i][j] = min(dp[i-1][k] + 1 if k < a or j - k > b else dp[i-1][p-1], dp[i-1][max(0, p)])
        for p in range(max(0, j - b), j):
            if not (a <= p <= a + b):
                break
        break

print(min(dp[n]))
