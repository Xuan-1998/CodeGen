import sys

def calculate_probability():
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))
    
    # Calculate the total number of teams possible with n players
    total_teams = 1
    for i in range(m):
        if i == h - 1:
            total_teams *= (s[i] + sum(s[:i]) + sum(s[i+1:]))
        else:
            total_teams *= s[i]
    
    # Calculate the number of teams without any players from department h
    no_players_h = 1
    for i in range(m):
        if i == h - 1:
            no_players_h *= sum(s[:i]) + sum(s[i+1:])
        else:
            no_players_h *= s[i]
    
    # Calculate the probability
    if total_teams == 0 or no_players_h == 0:
        return -1.0
    else:
        return (total_teams - no_players_h) / total_teams

print(calculate_probability())
