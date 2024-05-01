import sys

def solve(n, s):
    dp = [[[] for _ in range(2**i)] for i in range(n+1)]
    dp[0] = [[0]]

    for i in range(n):
        for j in range(2**i):
            # Determine the winner of this match (e.g., based on skill levels)
            if s[i][j % 2] == '1':  # Assuming '1' represents a win
                dp[i+1][j].append(j % 2**i)
            else:
                dp[i+1][j] = []

    winning_teams = []
    for i in range(n, 0, -1):
        if dp[i]:
            winning_teams.extend(list(set([team[0] for team in dp[i]])))
        else:
            break

    return sorted(winning_teams)

# Example usage
n = int(input())
s = input().strip()
print(solve(n, s))
