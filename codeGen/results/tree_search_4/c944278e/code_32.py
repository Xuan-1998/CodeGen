import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
dp = {i: {} for i in range(n+1)}
dp[0][''] = ['']
winning_teams = set()

def update_dp(i, s):
    if '1' not in dp[i-1]:
        return
    teams = dp[i-1][s[:i-1]]
    if s[i-1] == '1':
        new_teams = [t for t in teams if any(t[j] == '1' for j in range(n))]
    else:
        new_teams = [t for t in teams if all(t[j] == '0' for j in range(n))]
    dp[i][s] = new_teams

for i in range(1, n+1):
    for s in ['0', '1']:
        update_dp(i, s)

def get_winning_teams():
    winning_teams_set = set()
    for i in range(n+1):
        if i == 0:
            continue
        for s in dp[i]:
            for team in dp[i][s]:
                if all(team[j] == '1' for j in range(n)):
                    winning_teams_set.add(tuple(sorted([int(x) for x in team])))
    return [list(map(str, team)) for team in sorted(winning_teams_set)]

print(get_winning_teams())
