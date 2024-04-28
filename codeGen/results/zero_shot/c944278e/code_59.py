import sys
from math import comb

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

winners = set()
for i in range(1 << n):
    skill_level = 0
    for j in range(n):
        if (i & (1 << j)):
            skill_level += 1
    if sum((skill_level >> k) & 1 for k in range(n)) >= comb(n, 2):
        winners.add(skill_level)

for winner in sorted(list(winners)):
    print(winner)
