import sys

def max_score(array, k, z):
    n = len(array)
    dp = [[0] * (z + 1) for _ in range(n)]
    
    # Initialize the base case: no moves have been performed yet.
    dp[0][0] = array[0]
    
    for i in range(1, n):
        dp[i][0] = array[i]
        
        for j in range(1, min(k + 1, z) + 1):
            # Compute the maximum score for processing the first i-1 elements and performing j-1 moves.
            prev_max = dp[i - 1][j - 1]
            
            # Consider the possibility of making one move to the left from the current position.
            if j <= z:
                left_max = array[i - 1] + dp[i - 2][min(j - 2, z)]
                dp[i][j] = max(prev_max, left_max)
            else:
                # If we've reached or exceeded the allowed number of moves to the left, just consider the previous maximum.
                dp[i][j] = prev_max
    
    return dp[n - 1][min(k + 1, z)]

# Read input
t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    array = list(map(int, input().split()))
    
    # Solve the problem and print the answer.
    print(max_score(array, k, z))
