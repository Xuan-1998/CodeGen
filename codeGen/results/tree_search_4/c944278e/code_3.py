from itertools import combinations

def winning_teams(n, s):
    dp = [[False] * 2**n for _ in range(n)]
    
    for i in range(n-1, -1, -1):
        for j in range(2**n):
            if s[i] == '1':
                for k in range(i):
                    if not s[k] and dp[k][j]:
                        dp[i][j] = True
                        break
    
    winning_teams = [i for i in range(2**n) if dp[-1][i]]
    
    return sorted(winning_teams)

n = int(input())
s = input()
print(*winning_teams(n, s), sep='\n')
