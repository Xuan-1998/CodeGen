def min_replantings(n, m):
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base case: one section
    for j in range(1, n + 1):
        dp[1][j] = j - m
    
    # Fill up the DP table
    for i in range(2, m + 1):
        for j in range(i, n + 1):
            k = s[j-1]  # species of the current plant
            dp[i][j] = min(dp[i-1][j-1] + (k != i), dp[i][j-1])
    
    return dp[m][n]

# Read input from stdin
n, m = map(int, input().split())
s = [int(x) for x in input().split()]

print(min_replantings(n, m))
