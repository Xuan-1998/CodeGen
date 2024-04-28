import sys
n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
winning_teams = []
for i in range(2**n):
    team = [int(x) for x in bin(i)[2:].zfill(n)]
    if all(s[j] == str(team[j]) for j in range(n)):
        winning_teams.append(''.join(map(str, team)))
winning_teams.sort()
print('\n'.join(winning_teams))
