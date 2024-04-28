code
n = int(input())
dp = [[False] * (1 << n) for _ in range(n)]
for i in range(1, 2**n):
    for j in range(n):
        if ((i >> j) & 1):  # team has won the current game
            dp[j][i] = True
        else:
            dp[j][i] = all(dp[k][i ^ (1 << k)] for k in range(j))  # all previous games were won

winners = [team for team, wins in enumerate([(all(dp[i][2**n-1] for i in range(n)))]) if wins]
print(*sorted(winners), sep='\n')
