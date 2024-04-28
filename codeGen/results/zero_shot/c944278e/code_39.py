import sys
n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
winning_teams = set()

def get_winning_teams(n, s):
    for i in range(2**n):
        team_skill_level = [0]*n
        for j in range(n):
            if ((i >> j) & 1):
                team_skill_level[j] = 1
        winning = True
        for k in range(n-1):
            if (s[k] == '1' and team_skill_level[k] > team_skill_level[k+1]):
                winning = False
                break
        if (winning):
            team_skills_str = ''.join(map(str,team_skill_level))
            winning_teams.add(team_skills_str)

get_winning_teams(n, s)
for team in sorted(list(winning_teams)):
    print(team)
