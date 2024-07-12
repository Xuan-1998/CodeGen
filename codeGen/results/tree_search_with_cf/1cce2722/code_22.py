python
import sys
input = sys.stdin.read

def max_points(n, sequence):
    if n == 0:
        return 0
    
    max_val = max(sequence)
    
    # Step 1: Count Frequencies
    count = [0] * (max_val + 1)
    for num in sequence:
        count[num] += 1
    
    # Step 2: Initialize DP Array
    dp = [0] * (max_val + 1)
    
    # Step 3: Base Cases
    dp[0] = 0
    dp[1] = count[1]
    
    # Step 4: Fill DP Array
    for i in range(2, max_val + 1):
        dp[i] = max(dp[i-1], dp[i-2] + i * count[i])
    
    # Step 5: Result
    return dp[max_val]

if __name__ == "__main__":
    data = input().split()
    n = int(data[0])
    sequence = list(map(int, data[1:]))
    print(max_points(n, sequence))

