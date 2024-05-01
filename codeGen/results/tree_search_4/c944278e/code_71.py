import sys
from itertools import combinations

def find_winners(n):
    winners = set()
    dp = [[] for _ in range(2**n)]

    for i in range(2**n):
        team_combinations = list(combinations(range(n), n))
        winning_teams = set()

        for combination in team_combinations:
            skill_levels = [int(s) for s in bin(i)[2:].zfill(n)]
            if all(skill_levels[j] > 0 for j in combination):
                winning_teams.add(i)
        
        dp[i] = winning_teams

    return sorted(set.union(*dp))

# Read input
n = int(input())

# Generate and print the list of winning teams
winners = find_winners(n)

print("\n".join(map(str, winners)))
