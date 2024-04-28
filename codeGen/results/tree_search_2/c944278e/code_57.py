import sys

def tournament_winner(n):
    # Initialize the cache
    dp = [[[] for _ in range(2**n)] for _ in range(n+1)]
    
    # Base case: when n = 1, there's only one team that can win
    for i in range(2**n):
        dp[0][i] = [i]
    
    for i in range(1, n+1):
        for j in range(2**n):
            for k in range(2**n):
                if (j >> i) & 1 and (k >> i) & 1:  # If the current bit is set for both teams
                    for team in dp[i-1][j]:
                        for other_team in dp[i-1][k]:
                            if team > other_team:  # Team wins if it's higher than the opponent
                                dp[i][j].append(team)
                elif (j >> i) & 1 and not (k >> i) & 1:  # If only one team has set bits for this bit position
                    for team in dp[i-1][j]:
                        dp[i][j].append(team)
                elif not (j >> i) & 1 and (k >> i) & 1:
                    for other_team in dp[i-1][k]:
                        dp[i][j].append(other_team)
    
    # Find the winning teams
    winning_teams = set()
    for i in range(2**n):
        if dp[n-1][i]:
            for team in dp[n-1][i]:
                winning_teams.add(team)
    
    return sorted(list(winning_teams))

# Read input from stdin
n = int(sys.stdin.readline())

# Calculate the winning teams
winning_teams = tournament_winner(n)

# Print the result to stdout
for team in winning_teams:
    print(team)
