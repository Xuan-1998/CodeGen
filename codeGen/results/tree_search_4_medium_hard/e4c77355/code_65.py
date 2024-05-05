def lengthOfLIS(arr):
    n = len(arr)
    dp = [1] * n  # Initialize DP table with ones
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                
    return max(dp)

# Receive input from stdin
arr = list(map(int, input().split()))
print(lengthOfLIS(arr))
