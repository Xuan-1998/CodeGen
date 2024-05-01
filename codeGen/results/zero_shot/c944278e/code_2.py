import sys

n = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()

all_skills = [0]
for i in range(n):
    new_skills = []
    for skill in all_skills:
        new_skills.append(skill + (1 << i) if s[i] == '1' else skill)
    all_skills = new_skills

winning_teams = sorted([skill for skill in all_skills if bin(skill).count('1') >= n])

for team in winning_teams:
    print(team)
