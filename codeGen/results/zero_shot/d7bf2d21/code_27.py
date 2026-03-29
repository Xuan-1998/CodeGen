import sys

# Read input array from stdin
arr = list(map(int, input().split()))

n = len(arr)
dp = [0] * n  # Initialize dynamic programming table
max_length = 0

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
    max_length = max(max_length, dp[i])

count = sum(1 for i in range(n) if dp[i] == max_length)
print(count)
