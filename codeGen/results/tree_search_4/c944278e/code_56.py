def findWinningTeams(n, s):
    dp = [[0 for _ in range(2**n)] for _ in range(n)]

    for i in range(n-1, -1, -1):
        for j in range(2**n):
            if (s[j] == '1' and ((j & (1 << (i+1))) > 0) != ((j & (1 << (i+1+1))) > 0)):
                dp[i][j] = 1
            elif (s[j] == '0' and ((j & (1 << (i+1))) > 0) == ((j & (1 << (i+1+1))) > 0)):
                dp[i][j] = 1

    winning_teams = [str(i).zfill(2**n) for i in range(2**n) if dp[0][i]]
    return '\n'.join(winning_teams)

n = int(input())
s = input()
print(findWinningTeams(n, s))
