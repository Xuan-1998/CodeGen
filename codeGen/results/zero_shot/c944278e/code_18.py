import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

winners = []
for i in range(2**n):
    team_skill = 0
    for j in range(n):
        if (i & (1 << j)) > 0:
            team_skill += int(s[n-1-j])
    winners.append((team_skill, bin(i)[2:]))

winners.sort()

print('\n'.join([team[1] for team in winners]))
