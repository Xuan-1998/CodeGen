def maxSubarrayCount(Arr, K):
    N = len(Arr)
    dp = [0] * N  # Initialize dp array with zeros

    for i in range(N):
        if Arr[i] > K:  # If the current element is greater than K
            dp[i] = dp[i-1] + 1 if i == 0 else dp[i-1]
        elif i > 0 and Arr[i] <= K:  # If the current element is not greater than K and it's not the first element
            dp[i] = dp[i-1]

    return sum(dp)  # Return the total count of subarrays that satisfy the condition

# Read input from stdin
N, K = map(int, input().split())
Arr = list(map(int, input().split()))

print(maxSubarrayCount(Arr, K))
