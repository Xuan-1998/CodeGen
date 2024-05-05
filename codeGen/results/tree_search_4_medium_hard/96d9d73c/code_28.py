from collections import defaultdict

def canPartition(A, K, M):
    N = len(A)
    memo = {}
    
    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i >= N or j < 1:
            return False
        
        if A[i] <= max(memo.get((i-1, j-1), (0, 0))[1]) - M and A[i] >= min(memo.get((i-1, j-1), (0, 0))[1]) + M:
            memo[(i, j)] = dfs(i-1, max(j-1, K))
        else:
            memo[(i, j)] = False
        
        return memo[(i, j)]
    
    dp = [True] * N
    for i in range(1, N):
        for j in range(1, min(i+1, K)+1):
            if dfs(i, j):
                dp[i] = True
            else:
                dp[i] = False
    
    return dp[-1]

# Read input from standard input.
N, K, M = map(int, input().split())
A = list(map(int, input().split()))
print(canPartition(A, K, M))
