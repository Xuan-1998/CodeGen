def solve():
    n, k = map(int, input().split())
    s = input()
    dp = [[[] for _ in range(k+1)] for _ in range(n+1)]
    dp[0][0] = [s[:k]]
    
    for i in range(1, n+1):
        for j in range(min(i, k)+1):
            if j == 0:
                dp[i][j] = [s[:i]]
            else:
                if s[i-1] not in dp[i-1][j-1]:
                    dp[i][j] = min(dp[i-1][j-1] + [s[i-1]], dp[i-1][j], key=lambda x: (x, -len(x)))
                else:
                    dp[i][j] = min(dp[i-1][j-1] + [s[i-1]], dp[i-1][j], key=lambda x: (x, -len(x)))
    print(min(dp[n][k], key=lambda x: (x, -len(x))))
