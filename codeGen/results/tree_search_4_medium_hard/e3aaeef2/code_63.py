def solve():
    t = int(input())
    mod = 10**9 + 7
    
    dp = [[1] * (m + 1) for _ in range(11)]
    
    for i in range(2, 11):
        for j in range(1, m + 1):
            if i <= 9:
                dp[i][j] = min(dp[i][j - 1], ceil(log10(i)))
            else:
                k = int(str(i)[0])
                dp[i][j] = min(dp[k][j - 1] + ceil(log10(i - k)), dp[i][j - 1])
    
    for _ in range(t):
        n, m = map(int, input().split())
        print(dp[n % mod][m % mod])

solve()
