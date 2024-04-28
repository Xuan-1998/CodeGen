import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
dp = [1] * (n + 1)
max_points = 0
for i in range(2, n):
    dp[i] = max(dp[i - 1], dp[i - 2] + 1 if a[i - 2] == a[i] else 1)
max_points = max(dp[:])
print(max_points)
