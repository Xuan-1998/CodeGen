import sys

def find_winning_teams(n):
    # Initialize dp array with all False values
    dp = [[False] * (1 << n) for _ in range(n + 1)]

    # Base case: when n = 1, only one team can win
    dp[0][0] = True

    for i in range(1, n + 1):
        for j in range(1 << i):
            if dp[i - 1][j >> 1]:
                # If the current team wins, then all teams with skill level higher than the current one will also win
                for k in range(j << 1, (1 << i) | 0):
                    dp[i][k] = True

    winning_teams = []
    for j in range(1 << n):
        if dp[n - 1][j]:
            winning_teams.append(j)

    return sorted(winning_teams)


# Read input
n = int(sys.stdin.readline())

# Print the result
print(*find_winning_teams(n), sep='\n')
