def solve():
    while True:
        n, k = map(int, input().split())
        if n == 0 and k == 0: break
        s = input()
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(min(i, k) + 1):
                if s[i - 1] != 'RGB'[j % 3]:
                    dp[i][j] = min(dp[i-1][k-1], dp[i-1][j-1]) + 1
        print(min(dp[n-1][:k+1]))
