code
n = int(input())
s = input()
dp = [0] * (1 << n)
max_skill = 0
winning_teams = []
for i in range(1 << n):
    skill = 0
    for j in range(n):
        if ((i >> j) & 1):
            skill += int(s[j])
    dp[i] = skill
    if skill > max_skill:
        max_skill = skill
        winning_teams = [i]
    elif skill == max_skill:
        winning_teams.append(i)
print(*winning_teams, sep='\n')
