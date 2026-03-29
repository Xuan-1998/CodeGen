def solve():
    t = int(input())
    
    for _ in range(t):
        n, k, z = map(int, input().split())
        arr = list(map(int, input().split()))
        
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(k + 1):
                if j > 0:
                    left_score = dp[i - 1][max(0, j - 1)]
                    right_score = dp[i][min(j - 1, z)] + arr[i]
                    
                    dp[i][j] = max(dp[i][j], left_score, right_score)
                
        print(max(dp[n]))
