def solve():
    n = int(input())
    s = input()

    dp = [[True] * (1 << n) for _ in range(n)]
    winning_teams = [[[] for _ in range(1 << n)] for _ in range(n)]

    for i in range(n):
        for j in range(1 << n):
            if not dp[i][j]:
                continue
            win_team = 0
            for k in range(n):
                if s[k] == '1' and (j & (1 << k)):
                    win_team |= 1 << k
            winning_teams[i][win_team] = []
            for team in [t for t in range(1 << n) if dp[i-1][t] and (t & win_team)]:
                if not winning_teams[i-1][team]:
                    continue
                winning_teams[i][win_team].extend(winning_teams[i-1][team])

    winning_teams = [set(team for team in teams if team != 0) for teams in winning_teams[-1]]
    print('\n'.join(map(str, sorted(list(set.union(*[set(team) for team in teams]))))))


if __name__ == '__main__':
    solve()
