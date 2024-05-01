def count_paths(K, N, arr):
    memo = {}
    
    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        if i == N-1 and j == N-1:
            result = 0 if arr[i][j] > K else 1
        elif i > 0 or j > 0:
            if arr[i][j] <= K:
                result = dp(i-1, j) + dp(i, j-1)
            else:
                result = 0
        else:
            result = 0
        
        memo[(i, j)] = result
        return result
    
    return dp(0, 0)

K = int(input())
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

print(count_paths(K, N, arr))
