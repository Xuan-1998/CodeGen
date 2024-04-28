import sys
from itertools import combinations

def winning_teams(n):
    # Create all possible teams and their skill levels
    teams = [i for i in range(2**n)]

    # Initialize an empty set to store the winning teams
    winning_teams_set = set()

    # Generate all possible team permutations of length n
    for r in range(1, n+1):
        for team in combinations(teams, r):
            # Check if this team permutation is a winning team
            score = 0
            for i, t in enumerate(team):
                if s[n-1-i] == '1':
                    score += 2**i
                else:
                    score -= 2**i
            if score > 0 and tuple(sorted(team)) not in winning_teams_set:
                winning_teams_set.add(tuple(sorted(team)))

    # Sort the winning teams in ascending order and return as a list
    return sorted(list(winning_teams_set))

n = int(input())  # Read n from standard input
s = input()        # Read binary string s of length n from standard input

print(*winning_teams(n), sep='\n')  # Print the winning teams in ascending order
