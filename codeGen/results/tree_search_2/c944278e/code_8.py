import sys

def solve(n, s):
    # Create a table to store solutions
    dp = [[[] for _ in range(2**n)] for _ in range(n+1)]

    # Base case: when n = 0, there are no winning teams
    dp[0][0] = []

    # Fill up the table by considering each possible team and its corresponding skill level
    for i in range(1, n+1):
        for j in range(2**i):
            if s[j-1]:
                dp[i][j] = dp[i-1][j>>1]
            else:
                dp[i][j] = dp[i-1][j>>1 | 1]

    # Find all the winning teams
    winning_teams = set()
    for j in range(2**n):
        if s[j]:
            winning_teams.add(dp[n][j])
        else:
            winning_teams.add(dp[n][j]^((1<<n)-1))

    # Print the winning teams in ascending order
    print('\n'.join(map(str, sorted(list(winning_teams)))))

# Read input from stdin
n = int(input())
s = bin(int(input()))[2:]

# Solve the problem and print the output to stdout
solve(n, s)
