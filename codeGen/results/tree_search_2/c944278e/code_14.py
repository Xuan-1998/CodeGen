import sys
from math import comb
from itertools import combinations

def tournament_winner(n):
    # Initialize an empty set for the winning teams
    winning_teams = set()
    
    # Generate all possible permutations of teams
    for r in range(1, 2**n + 1):
        for team in combinations(range(2**n), r):
            # Check if the permutation is a winning team
            if is_winning_team(n, team):
                winning_teams.add(team)
    
    # Sort and print the winning teams
    for team in sorted(list(winning_teams)):
        print(*team)

def is_winning_team(n, team):
    # Generate all possible permutations of the given team
    for r in range(1, len(team) + 1):
        for perm in combinations(team, r):
            # Check if the permutation wins against any other team
            if not any(is_defeated(n, perm, oth_team) for oth_team in set(team) - {oth_member for oth_member in perm}):
                return True
    
    return False

def is_defeated(n, winning_team, losing_team):
    # Check if the winning team defeats the losing team
    for i in range(n):
        if (winning_team & (1 << i)) and not (losing_team & (1 << i)):
            return True
    
    return False

# Read input from stdin
n = int(sys.stdin.readline())

# Solve the problem
tournament_winner(n)
