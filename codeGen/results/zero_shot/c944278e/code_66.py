import sys
n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

winning_teams = set()
def find_winning_teams(n, s):
    for i in range(2**n):
        team_skill = 0
        for j in range(n):
            if ((i >> j) & 1) == (int(s[n-1-j]) % 2):
                team_skill += 1
        if team_skill > 0:
            winning_teams.add(i)
find_winning_teams(n, s)
for team in sorted(list(winning_teams)):
    print(team)
