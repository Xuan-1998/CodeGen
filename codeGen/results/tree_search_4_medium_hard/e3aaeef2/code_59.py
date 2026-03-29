def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if j == 0:
                    dp[i][j] = i
                else:
                    last_digit = (i % 10) + 1
                    if last_digit < 10:
                        dp[i][j] = dp[i][j - 1]
                    else:
                        dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1]) + 1
        
        print(dp[n][m])

if __name__ == "__main__":
    solve()
