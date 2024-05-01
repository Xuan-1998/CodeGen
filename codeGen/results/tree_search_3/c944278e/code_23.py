import sys

def solve(n, s):
    dp = [[False] * (1 << n) for _ in range(n)]
    winning_teams = []

    for i in range(n):
        for j in range(1 << n):
            if s[i] == 'W' and ((j >> i) & 1):  # team j wins at phase i
                dp[i][j] = True
            elif s[i] == 'L' and not ((j >> i) & 1):  # team j loses at phase i
                for k in range(1 << n):
                    if (k >> i) & 1:  # team k is the winner
                        dp[i][j] = dp[i][k]
            else:
                for k in range(1 << n):
                    if dp[i-1][k]:  # team k can win before phase i
                        dp[i][j] |= (k >> i) & 1

    for j in range(1 << n):
        if all(dp[n-1][j] and not ((j >> i) & 1) for i in range(n)):
            winning_teams.append(j)

    return sorted(winning_teams)

n = int(input())
s = input()
print(*solve(n, s), sep='\n')
