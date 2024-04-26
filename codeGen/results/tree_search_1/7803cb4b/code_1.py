import sys

def min_length_array(n, a):
    # Initialize the 2D DP array with infinities
    dp = [[float('inf')] * n for _ in range(n)]
    
    # Base case: a subarray with a single element has a length of 1
    for i in range(n):
        dp[i][i] = 1
    
    # Start filling the DP table
    for length in range(2, n + 1):  # subarray lengths from 2 to n
        for i in range(n - length + 1):
            j = i + length - 1
            # Check if the first and last elements can be combined
            if a[i] == a[j]:
                dp[i][j] = min(dp[i][j], dp[i + 1][j - 1] + 1)
            # Check all possible splits of the subarray
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
    
    # The answer is the minimum length of the entire array
    return dp[0][n - 1]

# Read input
n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))

# Get the result and print it
result = min_length_array(n, a)
print(result)
