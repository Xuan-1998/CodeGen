from functools import lru_cache

@lru_cache(maxsize=2**18)
def winners(teams):
    if len(teams) == 1:
        return [teams[0]]
    
    wins = []
    for i in range(len(teams)):
        team = teams[i]
        remaining_teams = teams[:i] + teams[i+1:]
        
        # If the current team has won, recursively find winners from the remaining teams
        if team == 'W':
            winners_of_remaining_teams = winners(remaining_teams)
            for winner in winners_of_remaining_teams:
                wins.append([team] + winner)
    
    return wins

n = int(input())
s = input()

teams = [i for i in range(2**n)]
for i, c in enumerate(s):
    if c == 'W':
        teams[i] = 'W'
    else:
        teams[i] = 'L'

winning_teams = winners(teams)
print(*sorted(map(str, winning_teams)), sep='\n')
