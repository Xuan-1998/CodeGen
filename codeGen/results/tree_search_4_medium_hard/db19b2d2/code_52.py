import sys

def calculate_probability(n, m, h, s):
    # Calculate the total number of players available
    total_players = sum(s)
    
    if total_players < n:
        return -1.0
    
    # Initialize a 2D array to store the probabilities
    dp = [[0.0] * (n + 1) for _ in range(m + 1)]
    
    # Calculate the probability that a randomly formed team will have at least one player from each department
    for i in range(1, m + 1):
        for k in range(min(k, h), n + 1):
            if s[i - 1] >= k:
                dp[i][k] = max(dp[i-1][k], (s[i-1]/total_players) * (1.0 - sum([dp[j][max(0, k - s[j])] for j in range(i)])))
    
    # Return the probability that a randomly formed team will have at least one player from the department of interest
    return dp[m][n]

# Read input from stdin
n, m, h = map(int, input().split())
s = list(map(int, input().split()))

# Calculate and print the result
result = calculate_probability(n, m, h, s)
print(result)
