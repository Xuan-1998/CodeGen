import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

dp = [0] * (1 << n)
max_skill = 0
winning_teams = []

for mask in range(1, 1 << n):
    skill = 0
    for i in range(n):
        if ((mask >> i) & 1):
            skill += int(s[i])
    dp[mask] = sum((~mask) & (1 << i)) * (skill > max_skill)
    max_skill = max(max_skill, skill)

for mask in range(1, 1 << n):
    if dp[mask]:
        winning_teams.append(skill)

winning_teams.sort()
print(*winning_teams, sep='\n')
