input = sys.stdin.read

def max_points(n, sequence):
    max_value = 105
    count = [0] * (max_value + 1)
    
    # Populate the frequency array
    for num in sequence:
        count[num] += 1
    
    # Initialize the dp array
    dp = [0] * (max_value + 1)
    
    # Base cases
    dp[0] = 0
    dp[1] = count[1]
    
    # Fill the dp array using the given relation
    for i in range(2, max_value + 1):
        dp[i] = max(dp[i-1], dp[i-2] + count[i] * i)
    
    # The answer will be in dp[105]
    return dp[max_value]

if __name__ == "__main__":
    data = input().split()
    n = int(data[0])
    sequence = list(map(int, data[1:]))
    print(max_points(n, sequence))

