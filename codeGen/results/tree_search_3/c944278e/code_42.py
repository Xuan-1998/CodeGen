import sys

def solve(n, s):
    memo = {}
    winning_teams = []

    def is_winner(teams, i):
        if (i, tuple(sorted(teams))) in memo:
            return memo[(i, tuple(sorted(teams)))]
        if i >= n:
            return 1
        winner = teams.index(max(teams[:i+1]))
        losing_teams = sorted([j for j in range(i+1) if j != winner])
        if is_winner(losing_teams, i+1):
            memo[(i, tuple(sorted(teams)))] = 1
            return 1
        else:
            memo[(i, tuple(sorted(teams)))] = 0
            return 0

    for teams in [list(range(2**n))] + [[j-1 for j in range(i+1)] for i in range(n-1, -1, -1)]:
        if is_winner(teams, n-1):
            winning_teams.append(tuple(sorted(teams)))

    return sorted([str(int(''.join(map(str, teams)), 2)) for teams in winning_teams])
