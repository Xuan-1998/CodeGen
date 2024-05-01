code
n = int(input())
arr = list(map(int, input().split()))
k = int(input())

dp = [0] * (n + 1)
max_sum = 0
for i in range(k, n + 1):
    max_sum = max(max_sum, dp[i-k])
    dp[i] = max(dp[i-1], 0) + max(arr[i-k:i])

print(max_sum)
