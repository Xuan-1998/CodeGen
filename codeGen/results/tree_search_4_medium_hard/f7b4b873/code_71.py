CODE
def palindromic_partitions(S):
    N = len(S)
    dp = [[False] * (N + 1) for _ in range(N + 1)]
    
    for i in range(N + 1):
        dp[i][i] = True
    
    for length in range(2, N + 1):
        for i in range(N - length + 1):
            j = i + length
            if S[i] == S[j - 1]:
                if length == 2 or dp[i + 1][j - 1]:
                    dp[i][j] = True
    
    partitions = []
    def dfs(i, path):
        if i == N:
            partitions.append(path)
            return
        
        for j in range(i, N):
            if dp[i][j + 1]:
                dfs(j + 1, [S[i:j + 1]] + path)
    
    dfs(0, [])
    return partitions
