def longest_increasing_subsequence(A):
    n = len(A)
    dp = [1] * n  # Initialize dynamic programming state variables

    for i in range(1, n):
        for j in range(i):
            if A[i] > A[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)  # Return the maximum value in the dynamic programming array
