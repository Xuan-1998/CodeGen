def max_points(n, sequence):
    # Step 1: Create a frequency array
    max_val = 105
    count = [0] * (max_val + 1)
    
    for num in sequence:
        count[num] += 1
    
    # Step 2: Initialize the dp array
    dp = [0] * (max_val + 1)
    dp[1] = count[1]
    
    # Step 3: Fill the dp array using the state expression
    for i in range(2, max_val + 1):
        dp[i] = max(dp[i-1], dp[i-2] + count[i] * i)
    
    # Step 4: The result is in dp[max_val]
    return dp[max_val]

# Input handling
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
sequence = list(map(int, data[1:]))

# Print the result
print(max_points(n, sequence))

