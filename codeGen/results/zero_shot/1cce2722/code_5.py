from collections import Counter
import sys

def max_points(n, sequence):
    # Step 1: Frequency Count
    freq = Counter(sequence)
    max_value = max(sequence)
    
    # Step 2: Dynamic Programming Array
    dp = [0] * (max_value + 1)
    
    # Step 3: Base Cases
    dp[1] = freq.get(1, 0)
    
    # Step 4: DP Transition
    for i in range(2, max_value + 1):
        dp[i] = max(dp[i-1], dp[i-2] + i * freq.get(i, 0))
    
    # Step 5: Result
    return dp[max_value]

# Read input from stdin
n = int(input().strip())
sequence = list(map(int, input().strip().split()))

# Calculate and print the result
print(max_points(n, sequence))
