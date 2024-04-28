import sys
import itertools

def get_winning_teams(n):
    teams = [i for i in range(2**n)]
    winning_teams = []
    
    for bit_string in itertools.permutations([0, 1], n):
        teams_copy = teams[:]
        for i, bit in enumerate(bit_string):
            if bit == 1:
                teams_copy[i] += 1
        
        if len(set(teams_copy)) == 1:  # Check if all teams have the same skill level
            winning_teams.append(min(teams_copy))
        
    return sorted(list(set(winning_teams)))

n = int(sys.stdin.readline().strip())
print(get_winning_teams(n))
