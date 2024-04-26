def max_points(sequence):
    max_val = max(sequence)
    freq = [0] * (max_val + 1)
    
    # Count the frequency of each number in the sequence
    for num in sequence:
        freq[num] += 1
    
    # Initialize the DP array
    dp = [0] * (max_val + 1)
    dp[1] = freq[1]
    
    # Base case for the second number
    if max_val > 1:
        dp[2] = max(dp[1], 2 * freq[2])
    
    # Fill the DP array using the recurrence relation
    for i in range(3, max_val + 1):
        dp[i] = max(dp[i-1], dp[i-2] + i * freq[i])
    
    # The answer is the last element in the DP array
    return dp[max_val]

# Read input from stdin
n = int(input().strip())
sequence = list(map(int, input().strip().split()))

# Calculate and print the answer
print(max_points(sequence))
