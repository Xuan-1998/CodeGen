import sys

def is_winning_team(team, phase):
    return any(s[i] == '1' for i in range(phase))

n = int(sys.stdin.readline())
s = [int(c) for c in sys.stdin.readline().strip()]

dp = [[False] * (2 ** n) for _ in range(n)]

for i in range(n):
    for j in range(2 ** n):
        if s[i] == 1:
            dp[i][j] = is_winning_team(j, i)
        else:
            dp[i][j] = any(dp[k][j] and (k < i) for k in range(i))

winning_teams = [team for team in range(2 ** n) if dp[-1][team]]
print('\n'.join(map(str, sorted(winning_teams))))
