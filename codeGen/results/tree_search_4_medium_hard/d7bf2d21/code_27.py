import sys

n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n

max_length = 0
count = 0

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
    if dp[i] > max_length:
        max_length = dp[i]
    elif dp[i] == max_length:
        count += 1

print(count)
