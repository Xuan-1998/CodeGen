import sys

def tournament_winner(n):
    dp = [[False] * (1 << n) for _ in range(n + 1)]
    winning_teams = []

    # Base case: there is only one winning team in a single-game tournament
    if n == 1:
        return [(0,)]

    for i in range(1, n + 1):
        for mask in range(1 << i):
            if dp[i - 1][mask & ~(1 << (i - 1))]:
                if (mask >> (i - 1) & 1):
                    # If the current bit is 1, then all winning teams must also win
                    dp[i][mask] = True
                else:
                    # If the current bit is 0, then some winning teams might lose
                    for j in range(i - 1, -1, -1):
                        if (mask >> j & 1) and not dp[j][mask & ~(1 << j)]:
                            break
                    else:
                        dp[i][mask] = True

    # Get all the winning teams by iterating through the last row of dp
    for mask in range(1 << n):
        if dp[n - 1][mask]:
            team_number = [i for i in range(n) if (mask >> i & 1)]
            winning_teams.append(team_number)

    return winning_teams

# Read input from stdin
n = int(sys.stdin.readline())

# Print the output to stdout
print(tournament_winner(n))
