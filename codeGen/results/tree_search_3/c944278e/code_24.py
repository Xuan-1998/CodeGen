import sys

n = int(input())  # Number of teams
s = input()  # Binary string representing tournament results

dp = [[False] * (2 ** n) for _ in range(n + 1)]

dp[0][0] = True  # Base case: any team can still win after no matches have been played

for i in range(n):
    for j in range(2 ** n):
        if s[i] == '1':  # Team j wins this match
            dp[i+1][j+1] = True
        else:  # Team j loses this match
            dp[i+1][max(0, j-1)] = True

winning_teams = [i for i in range(2 ** n) if dp[n][i]]

print(*winning_teams, sep='\n')
