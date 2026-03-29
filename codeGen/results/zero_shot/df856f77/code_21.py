import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dp = [0] * n

for i in range(1, n):
    if arr[i] <= arr[i-1]:
        dp[i] = 1 + dp[i-1]
    else:
        dp[i] = dp[i-1]

print(dp[-1])
