n = int(input())
s = input()
winning_teams = []
for i in range(2**n):
    team_skill = [0] * n
    binary_str = bin(i)[2:].zfill(n)
    for j in range(n):
        if binary_str[j] == '1':
            team_skill[j] += 1
    if all(team_skill[i] >= int(s[i]) for i in range(n)):
        winning_teams.append(i)
winning_teams.sort()
print('\n'.join(map(str, winning_teams)))
