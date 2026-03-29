def solution():
    n, m, h = map(int, input().split())
    s = list(map(int, input().split()))
    
    dp = [[0.0 for _ in range(n+1)] for _ in range(m+1)]
    
    total_players = sum(s)
    
    for i in range(1, m+1):
        for k in range(min(i, n)+1):
            if i == 1:
                dp[i][k] = s[0] / total_players
            else:
                dp[i][k] = 1 - (1 - (s[h-1] / total_players)) ** (n-k) * dp[i-1][k-1]
    
    return dp[m][0]

print(solution())
