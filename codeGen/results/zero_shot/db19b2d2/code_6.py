import sys

# Read input
n, m, h = map(int, sys.stdin.readline().split())
players_per_department = list(map(int, sys.stdin.readline().split()))

# Calculate the total number of players
total_players = sum(players_per_department)

# Check if there are enough basketball players in the university to form a team
if n > total_players:
    print(-1)
else:
    # Calculate the probability that a randomly formed team will have at least one player from the department of interest
    num_teams_with_at_least_one_player_from_h = 0
    for i in range(sum(1 for _ in players_per_department)):
        if i < h and total_players - i > n - 1:
            continue
        team_members = set()
        for j in range(min(i + 1, h)):
            team_members.update(set(range(players_per_department[j])))
        if not any(member in team_members for member in range(h, total_players)):
            num_teams_with_at_least_one_player_from_h += 1

    probability = num_teams_with_at_least_one_player_from_h / (2 ** n - 1)
    print(probability)
