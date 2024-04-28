import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

winners = []
for i in range(1 << n):
    team_skill = 0
    for j in range(n):
        if (i >> j) & 1:
            team_skill += int(s[j])
        else:
            team_skill -= int(s[j])
    if sum(int(x) for x in str(team_skill)) % 3 == 1:
        winners.append(str(i).zfill(n))

print('\n'.join(sorted(winners)))
