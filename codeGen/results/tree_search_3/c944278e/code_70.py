def find_winning_teams(n, s):
    dp = [[0] * 2 for _ in range(n + 1)]
    winning_teams = set()

    # Initialize base case: only one team left, it's the sole winner
    dp[0][0] = 1

    for i in range(n):
        for k in range(2):
            if s[i] == str(k):  # if the current phase is won/lost by this team
                for j in range(2):
                    if (dp[i][j] and team_j_skill_level <= k) or not dp[i][k]:  # condition for winning/losing teams
                        dp[i + 1][k] += dp[i][j]
            else:
                dp[i + 1][k] = dp[i][k]

        if dp[i + 1][0] > 0:  # if there are still winning teams after considering the current phase results
            winning_teams.update([f"Team {i+1}"] * dp[i + 1][0])
    return sorted(list(winning_teams))
