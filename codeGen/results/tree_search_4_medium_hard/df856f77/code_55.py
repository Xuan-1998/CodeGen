import sys

n = int(input())
arr = list(map(int, input().split()))
dp = [0] + [sys.maxsize] * (n - 1)

for i in range(1, n):
    dp[i] = min(dp[i-1], arr[i-1] == arr[i]) and dp[i-1]

print(min(dp))
