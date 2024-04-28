import sys
from itertools import permutations

n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().strip()))

winning_teams = set()
for p in permutations(range(n)):
    skill_level = sum(s[i] for i in p)
    if skill_level >= 2**n:
        winning_teams.add(''.join(map(str, p)))

print('\n'.join(sorted(list(winning_teams))))
