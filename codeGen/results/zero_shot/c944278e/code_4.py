import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

winning_teams = []
skill_levels = [0] * (1 << n)

for i in range(1 << n):
    skill_level = 0
    for j in range(n):
        if ((i >> j) & 1):
            skill_level += int(s[j])
    winning_teams.append((skill_level, bin(i)[2:]))

winning_teams.sort()

print("\n".join(team[1] for team in winning_teams))
