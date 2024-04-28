import sys

def partition_sum(arr):
    n = len(arr)
    total_sum = sum(arr)

    if total_sum % 2 != 0:
        return 0

    total_sum //= 2
    dp = [0] * (n + 1)
    prefix_sum = 0

    for i in range(n):
        prefix_sum += arr[i]
        if prefix_sum == total_sum:
            dp[i+1] = max(dp[i+1], dp[i] + 1)
        elif prefix_sum < total_sum and i > 0:
            dp[i+1] = max(dp[i+1], dp[i-1])

    return dp[n]

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(partition_sum(arr))
