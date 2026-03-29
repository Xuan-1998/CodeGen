def max_points(n, sequence):
    # Initialize count array
    count = [0] * 106  # Using 106 to handle index 105
    for num in sequence:
        count[num] += 1

    # Initialize dp array
    dp = [0] * 106

    # Base cases
    dp[0] = 0
    dp[1] = count[1]

    # Fill dp array using the transition formula
    for x in range(2, 106):
        dp[x] = max(dp[x-1], dp[x-2] + x * count[x])

    # The result will be in dp[105]
    return dp[105]

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    sequence = list(map(int, data[1:n+1]))
    
    result = max_points(n, sequence)
    print(result)

