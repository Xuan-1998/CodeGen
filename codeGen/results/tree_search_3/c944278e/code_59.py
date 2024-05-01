# Read the input n (the number of rounds) and s (the binary string representing the results)
n = int(input())
s = input()

# Initialize a set to store all winning teams
winning_teams = set()

# Iterate through each round
for i in range(n):
    # For each round, find all teams that won in this round
    winning_teams_in_round = {2**i * j for j in range(1<<n) if ((j >> (n - 1 - i)) & 1)}
    
    # Update the set of winning teams by adding all teams from the current round
    winning_teams |= winning_teams_in_round

# Print the winning teams in ascending order
for team in sorted(winning_teams):
    print(team)
