def solve():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        
        # Initialize 3D array dp
        max_j = max(2 * s, 10**5)
        max_k = max(a[0], 10**5)
        dp = [[[float('inf')] * (max_k + 1) for _ in range(max_j + 1)] for _ in range(n + 1)]
        
        # Base case: i = 1
        for j in range(max_j + 1):
            for k in range(max_k + 1):
                if a[0] - k >= s and (a[0] - k) * (s-j) >= 0:
                    dp[1][j][k] = (a[0] - k) * (s-j)
        
        # Fill in the dynamic programming table
        for i in range(2, n + 1):
            for j in range(max_j + 1):
                for k in range(max_k + 1):
                    if a[i-1] - k >= s and (a[i-1] - k) * (s-j) >= 0:
                        dp[i][j][k] = min(dp[i-1][j'][k'] + (a[i] - k') * (s-j'))
        
        # Find the minimum value of F
        min_f = float('inf')
        for j in range(max_j + 1):
            for k in range(max_k + 1):
                if dp[n][j][k] < min_f:
                    min_f = dp[n][j][k]
        
        print(min_f)

solve()
