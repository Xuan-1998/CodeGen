def max_points_earned(n, sequence):
    dp = [0] * (n + 1)
    
    def dfs(s):
        if s < 0:
            return 0
        
        if dp[s] > 0:
            return dp[s]
        
        points = 0
        for i in range(a[s-1], a[s]+2):
            if a[s] != i:
                points = max(points, dfs(i - 1) + (s+1))
        
        dp[s] = points
        return points
    
    result = 0
    for s in range(1, n + 1):
        result = max(result, dfs(s))
    
    return result

n = int(input())
sequence = list(map(int, input().split()))
print(max_points_earned(n, sequence))
