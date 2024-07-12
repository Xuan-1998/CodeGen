import sys
input = sys.stdin.read

def max_points(n, sequence):
    max_val = 105
    count = [0] * (max_val + 1)
    
    # Frequency count
    for num in sequence:
        count[num] += 1
    
    # Initialize DP array
    dp = [0] * (max_val + 1)
    dp[1] = count[1]
    
    # Transition
    for i in range(2, max_val + 1):
        dp[i] = max(dp[i-1], dp[i-2] + count[i] * i)
    
    # Result
    return dp[max_val]

# Read input
data = input().strip().split()
n = int(data[0])
sequence = list(map(int, data[1:]))

# Get the result
result = max_points(n, sequence)
print(result)

