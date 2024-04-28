def max_points(a):
    n = len(a)
    memo = [[0] * (n + 1) for _ in range(n + 1)]
    
    def dp(i, j):
        if i == j:
            return 0
        if memo[i][j]:
            return memo[i][j]
        
        ans = 0
        for k in range(i, j + 1):
            ans = max(ans, a[k] - (k - i) // 2 - (j - k) // 2)
        for k in range(max(1, i), min(j, n)):
            if k - i >= 0 and j - k >= 0:
                memo[i][j] = dp(i, k - 1) + dp(k + 1, j)
                return memo[i][j]
        
        memo[i][j] = ans
        return ans
    
    return max(0, dp(0, n - 1))

n = int(input())
a = list(map(int, input().split()))
print(max_points(a))
