def findWinningTeams(n):
    dp = [[[] for _ in range(2**n)] for _ in range(n)]
    
    for i in range(n):
        for mask in range(1 << (i + 1)):
            if (mask >> i) & 1:
                left = dp[i-1][mask ^ (1 << i)][0] + [str(i+1)]
            else:
                left = dp[i-1][mask ^ (1 << i)][0]
            
            right = []
            for team in dp[i-1][mask]:
                if int(team) < i+1:
                    right.append(str(i+1))
                else:
                    right.append(team)
            
            dp[i][mask] = left + right
    
    winningTeams = set()
    for mask in range(2**n):
        for team in dp[n-1][mask]:
            if int(team) != 0:
                winningTeams.add(int(team))
    
    return sorted(list(winningTeams))

n = int(input())
print(findWinningTeams(n))
