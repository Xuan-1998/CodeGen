def find_subset_sums(arr):
    dp = [[0] * (sum(arr) + 1) for _ in range(len(arr) + 1)]
    
    def dfs(i, s):
        if i > len(arr):
            return []
        if dp[i][s]:
            return dp[i][s]
        
        include = dfs(i + 1, s + arr[i])
        exclude = dfs(i + 1, s)
        
        dp[i][s] = [s] + (include if include else [])
        return dp[i][s]
    
    unique_sums = set()
    for i in range(len(arr)):
        for j in range(sum(arr) + 1):
            unique_sums.add(j - dfs(i + 1, j)[0])
    
    return sorted(list(unique_sums))
