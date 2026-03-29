import sys

n = int(sys.stdin.readline())

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
c = list(map(int, sys.stdin.readline().split()))

dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = max(a[i - 1], b[i - 1] + dp[i - 2], c[i - 1] + dp[i - 3])

print(dp[n])
