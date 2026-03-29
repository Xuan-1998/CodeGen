def longest_increasing_subsequence(sequence):
    # Initialize a list to store the lengths of LIS ending at each position.
    dp = [1] * len(sequence)
    
    for i in range(1, len(sequence)):
        for j in range(i):
            if sequence[i] > sequence[j]:
                # Update the length of the LIS ending at this position
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)

# Example usage:
sequence = list(map(int, input().split()))
print(longest_increasing_subsequence(sequence))
