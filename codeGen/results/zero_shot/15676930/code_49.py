import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
c = list(map(int, sys.stdin.readline().split()))

dp = [0] * (n + 1)
for i in range(2, n):
    dp[i] = max(dp[i-1], a[i-1] + c[i+1] - b[i])

print(max(dp))
