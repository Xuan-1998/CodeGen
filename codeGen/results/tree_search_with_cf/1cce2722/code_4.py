python
def max_points(n, sequence):
    max_val = 105  # Given constraint: 1 ≤ ai ≤ 105
    count = [0] * (max_val + 1)
    
    # Count occurrences of each integer
    for num in sequence:
        count[num] += 1
    
    # Initialize dp array
    dp = [0] * (max_val + 1)
    
    # Base cases
    dp[0] = 0
    dp[1] = count[1]
    
    # Fill dp array using the state transition
    for x in range(2, max_val + 1):
        dp[x] = max(dp[x-1], dp[x-2] + x * count[x])
    
    # The result is the maximum points that can be obtained
    return dp[max_val]

# Read input
import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
sequence = list(map(int, data[1:]))

# Calculate and print the result
print(max_points(n, sequence))

