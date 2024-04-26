def max_points(n, sequence):
    # Step 1: Calculate the frequency of each number in the sequence
    max_val = max(sequence)
    freq = [0] * (max_val + 1)
    for num in sequence:
        freq[num] += 1

    # Step 2: Initialize the DP array
    dp = [0] * (max_val + 1)
    
    # Step 3: Base cases
    dp[1] = freq[1]
    
    # Step 4: Fill in the DP table
    for i in range(2, max_val + 1):
        dp[i] = max(dp[i-1], dp[i-2] + i * freq[i])
    
    # Step 5: Return the answer
    return dp[max_val]

# Read input from stdin
n = int(input().strip())
sequence = list(map(int, input().strip().split()))

# Calculate and print the result
print(max_points(n, sequence))
