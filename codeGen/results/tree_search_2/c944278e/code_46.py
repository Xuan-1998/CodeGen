import sys

def solve(n, s):
    # Initialize 2D table for dynamic programming
    dp = [[False] * (n + 1) for _ in range(2 ** n)]

    # Iterate through each phase (0 <= j <= n)
    for j in range(n + 1):
        # Calculate the skill level of each team based on the binary string s and the phase number j
        for i in range(2 ** n):
            if ((s >> j) & 1):  # If the ith bit is set in the current phase's result
                dp[i][j] = any(dp[(i << 1) + k][j - 1] and s[k // 2] == (k % 2) for k in range(i * 2, i * 2 + n))  # Check if a team has won up to this phase
            else:  # If the ith bit is not set in the current phase's result
                dp[i][j] = all(dp[(i << 1) + k][j - 1] and s[k // 2] != (k % 2) for k in range(i * 2, i * 2 + n))  # Check if a team has not won up to this phase

    # Identify the winning teams
    winning_teams = [i for i in range(2 ** n) if dp[i][n]]

    return sorted(winning_teams)

# Read input from stdin
n = int(input())
s = bin(int(input()))[2:].zfill(n)

# Print the winning teams to stdout
print(*solve(n, s), sep='\n')
