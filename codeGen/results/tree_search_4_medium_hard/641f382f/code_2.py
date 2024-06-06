import math
import sys

def main():
    # Read the number of elements in the array
    n = int(input().strip())
    
    # Read the elements of the array
    arr = list(map(int, input().strip().split()))
    
    # Initialize the dp array with infinity
    dp = [[float('inf')] * n for _ in range(n)]
    
    # Initialize the gcd array
    gcd = [[0] * n for _ in range(n)]
    
    # Precompute the GCD for all possible subarrays
    for i in range(n):
        gcd[i][i] = arr[i]
        for j in range(i + 1, n):
            gcd[i][j] = math.gcd(gcd[i][j - 1], arr[j])
    
    # Fill in the dp array using a bottom-up approach
    for i in range(n):
        dp[i][i] = 0 if arr[i] == 1 else float('inf')
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if gcd[i][j] == 1:
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + 1)
    
    # The answer is in dp[0][n-1]
    result = dp[0][n-1]
    
    # If it's not possible to make all elements equal to 1, print -1
    if result == float('inf'):
        print(-1)
    else:
        print(result)

if __name__ == "__main__":
    main()
