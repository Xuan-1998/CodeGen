import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

dp = [[set() for _ in range(2**n)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(2**n):
        if (s[i-1] == '0' and j & (1 << (i-1))) or (s[i-1] == '1' and not j & (1 << (i-1))):
            dp[i][j].update(dp[i-1][team] for team in range(2**n) if ((s[i-1] == '0' and team & (1 << (i-1)))) or ((s[i-1] == '1' and not team & (1 << (i-1))))))
        else:
            dp[i][j].update(dp[i-1][team] for team in range(2**n) if ((s[i-1] == '0' and team & (1 << (i-1)))) or ((s[i-1] == '1' and not team & (1 << (i-1)))))

win_teams = set()
for j in range(2**n):
    win_teams.update(dp[n][j])

print('\n'.join(map(str, sorted(list(win_teams)))))
