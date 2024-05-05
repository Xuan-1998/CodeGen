import sys

# Define the modulo value
MOD = 10**9 + 7

def beautyContest(t, l, r):
    # Create a 2D array to store the dp values
    dp = [[0] * (r - l + 1) for _ in range(t + 1)]

    # Base case: When there is only one group left
    for i in range(1, t + 1):
        dp[i][0] = i - 1

    # Fill the dp table using bottom-up dynamic programming
    for i in range(1, t + 1):
        for j in range(min(i, r - l), 0, -1):
            dp[i][j] = min(dp[i-1][j-1] + j, dp[max(0, i-j)][j])

    # Return the answer as the value of the expression
    return (t * dp[l][r] % MOD) - (l * dp[r][r] % MOD)

# Receive inputs from stdin and print the answer to stdout
t, l, r = map(int, input().split())
print(beautyContest(t, l, r))
