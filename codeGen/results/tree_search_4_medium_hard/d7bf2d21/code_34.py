def longest_increasing_subsequences(arr):
    n = len(arr)
    dp = [1] * n  # Initialize DP table with values representing the length of the longest increasing subsequences ending at each index

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    max_length = max(dp)
    count = 0
    for i in range(n-1, -1, -1):  # Iterate from right to left
        if dp[i] == max_length:
            count += 1

    return count
