def findWinningTeams(n):
    # Base case: when n = 1, there's only one team that can win
    if n == 1:
        return [0]

    # Initialize the table with all zeros (assuming no teams have won yet)
    dp = [[[] for _ in range(2**n)] for _ in range(n)]

    # Fill up the table recursively
    for i in range(n):
        for state in range(2**(n-i-1)):
            # If this is the last round, there's only one team that can win (the current state)
            if i == n-1:
                dp[i][state] = [state]
            else:
                # Recursively fill up the table
                winning_teams = []
                for prev_state in range(2**(n-i)):
                    next_state = state | (prev_state << 1)
                    if dp[i-1][prev_state]:
                        winning_teams.extend(dp[i-1][prev_state])
                dp[i][state] = winning_teams

    # Find all the winning teams
    winning_teams = set()
    for state in range(2**n):
        if dp[n-1][state]:
            winning_teams.update(dp[n-1][state])

    return sorted(list(winning_teams))

# Read input from stdin
n = int(input())

# Print the result to stdout
print(findWinningTeams(n))
