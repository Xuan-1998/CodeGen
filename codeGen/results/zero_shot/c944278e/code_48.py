import sys
from itertools import permutations

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

winners = []
for p in permutations([i for i, x in enumerate(s) if x == '1']):
    skill_levels = [2**i for i in p]
    if all(skill_levels[i-1] > skill_levels[i] for i in range(1, len(p))):
        winners.append(' '.join(map(str, sorted(p))))

print('\n'.join(sorted(set(winners))))
