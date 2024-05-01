def find_winning_teams(n, s):
    dp = [[[0] * (1 << n) for _ in range(1 << n)] for _ in range(n + 1)]

    for i in range(n + 1):
        for mask in range(1 << n):
            for team in range(1 << n):
                # Base case: only one team left
                if i == 0:
                    dp[i][mask][team] = 1 if team & mask else 0

                # State transition: update dp based on phase results
                prev_winners = []
                for j in range(n):
                    if (mask >> j) & 1 and s[j]:
                        prev_winners.append(team | (1 << j))
                for winner in prev_winners:
                    dp[i][mask][team] += dp[i - 1][(mask ^ (1 << j))][winner]

    winning_teams = []
    for mask in range(1 << n):
        for team in range(1 << n):
            if dp[n][mask][team]:
                winning_teams.append(team)

    return sorted(winning_teams)
