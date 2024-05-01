import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

winning_teams = set()
for i in range(2**n):
    team = bin(i)[2:].zfill(n)
    if all((int(s[j], 2) & (1 << int(team[j]))) for j in range(n)):
        winning_teams.add(team)

print("\n".join(sorted(list(winning_teams))))
