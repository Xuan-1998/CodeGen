import sys
from collections import defaultdict

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

teams = 2**n
winning_teams = set()

for i in range(1, teams+1):
    bitmask = format(i, 'b').zfill(n)
    skill_level = sum(int(b) for b in bitmask)
    
    if s == bitmask:
        winning_teams.add(skill_level)

winning_teams = sorted(list(winning_teams))
print(*winning_teams, sep='\n')
