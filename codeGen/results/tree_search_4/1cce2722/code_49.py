def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    dp = [[-1] * (n + 1) for _ in range(n)]
    
    for i in range(n):
        if i == 0:
            dp[i][i] = 0
        elif i == n - 1:
            dp[i][i] = 1
        else:
            for j in range(i + 1):
                if a[j] == a[i]:
                    dp[i][j] = max(dp[i-1][j], dp[i-2][j-2] if i > 0 else dp[0][j])
                elif j == i - 1 and i > 0:
                    dp[i][j] = max(dp[i-1][j], dp[i-2][j-2])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[0][j], dp[n-2][j])
    
    return max(dp[n-1])

print(solve())
