import sys

# Define the modulo value
MOD = 998244353

def calc_probability(n):
    # Initialize a 2D array to store the dynamic programming table
    dp = [[0] * (n+1) for _ in range(n+1)]

    # Base case: only one town, no signal is possible
    dp[0][0] = 1

    # Fill up the dynamic programming table
    for i in range(1, n):
        for j in range(i+1):
            if j == 0:
                # No signal to town 0
                dp[i][j] = dp[i-1][i]
            elif j == i:
                # Signal to all towns except town i
                dp[i][j] = (dp[i-1][i-1] * (n-i)) % MOD
            else:
                # Signal to some towns between 0 and i-1
                dp[i][j] = ((dp[i-1][j-1] * (n-j+1)) % MOD) + (dp[i-1][j] * (i-j)) % MOD

    # Calculate the probability of finding a valid configuration
    prob = 0
    for j in range(n):
        prob += dp[n][j]
    return prob % MOD

# Read input from stdin
n = int(sys.stdin.readline())

# Calculate and print the result to stdout
print(calc_probability(n))
