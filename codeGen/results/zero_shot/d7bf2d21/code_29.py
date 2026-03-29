import sys

n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n
max_len = 0
count = 0

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
    max_len = max(max_len, dp[i])

print(sum(1 for x in dp if x == max_len))
