def find_winning_teams(n):
    # Initialize a table to store the results of subproblems
    dp = [[[] for _ in range(2**n)] for _ in range(n)]

    # Base case: when n == 1, there's only one winning team
    if n == 1:
        return [[s]]

    # Fill up the table using bottom-up dynamic programming
    for i in range(n):
        for j in range(2**n):
            # Get the result of the current phase
            phase_result = (j >> (n - i - 1)) & 1

            # If this team wins, add all teams that can win in the next round
            if phase_result:
                dp[i][j] = [[j]] + sum(dp[i+1][k] for k in range(2**n) if (k >> (n - i - 1)) & 1)
            # If this team loses, add all teams that can win without advancing to the next round
            else:
                dp[i][j] = [[j]] + sum(dp[i+1][k] for k in range(2**n) if not (k >> (n - i - 1)) & 1)

    # Return the winning teams
    return [team for team in dp[-1][-1]]
