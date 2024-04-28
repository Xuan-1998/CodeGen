from collections import defaultdict

def maxSumAfterPartitioning(arr, k):
    n = len(arr)
    dp = [0] * (n + 1)

    # Initialize memoization dictionary
    memo = defaultdict(int)

    for i in range(1, n + 1):
        if i <= k:
            # Base case: calculate the maximum value in the current window
            max_val = max(arr[:i])
            dp[i] = max_val
        else:
            # Recalculate the maximum sum considering the last element of the previous subarray and all elements in the current subarray
            for j in range(1, k + 1):
                if i - j >= k:
                    dp[i] = max(dp[i], memo[i - j] + max(arr[i - j:i]))
                else:
                    dp[i] = max(dp[i], arr[i - j:i].pop() + memo[i - j])
        # Update the memoization dictionary
        memo[i] = dp[i]

    return dp[n]
