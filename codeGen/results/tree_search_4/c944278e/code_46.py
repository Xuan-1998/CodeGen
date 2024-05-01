from bitstring import BitArray

n = int(input())
s = BitArray(bin=input()).int

dp = [[set() for _ in range(1 << n)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1 << n):
        if s[i - 1] == '1':
            dp[i][j].update(dp[i - 1][j])
        else:
            dp[i][j].update({~jk for jk in dp[i - 1][~j]})

winning_teams = [team for team in range(1 << n) if dp[n][team]]

print(*sorted(winning_teams), sep='\n')
