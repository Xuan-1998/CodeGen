import sys

def min_time_to_eat_candies(n, s, k, r, colors):
    # Initialize the DP table with infinity
    dp = [[[float('inf')] * 3 for _ in range(k+1)] for _ in range(n+1)]
    
    # Mapping from color to index
    color_to_idx = {'R': 0, 'G': 1, 'B': 2}
    
    # Base case: Tanya has not eaten any candies
    for i in range(3):
        dp[s][0][i] = 0
    
    # Fill in the DP table
    for candies in range(1, k+1):
        for i in range(1, n+1):
            for c in range(3):
                # Try moving from the left neighbor
                if i > 1:
                    dp[i][candies][c] = min(dp[i][candies][c], dp[i-1][candies][c] + 1)
                # Try moving from the right neighbor
                if i < n:
                    dp[i][candies][c] = min(dp[i][candies][c], dp[i+1][candies][c] + 1)
                # Try eating from the current box if it's possible
                if candies >= r[i] and color_to_idx[colors[i-1]] != c:
                    for last_c in range(3):
                        if last_c != c:
                            dp[i][candies][c] = min(dp[i][candies][c], dp[i][candies - r[i]][last_c] + 1)
    
    # Find the minimum time to eat at least k candies
    result = min(dp[i][k][c] for i in range(1, n+1) for c in range(3))
    
    return -1 if result == float('inf') else result

# Read input from stdin
n, s, k = map(int, sys.stdin.readline().split())
r = list(map(int, sys.stdin.readline().split()))
colors = sys.stdin.readline().strip()

# Calculate and print the result
print(min_time_to_eat_candies(n, s, k, r, colors))
