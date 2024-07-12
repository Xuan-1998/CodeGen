import sys
input = sys.stdin.read

def max_points(n, sequence):
    if n == 1:
        return sequence[0]
    
    # Find the maximum value in the sequence
    max_val = max(sequence)
    
    # Create a frequency array
    count = [0] * (max_val + 1)
    for num in sequence:
        count[num] += 1
    
    # Initialize the dp array
    dp = [0] * (max_val + 1)
    dp[1] = count[1]
    
    # Fill the dp array using the transition relationship
    for x in range(2, max_val + 1):
        dp[x] = max(dp[x-1], dp[x-2] + x * count[x])
    
    # The result is the maximum points that can be obtained
    return dp[max_val]

# Read input
data = input().split()
n = int(data[0])
sequence = list(map(int, data[1:]))

# Calculate and print the result
print(max_points(n, sequence))

