def find_min_f():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        dp = [[0] * (s+1) for _ in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(s+1):
                if i == 1:
                    x = min(a[0], s)
                    y = max(0, a[0]-x)
                    dp[i][j] = (a[0]*x + y*(s-y))
                else:
                    dp[i][j] = float('inf')
                    for k in range(i):
                        for x in range(max(0, a[k]-s), min(a[k], s)+1):
                            y = a[k] - x
                            if (x-s)*(y-s) >= 0:
                                dp[i][j] = min(dp[i][j], dp[k][a[k-1]-s] + (a[k]*x+y*(s-y)))
                    dp[i][j] = min(dp[i][j], dp[i-1][j])
        
        print(min(dp[n]))

find_min_f()
