def max_points(a):
    n = len(a)
    dp = [[0] * n for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = sum(1 for k in range(i) if (a[k] - a[i]) % 2 == 0)
        
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = max(dp[i][k-1] + 1 for k in range(i+1, j+1) if a[k] == a[i] or a[k] == a[i] - 1)
            
    return dp[0][n-1]

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    print(max_points(a))
