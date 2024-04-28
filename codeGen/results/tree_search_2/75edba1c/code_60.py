def count_subarrays(N, K, Arr):
    dp = [0] * N  # Initialize the DP array

    for i in range(N):  # Process each element
        max_val = max(Arr[:i+1])  # Calculate the maximum value seen so far
        if max_val > K:  # Check if the maximum value exceeds K
            dp[i] = i + 1 - sum(1 for j in range(i) if max(Arr[j:i+1]) > K)
        else:
            dp[i] = 0

    return sum(dp)  # Return the total count of subarrays
