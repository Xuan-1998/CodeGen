def networkquality():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split()))
        dp = [[False]*1000000 for _ in range(1000000)]
        for i in range(n-1):
            for j in range(b[i], min(i+2,n)):
                if j-b[i] not in [k for k in range(j)]:
                    dp[j][b[i]] = True
        print("YES" if any(dp[n][i]) else "NO")

networkquality()
