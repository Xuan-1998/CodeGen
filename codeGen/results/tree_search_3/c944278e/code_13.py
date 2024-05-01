import sys

def solve(n, s):
    dp = [0] * (2**n + 1)
    for i in range(2**n - 1, -1, -1):
        team_skill = 0
        for j in range(n):
            if ((i >> j) & 1):
                team_skill += int(s[n-1-j])
        dp[i] = sum(dp[k] for k in range(i+1, 2**n) if (k >> j) & 1)
    winning_teams = [team for i, team in enumerate(range(2**n), 1) if (i > 0 and dp[i-1] < dp[i]) or (i == 0)]
    print(*winning_teams)

n = int(input())
s = input()
solve(n, s)
