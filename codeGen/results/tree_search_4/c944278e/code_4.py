===BEGIN CODE===
n = int(input())
s = input()

dp = [[False] * (2**n) for _ in range(n)]

for i in range(n):
    for j in range(2**n):
        if s[i] == '1' or any(s[k] == '1' and dp[k][j] for k in range(i)):
            dp[i][j] = True

winning_teams = [i for i in range(2**n) if dp[n-1][i]]

print(*sorted(winning_teams), sep='\n')
===END CODE===
