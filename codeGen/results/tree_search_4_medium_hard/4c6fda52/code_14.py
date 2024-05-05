def solve():
    while True:
        n, k = map(int, input().split())
        s = input()
        
        dp = [[0] * (k+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, min(i+1, k)+1):
                if i < k:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = min(dp[i-1][j] + (s[i-k] != 'RGB'[j%3]), dp[i-1][j] + 1)
        
        print(min(dp[n]))

if __name__ == "__main__":
    solve()
