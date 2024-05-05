def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    dp = [[0] * (max(a) + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(max(a) + 1):
            if a[i-1] % j == 0:
                dp[i][j] = dp[i-1][j//j] + 1
            else:
                dp[i][j] = dp[i-1][j]
    
    ans = sum(dp[n][j] for j in range(max(a) + 1))
    print(ans % (10**9 + 7))

if __name__ == "__main__":
    solve()
