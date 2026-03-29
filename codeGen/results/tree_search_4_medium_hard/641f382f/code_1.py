from math import gcd
from sys import stdin

# Function to precompute the gcd of all subarrays
def precompute_gcd(arr, n):
    gcd_precompute = [[0] * n for _ in range(n)]
    for i in range(n):
        gcd_precompute[i][i] = arr[i]
        for j in range(i + 1, n):
            gcd_precompute[i][j] = gcd(gcd_precompute[i][j - 1], arr[j])
    return gcd_precompute

# Main function to solve the problem using dynamic programming
def min_operations_to_make_ones(arr, n):
    # Precompute gcd of all subarrays
    gcd_precompute = precompute_gcd(arr, n)
    
    # Initialize the dp array with -1 representing uncalculated subproblems
    dp = [[-1] * n for _ in range(n)]
    
    # Base case: subarray of length 1 requires 0 operations
    for i in range(n):
        dp[i][i] = 0
    
    # Fill the dp array for subarrays of length greater than 1
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if gcd_precompute[i][j] == 1:
                dp[i][j] = 0
            else:
                dp[i][j] = float('inf')
                for k in range(i, j):
                    if gcd_precompute[i][k] == 1 and gcd_precompute[k + 1][j] == 1:
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + 1)
    
    # If it's impossible to make all elements equal to 1, return -1
    if dp[0][n - 1] == float('inf'):
        return -1
    else:
        return dp[0][n - 1]

# Read input from stdin
n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().strip().split()))

# Call the function and print the result to stdout
print(min_operations_to_make_ones(arr, n))
