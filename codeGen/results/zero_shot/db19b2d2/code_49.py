import sys
from math import comb

n, m, h = map(int, input().split())  # read the number of players on the team, departments in the university, and department of interest
s = list(map(int, input().split()))  # read the number of basketball players in each department

# calculate the total number of available players (n) that can be selected for the team
total_available_players = sum(s)

# if there are not enough basketball players to form a team, output -1
if n > total_available_players:
    print(-1)
else:
    # calculate the probability that at least one player from the department of interest is selected for the team
    prob_at_least_one_player_from_interest_department = 0.0
    for i in range(1, n+1):
        num_players_from_interest_department = comb(s[h-1], i) if i <= s[h-1] else 0
        prob_at_least_one_player_from_interest_department += num_players_from_interest_department / (comb(total_available_players, i))
    
    print(prob_at_least_one_player_from_interest_department)
