def find_paths(arr, n, k):
    memo = [[0]*(k+1) for _ in range(n)]
    
    def dfs(i, j, count):
        if i == 0 and j == 0:
            return int(count == k)
        
        if memo[i][j] > 0:
            return memo[i][j]
        
        total = 0
        if i > 0:
            total += dfs(i-1, j, count+arr[i-1][j])
        if j < n-1:
            total += dfs(i, j+1, count+arr[i][j+1])
        
        memo[i][j] = total
        return total
    
    return dfs(n-1, 0, 0)
