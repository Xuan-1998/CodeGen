def count_paths(K, N, arr):
    memo = {}

    def dp(i, j, k):
        if (i, j, k) in memo:
            return memo[(i, j, k)]
        
        if i == N - 1 and j == N - 1:
            if arr[i][j] == k:
                return 1
            else:
                return 0
        
        if k < arr[i][j]:
            return 0
        
        ways = dp(i + 1, j, k - arr[i][j]) + dp(i, j + 1, k - arr[i][j])
        
        memo[(i, j, k)] = ways
        return ways
    
    return dp(0, 0, K)

K, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

print(count_paths(K, N, arr))
