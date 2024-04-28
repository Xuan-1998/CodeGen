def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        current_max = 0
        for j in range(min(i, k), -1, -1):
            current_max = max(current_max, arr[j])
            if i >= j + k:
                dp[i] = max(dp[i], current_max * (i - j) + dp[j - k])
            else:
                dp[i] = max(dp[i], current_max * (k - j + 1))
        if i < n and i % k != 0:
            current_max = arr[i]
            dp[i] = max(dp[i], current_max)

    return dp[-1]

# Test the function
arr = list(map(int, input().split()))
k = int(input())
print(maxSumAfterPartitioning(arr, k))
