python
def max_points(n, sequence):
    if n == 0:
        return 0
    
    max_val = max(sequence)
    count = [0] * (max_val + 1)
    
    for num in sequence:
        count[num] += 1
    
    dp = [0] * (max_val + 1)
    dp[1] = count[1]
    
    for i in range(2, max_val + 1):
        dp[i] = max(dp[i-1], dp[i-2] + i * count[i])
    
    return dp[max_val]

# Read input
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
sequence = list(map(int, data[1:]))

# Calculate and print the result
print(max_points(n, sequence))

