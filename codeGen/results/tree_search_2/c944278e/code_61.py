import sys

def winning_teams(n):
    s = input()
    dp = [[0] * (n + 1) for _ in range(2**n)]
    winning_teams = set()

    # Base case: only one team that can win when n = 1
    if n == 1:
        return {int(s, 2)}

    for i in range(2**n):
        for j in range(n):
            # Calculate the skill level of the current team
            team_skill = int('0' + s[:j+1], 2)
            # Update the maximum skill level considering the next team's result
            if (i >> j) & 1:
                dp[i][j] = max(dp[i][j-1] if j > 0 else team_skill, dp[i ^ (1 << j)][j-1] if j > 0 else 0)
            else:
                dp[i][j] = max(dp[i][j-1] if j > 0 else team_skill, dp[i | (1 << j)][j-1] if j > 0 else 0)

    # Find all the winning teams
    for i in range(2**n):
        if dp[i][-1]:
            winning_teams.add(int(''.join(['1' if ((i >> j) & 1) else '0' for j in range(n)]), 2))

    return sorted(list(winning_teams))
