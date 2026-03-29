def solve():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        dp = [[0] * (sum(a) + n*s + 1) for _ in range(n+1)]
        
        for i in range(1, n+1):
            for k in range(sum(a) + n*s + 1):
                if i == 1:
                    if a[0] <= k:
                        dp[i][k] = min(dp[i][k], a[0])
                    else:
                        dp[i][k] = 0
                else:
                    for j in range(min(i, k+1), -1, -1):
                        if j >= s and (j-s) * (a[i-1]-s) >= 0:
                            dp[i][k] = min(dp[i][k], dp[i-1][k-j+a[i-1]] + a[i-1])
                        elif k-j+a[i-1] >= 0:
                            dp[i][k] = min(dp[i][k], dp[i-1][k-j+a[i-1]] + a[i-1])

        print(dp[n][sum(a) - n*s])
