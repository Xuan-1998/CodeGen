def minF(a):
    n = len(a)
    dp = [[0] * (200005) for _ in range(200005)]
    
    for i in range(n):
        s = 0
        for j in range(i, -1, -1):
            if a[j] > s:
                dp[i][s] = min(dp[i][s], dp[j-1][a[j]-s-1] + a[j]*a[j])
            s += a[j]
    
    return dp[n-1][0]

t = int(input())
for _ in range(t):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    print(minF(a))
