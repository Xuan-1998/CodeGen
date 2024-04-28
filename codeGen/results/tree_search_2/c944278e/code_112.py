from collections import namedtuple

Tournament = namedtuple('Tournament', 'winning_teams')

def solve(n, s):
    dp = [[[] for _ in range(1 << n)] for _ in range(n+1)]
    
    # Base case: when there's only one team left in the tournament
    for i in range((1 << n) - 1, -1, -1):
        if bin(i).count('1') == 1:
            dp[0][i] = [(i,)]

    for curr_level in range(1, n+1):
        for remaining_teams in range((1 << (n - curr_level)), -1, -1):
            # Check the result of the current game
            if s[curr_level-1] == 'W':
                winners = set()
                for i in range((1 << (n - curr_level)), -1, -1):
                    if bin(i).count('1') <= 2:
                        winners.update(dp[curr_level-1][i])
            else:
                winners = {i for i in range((1 << (n - curr_level)), -1, -1) if bin(i).count('1') <= 1}

            # Update the dp table
            dp[curr_level][remaining_teams] = [(winners | i) for i in dp[curr_level-1][remaining_teams] if (winners | i) not in winners]

    winning_teams = set()
    for i in range((1 << n) - 1, -1, -1):
        winning_teams.update(dp[n][i])

    return Tournament(sorted(list(winning_teams)))

n = int(input())
s = input()

print(solve(n, s))
