import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
c = list(map(int, sys.stdin.readline().split()))

dp = [0] * (n + 1)

for i in range(2, n+1):
    dp[i] = max(a[i-1] + dp[i-2], c[i-1] + dp[i-3]) if i > 2 else a[i-1] + dp[i-2]

print(dp[n])
