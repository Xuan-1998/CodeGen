import sys

def team_probability(n, m, h, s):
    # Initialize the DP table with zeros.
    dp = [[0.0] * (m + 1) for _ in range(n + 1)]

    # Base case: If there are fewer players than departments,
    # it's impossible to form a team with at least one player from each department.
    for i in range(n + 1):
        dp[i][0] = 1.0 if i >= h else 0.0

    # For larger teams, iterate through each department and update the probability.
    for j in range(1, m + 1):
        for i in range(h - 1, n + 1):
            dp[i][j] = max(dp[k][j - 1] * (s[j - 1] / sum(s)) for k in range(min(i, h), h))

    # If there are not enough basketball players to form a team, output -1.
    if sum(s) < n:
        return -1.0

    return dp[n][m]

# Read input from stdin and calculate the result
n, m, h = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))
print("{:.6f}".format(team_probability(n, m, h, s)))
