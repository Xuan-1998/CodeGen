def numPaths(arr):
    N = len(arr)
    memo = {}

    def dfs(i, j, k):
        if (i, j, k) in memo:
            return memo[(i, j, k)]
        
        if i == N - 1 and j == N - 1:
            return arr[i][j] == k
        
        total = 0
        if i < N - 1:
            total += dfs(i + 1, j, k)
        if j < N - 1:
            total += dfs(i, j + 1, k)
        
        if arr[i][j] + total == k:
            return total + 1
        else:
            return 0
        
    return dfs(0, 0, K)

K = int(input())
N = int(input())
arr = [[int(x) for x in input().split()] for _ in range(N)]

print(numPaths(arr))
