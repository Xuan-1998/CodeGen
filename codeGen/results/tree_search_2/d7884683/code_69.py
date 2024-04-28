import sys

def max_partitions(arr):
    n = len(arr)
    total_sum = sum(arr)

    # Precompute cumulative sums
    cum_sums = [0] * (n + 1)
    for i in range(n):
        cum_sums[i + 1] = cum_sums[i] + arr[i]

    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            left_sum = cum_sums[j] - cum_sums[i - 1]
            right_sum = total_sum - left_sum

            if left_sum == right_sum:
                dp[i][j] = max(dp[i - 1][j - 1], 1) + (j - i)
            else:
                dp[i][j] = max(dp[i - 1][j - 1], 0)

    return dp[1][n]

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_partitions(arr))
