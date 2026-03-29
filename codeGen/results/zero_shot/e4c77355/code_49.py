def longest_increasing_subsequence(array):
    n = len(array)
    dp = [1] * n  # Initialize dp array with all 1's

    for i in range(1, n):
        for j in range(i):
            if array[i] > array[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)
