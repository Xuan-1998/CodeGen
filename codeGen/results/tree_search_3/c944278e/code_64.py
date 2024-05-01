===BEGIN CODE===
n = int(input())
dp = [0] * (1 << n)
skill_levels = []

for i in range(n):
    team_skill_level, result = input().split()
    skill_levels.append(int(team_skill_level))

for i in range(1 << n):
    for j in range(i):
        if (result[j] == 'W' and int(result[i]) != 0) or (result[j] == 'L' and int(result[i]) == 0):
            dp[i] += dp[j]

winning_teams = [i for i in range(1 << n) if dp[i] == (1 << n - 1)]
print(' '.join(map(str, winning_teams)))
===END CODE===
