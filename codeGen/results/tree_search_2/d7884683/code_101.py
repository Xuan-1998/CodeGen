def max_partitions(arr):
    n = len(arr)
    dp = [1] * n  # Initialize DP array with 1s

    for i in range(1, n):
        left_sum = sum(arr[:i])
        right_sum = sum(arr[i:])

        if left_sum == right_sum:
            dp[i] = max(dp[i-1], dp[i-2] + 1)  # Update DP value
        else:
            dp[i] = dp[i-1]

    return dp[-1]  # Return the maximum number of partitions

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_partitions(arr))
