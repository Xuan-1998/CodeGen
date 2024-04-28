import sys
from itertools import permutations

n = int(sys.stdin.readline())
s = str(sys.stdin.readline().strip())

winners = set()
for perm in permutations(range(n), n):
    skill_level = 0
    for i, bit in enumerate(s):
        if (bit == '1' and perm[i] % 2 == 0) or (bit == '0' and perm[i] % 2 != 0):
            skill_level += 1
    winners.add(skill_level)

print('\n'.join(map(str, sorted(list(winners)))))
