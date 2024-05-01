import sys
from math import log2

def tournament_winner(n):
    # Initialize dp[][] array with zeros
    dp = [[0] * (1 << n) for _ in range(n + 1)]

    # Fill up the dp[][] array using dynamic programming
    for i in range(1, n + 1):
        for j in range(1 << i):
            if i == n:
                # If we've reached the end of the tournament, update dp[i][j] with team j's skill level
                dp[i][j] = log2(j)
            else:
                max_skill = 0
                for k in range(1 << (i - 1)):
                    if ((k >> (n - i)) & 1) == (j >> i):
                        # If team j won the previous round, update dp[i][j] with the maximum skill level achieved by any winning teams
                        max_skill = max(max_skill, dp[i - 1][k])
                dp[i][j] = max_skill

    # Find the winners as the teams whose maximum achievable skill level is higher than or equal to the highest achievable skill level for any winning team
    max_skill = 0
    winners = set()
    for j in range(1 << n):
        if log2(j) > max_skill:
            max_skill = log2(j)
            winners = {j}
        elif log2(j) == max_skill:
            winners.add(j)

    # Print the winners
    print(*sorted(winners), sep='\n')

# Read input from stdin and run the tournament_winner function
n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
tournament_winner(n)
