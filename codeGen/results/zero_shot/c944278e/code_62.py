import sys
from itertools import permutations

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

winning_teams = set()
for p in permutations(range(n)):
    score = 0
    for i, v in enumerate(p):
        if s[i] == '1':
            score += 2 ** (n - i - 1)
    winning_teams.add(score)

print(*sorted(list(winning_teams)), sep='\n')
