def find_winning_teams(n):
    memo = {}

    def dp(i, j):
        if (i, j) not in memo:
            if i == 0:
                return [j]
            else:
                teams = []
                for k in range(2**n):
                    if ((k >> i - 1) & 1) != ((k >> j - 1) & 1):
                        teams.extend(dp(i - 1, k))
                memo[(i, j)] = teams
        return memo[(i, j)]

    winning_teams = dp(n, 0)
    return sorted([i + 1 for i in winning_teams])
