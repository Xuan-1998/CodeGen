def max_points(n, sequence):
    # Step 1: Count Frequency
    max_value = max(sequence)
    count = [0] * (max_value + 1)
    for num in sequence:
        count[num] += 1
    
    # Step 2: Initialize DP Array
    dp = [0] * (max_value + 1)
    
    # Step 3: Base Cases
    dp[0] = 0
    dp[1] = count[1]
    
    # Step 4: Transition
    for x in range(2, max_value + 1):
        dp[x] = max(dp[x-1], dp[x-2] + x * count[x])
    
    # Step 5: Result
    return dp[max_value]

# Read input
import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
sequence = list(map(int, data[1:]))

# Get the result
result = max_points(n, sequence)

# Print the result
print(result)

