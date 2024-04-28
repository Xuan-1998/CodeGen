import sys

def winning_teams(n, s):
    # Initialize dp table with zeros
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # Base case: if the binary string is all '1's, then the maximum skill level is 2^n - 1
    max_skill = 2 ** n - 1
    for i in range(1, n + 1):
        dp[i][0] = max_skill

    # Fill up the dp table using the binary string
    for i in range(1, n + 1):
        for j in range(1, min(i, n) + 1):
            if s[i - 1] == '1':
                # If the current team wins, add its skill level to the maximum skill level of the previous teams
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + (2 ** (n - i)))
            else:
                # If the current team loses, just copy the maximum skill level from the previous teams
                dp[i][j] = dp[i - 1][j]

    # Find all winning teams by iterating through the dp table and checking if the maximum skill level is greater than or equal to 2^n - 1
    winning_teams = []
    for i in range(n, 0, -1):
        if dp[i][n] >= (2 ** n) - 1:
            winning_teams.append(i)

    return winning_teams

# Read input from stdin
n = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()

# Print the winning teams to stdout
print(*winning_teams(n, s), sep='\n')
