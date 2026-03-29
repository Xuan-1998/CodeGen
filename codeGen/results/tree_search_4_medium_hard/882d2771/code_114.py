def solve():
    t, l, r = map(int, input().split())
    dp = [[0] * (l + 1) for _ in range(r + 1)]
    
    # Base case: no girls remaining
    dp[0][0] = 0
    
    for i in range(1, r + 1):
        for k in range(min(i, l), -1, -1):
            if k == 0:
                dp[i][k] = i - 1
            else:
                dp[i][k] = min(dp[j][k-1] + 1 for j in range(k))
    
    # Calculate f(n)
    res = t * (dp[l][l] - l) + sum(tj * dj for tj, dj in zip(map(int, input().split()), dp[0]))
    print(res % (10**9 + 7))

solve()
