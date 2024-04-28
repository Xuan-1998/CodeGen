import sys
n = int(sys.stdin.readline().strip())
s = list(map(int, sys.stdin.readline().strip()))
winning_teams = []

for i in range(2**n):
    team_skills = [0] * n
    binary_str = bin(i)[2:].zfill(n)
    
    for j in range(n):
        if binary_str[j] == '1':
            team_skills[j] += 1
    
    is_winning_team = True
    for j in range(n-1, -1, -1):
        if s[j] > 0 and (team_skills[j] < s[j]):
            is_winning_team = False
            break
    
    if is_winning_team:
        winning_teams.append(i)

print(' '.join(map(str, sorted(winning_teams))))
