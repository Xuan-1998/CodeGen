import sys

def solve(n, s):
    dp = [[0] * (1 << n) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][1 << i - 1] = 1

    for i in range(1, n + 1):
        for j in range(1 << i, 1 << (i + 1)):
            dp[i + 1][j | (1 << i)] = max(dp[i][k] for k in range(j) if (k & j) == 0 and s[k >> i] < s[j - 1])

    winning_teams = set()
    for i in range(1, 1 << n):
        if dp[n][i]:
            winning_teams.add(i)

    return sorted(list(winning_teams))

n = int(input())
s = [int(c) for c in input().strip()]
print('\n'.join(map(str, solve(n, s))))
