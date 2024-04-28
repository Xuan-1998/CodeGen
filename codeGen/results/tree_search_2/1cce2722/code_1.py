from sys import stdin

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))

dp = [0] * (n + 1)
for i in range(2, n):
    dp[i] = max(dp[i - 2] + i if i >= 2 else 0, dp[i - 1] + 1 if i > 0 else 0)

print(dp[-1])
