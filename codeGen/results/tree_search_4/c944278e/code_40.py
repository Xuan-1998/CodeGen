def winning_teams(n, s):
    dp = [[False] * (1 << n) for _ in range(n + 1)]
    
    for i in range(n + 1):
        if i == 0:
            continue
        
        for j in range(1 << n):
            if not dp[i - 1][j]:
                continue
            
            if s[i - 1] == '1' and (s[i - 1]^j) != 0:
                dp[i][j] = True
            elif s[i - 1] == '0' and (s[i - 1]^j) == 0:
                dp[i][j] = False
    
    winning_teams = []
    
    for j in range(1 << n):
        if any(dp[i][j] for i in range(n + 1)):
            winning_teams.append(j)
    
    return sorted(winning_teams)

n = int(input())
s = input()
print(*winning_teams(n, s), sep='\n')
