def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        dp = [[0] * (m+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(m+1):
                if j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = sum(dp[min(i-1, (n+k+2)//2)][min(j-1, (n+k+2)//2)] * (k < i/2 + n // 2) for k in range(min(i+1, j)+1))
        print((dp[n][m]) % (10**8 + 7))

if __name__ == "__main__":
    solve()
