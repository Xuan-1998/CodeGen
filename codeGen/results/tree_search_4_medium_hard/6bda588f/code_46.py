def min_f_value():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        
        dp = [[[float('inf')] * (s + 1) for _ in range(n + 1)] for _ in range(s + 1)]
        dp[0][0][0] = 0
        
        for i in range(1, n + 1):
            for j in range(min(i, s) + 1):
                if a[i - 1] <= j:
                    dp[j][i][j] = min(dp[j][i][j], a[i - 1] * (s - j))
                else:
                    dp[j][i][j] = min(dp[j][i][j], (a[i - 1] - s) * (s - j))
        
        print(min(dp[s]))
