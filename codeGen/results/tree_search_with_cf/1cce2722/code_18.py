def max_points(n, sequence):
    # Step 1: Frequency Count
    max_val = 105
    count = [0] * (max_val + 1)
    for num in sequence:
        count[num] += 1
    
    # Step 2: Bottom-Up Strategy with Tabulation
    dp = [0] * (max_val + 1)
    
    # Step 3: Base Cases
    dp[0] = 0
    dp[1] = count[1] * 1
    
    # Step 4: Iteration using State Expression
    for i in range(2, max_val + 1):
        dp[i] = max(dp[i-1], dp[i-2] + count[i] * i)
    
    # Step 5: Result
    return dp[max_val]

# Input and Output handling
import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
sequence = list(map(int, data[1:]))

# Compute and print the result
print(max_points(n, sequence))

