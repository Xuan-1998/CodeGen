import sys
from itertools import permutations

n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().strip()))
winning_teams = []

for p in permutations(range(2**n), n):
    if all(s[i-1] <= s[i] for i in range(1, n)):
        winning_teams.append(p)

print('\n'.join(map(str, sorted(winning_teams))))
