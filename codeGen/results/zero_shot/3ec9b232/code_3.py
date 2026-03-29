def solve():
    n = int(input())
    M = list(map(int, input().split()))
    
    dp = [[0] * (n+1) for _ in range(n+1)]
    
    for m in M:
        for i in range(n-m, -1, -1):
            if dp[i][i+m-1]:
                dp[n][m] += dp[i][i+m-1]
    
    print(dp[n][0] % (10**9 + 7))

if __name__ == "__main__":
    solve()
