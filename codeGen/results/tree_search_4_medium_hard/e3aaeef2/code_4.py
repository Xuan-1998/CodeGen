def solve():
    t = int(input())
    
    for _ in range(t):
        n, m = map(int, input().split())
        
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(2, n + 1):
            for j in range(m + 1):
                if j == 0:
                    dp[i][j] = len(str(i))
                else:
                    dp[i][j] = (dp[i // 10**(len(str(i)) - 1)][j - 1] + 1) % (10**9 + 7)
        
        print(dp[n][m])

if __name__ == "__main__":
    solve()
