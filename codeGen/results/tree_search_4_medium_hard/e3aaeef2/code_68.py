def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        dp = [[0]*(m+1) for _ in range(n+1)]
        for i in range(1, n+1):
            dp[i][0] = i
        for i in range(1, n+1):
            for j in range(1, min(i, m)+1):
                if i == 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = max(dp[i-1][j], j)
        print(dp[n][m]%1000000007)

if __name__ == "__main__":
    solve()
