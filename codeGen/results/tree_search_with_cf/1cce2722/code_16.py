import sys
input = sys.stdin.read

def max_points(n, sequence):
    max_val = 105
    count = [0] * (max_val + 1)
    
    # Step 1: Frequency count
    for num in sequence:
        count[num] += 1
    
    # Step 2: Initialize DP array
    dp = [0] * (max_val + 1)
    
    # Step 3: Base cases
    dp[0] = 0
    dp[1] = count[1] * 1
    
    # Step 4: State transition
    for i in range(2, max_val + 1):
        dp[i] = max(dp[i-1], dp[i-2] + count[i] * i)
    
    # Step 5: Result
    return dp[max_val]

if __name__ == "__main__":
    data = input().split()
    n = int(data[0])
    sequence = list(map(int, data[1:]))
    print(max_points(n, sequence))

