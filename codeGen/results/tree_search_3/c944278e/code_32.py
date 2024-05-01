from sys import stdin

def can_win(tournament_results):
    n = len(bin(int('1' * (2 ** (len(tournament_results) - 1)), 2)).strip('0b'))
    dp = [[False] * n for _ in range(2 ** n)]

    for i in range(2 ** n):
        dp[i][0] = True

    for k in range(1, n):
        for j in range(2 ** n):
            for i in range(2 ** n):
                if (tournament_results[(k - 1) % len(tournament_results)] == '1' and
                        (i >> k & 1) == 1) or (tournament_results[(k - 1) % len(tournament_results)] == '0' and
                        (i >> k & 1) == 0):
                    dp[j][k] = dp[i][k-1]

    winning_teams = [i for i in range(2 ** n) if dp[i][n-1]]
    return sorted(winning_teams)

tournament_results = list(map(int, stdin.readline().strip()))
print(can_win(tournament_results))
