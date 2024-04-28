import sys

n = int(input())
s = input()

dp = [[0]*2**n for _ in range(n+1)]
winner = [[False]*2**n for _ in range(n+1)]

for i in range(n):
    for j in range(2**n):
        if (s[i] == '1' and winner[i][j]):
            dp[i+1][j] = max(dp[i][j], 2**(n-i-1)-1)
            winner[i+1][j] = True
        elif (s[i] == '0' and winner[i][j]):
            dp[i+1][j] = min(dp[i][j], 2**(n-i-1)-1)
            winner[i+1][j] = False

winning_teams = [i for i in range(2**n) if winner[n][i]]
print(' '.join(map(str, winning_teams)))
