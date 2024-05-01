import sys
from collections import defaultdict

def coin_paths(K, N, arr):
    memo = defaultdict(int)
    dp = [[0] * (N+1) for _ in range(N+1)]

    def dfs(i, j):
        if i > N or j > N:
            return 0
        if i == N and j == N:
            return 1 if arr[i-1][j-1] <= K else 0
        key = (i, j)
        if memo[key]:
            return memo[key]
        
        left = dfs(i, j+1) if j < N else 0
        top = dfs(i+1, j) if i < N else 0
        
        dp[i][j] = left + top
        if arr[i-1][j-1] <= K:
            dp[i][j] += 1 if (i == N and j == N) or (arr[i-1][j-1] < K) else 0
        memo[key] = dp[i][j]
        
        return dp[i][j]

    return dfs(1, 1)

K, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

print(coin_paths(K, N, arr))
