import sys

def max_partitions(arr):
    n = len(arr)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]

    dp = [[0] * (prefix_sum[n] // 2 + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for right_sum in range((prefix_sum[i] + 1) // 2, -1, -1):
            if prefix_sum[i] - right_sum == right_sum:
                dp[i][right_sum] = max(dp[i-1][right_sum], dp[i-1][right_sum-1] + 1)
            elif i > 0 and right_sum < prefix_sum[i]:
                dp[i][right_sum] = max(dp[i-1][right_sum], dp[i-1][max(0, right_sum - arr[i])] + 1)

    return dp[n][prefix_sum[n] // 2]

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_partitions(arr))
