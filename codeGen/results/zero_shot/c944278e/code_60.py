n = int(input())
s = input()
winning_teams = []

def can_win(teams, skill_levels):
    for i in range(len(teams)):
        if teams[i] == 1:
            return False
    return True

for i in range(2**n):
    teams = format(i, 'b').zfill(n)
    if can_win([int(x) for x in teams], [int(x) for x in s]):
        winning_teams.append(teams)

winning_teams.sort()
print('\n'.join(winning_teams))
