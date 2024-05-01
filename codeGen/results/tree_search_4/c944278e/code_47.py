import sys

def winning_teams(n):
    # Create a 2D array dp where dp[i][j] represents the winning teams for the first i phases, with j being the skill level of the team.
    dp = [[set() for _ in range(2**n)] for _ in range(n + 1)]
    
    # Initialize the 2D array dp with zeros. For each phase i from 0 to n-1:
    for i in range(n):
        for j in range(2**n):
            if (j >> i) & 1:  # If the ith bit of binary representation of j is 1
                # Find the winning teams for the previous phases (i.e., up to phase i-1) using memoization.
                dp[i+1][j] = set.intersection(dp[i][j], {k for k in range(2**n) if (k >> (i - 1)) & 1 and not dp[i][k]})
    
    # To find the final winning teams, iterate over all possible skill levels j from 0 to 2^n - 1.
    winning_teams = [j for j in range(2**n) if all((j >> i) & 1 for i in range(n))]
    
    return sorted(winning_teams)

# Read input
n = int(input())

# Print output
print(*winning_teams(n), sep='\n')

