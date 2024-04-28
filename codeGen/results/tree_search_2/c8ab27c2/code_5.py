from collections import defaultdict

def uncommonFromS(T):
    dp = [[0] * (len(T) + 1) for _ in range(len(input()) + 1)]
    
    memo = defaultdict(int)
    
    def dfs(i, j):
        if i >= len(input()):
            return False
        if j >= len(T):
            return True
        
        if input()[i] == T[j]:
            dp[i][j] = (dp[i-1][j-1] if i > 0 and j > 0 else 1) + (1 if memo[(i, j)] != -1 else dfs(i+1, j+1))
            return bool(dp[i][j])
        elif dp[i][j] == -1:
            dp[i][j] = not dfs(i+1, j)
        return dp[i][j]
    
    for i in range(len(input()) + 1):
        for j in range(len(T) + 1):
            if input()[i-1:i+1] != T[j-1:j+1]:
                memo[(i, j)] = -1
    
    for l1 in range(1, len(input()) + 1):
        for l2 in range(1, len(T) + 1):
            if dfs(len(input()) - l1, len(T) - l2):
                return l1
    return -1

input()
T = input()
print(uncommonFromS(T))
