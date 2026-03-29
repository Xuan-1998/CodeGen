def longest_increasing_subsequence(seq):
    n = len(seq)
    dp = [1] * n  # initialize dp array

    for i in range(1, n):
        for j in range(i):
            if seq[i] > seq[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Example usage:
input_array = [3, 4, -1, 5]
print(longest_increasing_subsequence(input_array))  # Output: 3
