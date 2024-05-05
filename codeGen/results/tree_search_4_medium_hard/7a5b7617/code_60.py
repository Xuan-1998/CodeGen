def table_configurations(N, M):
    memo = [[0]*M for _ in range(N)]
    
    def dp(i, j):
        if i == 1:
            return 1 if j <= M else 0
        
        if memo[i][j] != -1:
            return memo[i][j]
        
        result = 0
        for k in range(1, j+1):
            result += dp(i-1, j-k)
        
        memo[i][j] = result % (10**9 + 7)
        return memo[i][j]
    
    total_configurations = 0
    for j in range(M+1):
        total_configurations += dp(N, j)
    
    return total_configurations

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(table_configurations(N, M))
