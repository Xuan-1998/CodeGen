import sys

def beautycontest(t, l, r):
    MOD = 10**9 + 7
    
    # Initialize the DP table with zeros
    dp = [[0] * (r - l + 1) for _ in range(t + 1)]
    
    # Base case: when there's only one group left (n == 1 or k == 1)
    for i in range(t + 1):
        if i <= 1:
            dp[i][0] = 0
    
    # Fill up the DP table using the transition relationship
    for n in range(2, l + r + 1):
        for k in range(min(n, r - l + 1)):
            dp[n][k] = min((dp[n-1][k-1] if k > 0 else 0) + k, dp[n-k][k])
    
    # Calculate the value of the expression
    res = sum(t * dp[r][i] for i in range(r - l + 1)) - l * dp[r][r-l]
    
    return int(res % MOD)

# Read input from standard input
t, l, r = map(int, input().split())

# Print the answer to standard output
print(beautycontest(t, l, r))
