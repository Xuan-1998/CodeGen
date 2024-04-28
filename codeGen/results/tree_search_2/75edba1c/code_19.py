def max_subarray_count(N, K, Arr):
    dp = [0] * N  # Initialize dynamic programming array
    max_elements = set()  # Set to store maximum elements seen so far

    for i in range(N):
        curr_max = max(Arr[:i+1])  # Update current maximum element
        if curr_max > K:
            dp[i] = sum(dp[j-1] for j in range(i) if max_elements.add(Arr[j]) and Arr[j] > K)
        max_elements.add(curr_max)

    return sum(dp)
