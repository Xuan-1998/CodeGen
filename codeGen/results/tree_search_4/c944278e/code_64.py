def count_winning_teams(n, s):
    # Initialize a 2D table with (n+1) rows and 2^(n-1) columns
    dp = [[0] * (1 << n) for _ in range(n + 1)]

    # Base case: when there are no more teams to consider
    def dfs(i, state):
        if i == n:
            return [state]
        if dp[i][state]:
            return dp[i][state]

        result = []
        if s[i - 1] == 'W':  # Current team wins
            for next_state in range(2**n):
                if (state & next_state) != state:  # Next team is the loser
                    result.extend(dfs(i + 1, state | next_state))
        else:  # Current team loses
            for next_state in range(2**n):
                if (state & next_state) == state:  # Next team is the winner
                    result.extend(dfs(i + 1, state | next_state))

        dp[i][state] = [x[0] for x in set(tuple(sorted(x)) for x in result)]
        return dp[i][state]

    # Main function to count winning teams
    winning_teams = dfs(1, 0)

    # Sort and print the results
    winning_teams.sort()
    for i in winning_teams:
        print(i)
