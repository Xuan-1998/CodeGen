import sys

def min_time_to_eat_candies(n, s, k, r, c):
    # Initialize the DP table with a large number
    dp = [[[float('inf')] * 3 for _ in range(k + 1)] for _ in range(n + 1)]
    color_map = {'R': 0, 'G': 1, 'B': 2}
    
    # Base case: at the starting position with 0 candies eaten
    for color in range(3):
        dp[s][0][color] = 0

    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(k + 1):
            for l in range(3):
                if j - r[i - 1] >= 0 and color_map[c[i - 1]] != l:
                    dp[i][j][color_map[c[i - 1]]] = min(dp[i][j][color_map[c[i - 1]]], dp[i][j - r[i - 1]][l])

                if i - 1 > 0:
                    dp[i][j][l] = min(dp[i][j][l], dp[i - 1][j][l] + 1)

                if i + 1 <= n:
                    dp[i][j][l] = min(dp[i][j][l], dp[i + 1][j][l] + 1)

    # Find the minimum time to eat at least k candies
    result = min(dp[i][k][l] for i in range(1, n + 1) for l in range(3))
    
    return -1 if result == float('inf') else result

# Read input from stdin
n, s, k = map(int, input().split())
r = list(map(int, input().split()))
c = input().strip()

# Calculate and print the result
print(min_time_to_eat_candies(n, s, k, r, c))
