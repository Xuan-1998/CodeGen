python
import sys
input = sys.stdin.read

def max_points(n, sequence):
    if n == 0:
        return 0
    
    max_value = 105  # Given constraint that 1 ≤ ai ≤ 105
    frequency = [0] * (max_value + 1)
    
    # Count frequencies
    for num in sequence:
        frequency[num] += 1
    
    # Initialize dp array
    dp = [0] * (max_value + 1)
    
    # Base cases
    dp[0] = 0
    dp[1] = frequency[1]
    
    # Fill dp array using the state transition relation
    for x in range(2, max_value + 1):
        dp[x] = max(dp[x-1], dp[x-2] + x * frequency[x])
    
    # The result is the maximum points that can be obtained
    return dp[max_value]

if __name__ == "__main__":
    data = input().split()
    n = int(data[0])
    sequence = list(map(int, data[1:]))
    print(max_points(n, sequence))

