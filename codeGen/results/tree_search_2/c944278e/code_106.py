from collections import defaultdict

def winning_teams(n, s):
    # Initialize a dictionary to store the number of wins for each team
    dp = defaultdict(int)

    # Iterate through the phases of the tournament
    for i in range(n):
        # For each phase, iterate through the teams and update their win counts
        for j in range(2**i):
            if (s[j] == '1' and s[2*j+1] == '0') or (s[j] == '0' and s[2*j+1] == '1'):
                # If a team wins this phase, increment their win count
                dp[j] += 1

    # Find all teams that can win the tournament by filtering those with more than half the total number of wins
    winning_teams = [team for team in dp if dp[team] > 2**(n-1)]

    return sorted(winning_teams)

# Read input from stdin
n = int(input())
s = input()

# Print the output to stdout
print(*winning_teams(n, s), sep='\n')
