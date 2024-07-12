python
def max_points(n, sequence):
    # Step 1: Frequency Array Calculation
    max_val = 105
    freq = [0] * (max_val + 1)
    
    for num in sequence:
        freq[num] += 1
    
    # Step 2: Initialize DP array
    dp = [0] * (max_val + 1)
    
    # Step 3: Base Cases
    dp[1] = freq[1]
    
    # Step 4: Bottom-Up Calculation
    for i in range(2, max_val + 1):
        dp[i] = max(dp[i-1], dp[i-2] + freq[i] * i)
    
    # Step 5: Result Extraction
    return dp[max_val]

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    sequence = list(map(int, data[1:]))
    
    print(max_points(n, sequence))

