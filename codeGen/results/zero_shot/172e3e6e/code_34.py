def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if a[j - 1] % i == 0:
                dp[i][j] = dp[i - 1][i - 1] + (a.count(a[j - 1]) // i)
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    print((dp[n][n] % (10**9 + 7)))

if __name__ == "__main__":
    main()
