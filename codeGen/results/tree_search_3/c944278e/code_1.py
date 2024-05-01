def find_winning_teams(n, s):
    # Initialize the dp dictionary
    dp = {(0, j): [j] for j in range(2**n)}

    # Iterate over each round
    for i in range(1, n + 1):
        # Update the dp dictionary based on the current round's results
        for j in range(2**n):
            if s[i - 1] == 0:  # Team loses in this round
                dp[(i, j)] = []
            elif s[i - 1] == 1:  # Team wins in this round
                for k in range(2**n):
                    if (k & (1 << i - 1)) > 0 and not dp.get((i - 1, k), []):  # Team is still competing and has not been eliminated yet
                        dp[(i, j)] = [j] + dp.get((i - 1, k), [])

    # Find the winning teams in ascending order
    return sorted([team for teams in dp[(n, :)].values() for team in teams])
