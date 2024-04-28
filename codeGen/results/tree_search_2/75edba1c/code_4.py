def count_subarrays(arr, K):
    n = len(arr)
    dp = [0] * (n + 1)  # Initialize DP array with zeros

    max_element = arr[0]
    for i in range(1, n):
        if arr[i] > K and max_element <= K:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = dp[i-1]
        max_element = max(max_element, arr[i])

    return sum(dp) - dp[0]

# Example usage:
N, K = map(int, input().split())
arr = list(map(int, input().split()))
print(count_subarrays(arr, K))
