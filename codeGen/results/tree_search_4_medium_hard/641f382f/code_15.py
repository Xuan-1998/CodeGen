import math
import sys

def main():
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    
    # Check if there's already a 1 in the array
    if 1 in arr:
        print(0)
        return
    
    # Initialize the DP array with infinity
    dp = [[float('inf')] * (max(arr) + 1) for _ in range(n)]
    
    # Set the base case for the DP array
    for g in range(1, max(arr) + 1):
        if math.gcd(arr[0], g) == g:
            dp[0][g] = 0
    
    # Fill the DP table
    for i in range(1, n):
        for g in range(1, max(arr) + 1):
            for h in range(1, max(arr) + 1):
                if math.gcd(arr[i], h) == g:
                    dp[i][g] = min(dp[i][g], dp[i-1][h] + 1)
    
    # Find the minimum number of operations to make all elements equal to 1
    min_operations = min(dp[n-1][1], default=float('inf'))
    print(-1 if min_operations == float('inf') else min_operations)

if __name__ == "__main__":
    main()
