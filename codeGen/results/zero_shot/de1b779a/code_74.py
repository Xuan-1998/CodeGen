from sys import stdin

n, m = map(int, stdin.readline().split())
dp = [0] * (n + 1)

for _ in range(m):
    ai, bi, ci, di = map(int, stdin.readline().split())
    for i in range(n, bi - 1, -1):
        dp[i] = max(dp[i], dp[i - ci] + di)

print(max(dp))
