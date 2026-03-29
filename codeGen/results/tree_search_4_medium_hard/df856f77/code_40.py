import sys

n = int(input())
arr = list(map(int, input().split()))

dp = [0] * n
for i in range(1, n):
    dp[i] = float('inf')
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = min(dp[i], dp[j] + (i - j))
print(dp[-1])
