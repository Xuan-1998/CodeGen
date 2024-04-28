import sys
n = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()
teams = []
for i in range(2**n):
    team = [0]*n
    for j in range(n):
        if (i>>j)&1:
            team[j] = 1
    teams.append(team)
for i,team in enumerate(sorted(map(int,''.join('1'if x else '0'for x in team),teams))):
    print(i+1)
