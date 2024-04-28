n = int(input())
s = input()

def find_winning_teams(n, s):
    winning_teams = []
    for i in range(2**n):
        team_skill_level = 0
        for j in range(n):
            if ((i >> j) & 1):
                team_skill_level += 1 if s[j] == '1' else -1
        if team_skill_level > 0:
            winning_teams.append(i)
    return sorted(winning_teams)

print(*find_winning_teams(n, s), sep='\n')
